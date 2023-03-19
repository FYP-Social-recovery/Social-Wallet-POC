from utils.fp_preprocessing_utils.segmentation import Segmentation
from utils.fp_preprocessing_utils.normalization import normalize
from utils.fp_preprocessing_utils.gabor_filter import gabor_filter
from utils.fp_preprocessing_utils.frequency import ridge_freq
from utils.fp_preprocessing_utils.orientation import visualize_angles,  calculate_angles 
from utils.fp_preprocessing_utils.skeletonize import skeletonize

import cv2
from PIL import Image

from utils.fuzzy_vault_utils.Chaff_Points_Generator import ChaffPointsGenerator
from utils.fuzzy_vault_utils.Minutia_Converter import MinutiaConverter
from utils.fuzzy_vault_utils.Minutiae_Extractor import MinutiaeExtractor
from utils.fuzzy_vault_utils.Polynomial_Generator import PolynomialGenerator
from utils.fuzzy_vault_utils.Secret_generator import SecretGenerator
from utils.fuzzy_vault_utils.Strings import *
from utils.fuzzy_vault_utils.Constants import *
from utils.fuzzy_vault_utils.Vault_Verifier import VaultVerifier
from utils.fuzzy_vault_utils.Vault import Vault

import os
from subprocess import Popen, PIPE

class FingerPrintController:

# Enrolling fingerprint template
    def read_image(input_img):
        # Open fingerprint image
        fingerprint_image = cv2.imread(input_img)
        
        return fingerprint_image

# Preprocessing Fingerprint
    def fingerprint_pipline(input_img, save_image=False, save_path=None):
        block_size = 16

        resized_fingerprint_image = cv2.resize(input_img, None, fx=2.5, fy=2.5)
        
        # grey scale transformation -> normalization -> orientation -> frequency -> mask -> filtering
        
        # rgb image to grey scale transformation
        gray_scale_image = cv2.cvtColor(resized_fingerprint_image, cv2.COLOR_BGR2GRAY)

        # normalization - removes the effects of sensor noise and finger pressure differences.
        normalized_img = normalize(gray_scale_image.copy(), float(100), float(100))

        # normalisation
        (segmented_img, normim, mask) = Segmentation.create_segmented_and_variance_images(normalized_img, block_size, 0.2)
    
        # orientations
        angles = calculate_angles(normalized_img, W=block_size, smoth=False)

        # find the overall frequency of ridges in Wavelet Domain
        freq = ridge_freq(normim, mask, angles, block_size, kernel_size=5, minWaveLength=5, maxWaveLength=15)

        # create gabor filter and do the actual filtering
        gabor_img = gabor_filter(normim, angles, freq)
        
        # thinning or skeletonize
        thin_image = skeletonize(gabor_img)
        
        if(save_image):
            # save image as a jpg
            im = Image.fromarray(thin_image)
            im.save(save_path)

        return thin_image

# Extract minutiea
    def capture_new_fp_xyt(capturing_fp, echo=False):
        """
        input fingerprint image of type .jpg
        Use mindtct to extract .xyt file from .jpg
        Check if there are enough minutiae detected according to MINUTIAE_POINTS_AMOUNT
        :return: True if enough minutiae detected, else False
        """
        # Tries to read image convert to 
        try:
            # Current image destination folder path and save to new image
            if not os.path.exists(FP_TEMP_FOLDER):
                os.mkdir(FP_TEMP_FOLDER)

            img = Image.open(capturing_fp)
            image_destination_jpg = FP_TEMP_FOLDER + FP_OUTPUT_NAME + '.jpg'
            img.save(image_destination_jpg)
            
            if echo:
                print('The image of %s was saved to %s.' % (FP_OUTPUT_NAME, FP_TEMP_FOLDER))
                print('Finished capturing fingerprint %s.\n' % FP_OUTPUT_NAME)

        except Exception as e:
            print('Operation failed!')
            print('Exception message: ' + str(e))
            raise Exception('An internal error occurred.')
        
        FingerPrintController.run_mindtct(FP_TEMP_FOLDER + FP_OUTPUT_NAME + '.jpg')
        
        # amount of minutiae in .xyt
        num_lines = sum(1 for _ in open(FP_TEMP_FOLDER + FP_OUTPUT_NAME + '.xyt'))
        if num_lines >= MINUTIAE_POINTS_AMOUNT:
            if echo:
                print('{} minutiae were found...'.format(num_lines))
            return True
        else:
            if echo:
                print('Unfortunately, only {} minutiae were found...'.format(num_lines))
            return False

    def run_mindtct(image_path):
        """ Runs mindtct on xyt file path"""
        
        if not os.path.exists(FP_TEMP_FOLDER):
                os.mkdir(FP_TEMP_FOLDER)
                
        mindtct = Popen(['mindtct', image_path, FP_TEMP_FOLDER + FP_OUTPUT_NAME], stdout=PIPE, stderr=PIPE)
        mindtct.communicate()

# Generate vault
    def enroll_new_fingerprint(xyt_path, secret):
        # calculate secret according to polynomial degree. secret has to be able to be encoded in bytes (*8)
        secret_bytes = SecretGenerator.generate_smallest_secret_with_predefined_secret(POLY_DEGREE, CRC_LENGTH, secret, min_size=128, echo=False)
        print(APP_FV_SECRET)

        fuzzy_vault = FingerPrintController.generate_vault(xyt_path, MINUTIAE_POINTS_AMOUNT, CHAFF_POINTS_AMOUNT, POLY_DEGREE,
                                    secret_bytes, CRC_LENGTH, GF_2_M, echo=False)
        
        vault = fuzzy_vault.log_vault()
        
        print(APP_FV_GENERATED)

        print('\n')
        print(APP_ENROLL_SUCCESS)
        
        return vault

    def generate_vault(xyt_input_path, minutiae_points_amount, chaff_points_amount, poly_degree, secret, crc_length,
                    gf_exp, echo=False):
        # extract minutiae from template
        nbis_minutiae_extractor = MinutiaeExtractor()
        minutiae_list = nbis_minutiae_extractor.extract_minutiae_from_xyt(xyt_input_path)
        if len(minutiae_list) < minutiae_points_amount:
            if echo:
                print('Not enough minutiae in template to proceed for generation of vault...')
            
            return None

        vault = Vault()
        m2b = MinutiaConverter()

        # Cut low quality minutiae and convert all minutiae to uint and add to vault
        genuine_minutiae_list = []
        for candidate in minutiae_list:
            if len(genuine_minutiae_list) == minutiae_points_amount:
                break
            too_close = False
            for minutia in genuine_minutiae_list:
                if candidate.distance_to(minutia) <= POINTS_DISTANCE:
                    too_close = True
                    break
            if not too_close:
                genuine_minutiae_list.append(candidate)
        if echo:
            print("Amount of genuin minutiae : ", len(genuine_minutiae_list))
            # print("Genuin minutiae : ", genuine_minutiae_list)
        for minutia in genuine_minutiae_list:
            vault.add_minutia_rep(m2b.get_uint_from_minutia(minutia))
        
        # create chaff points and add to vault
        chaff_points_list = ChaffPointsGenerator.generate_chaff_points_randomly(chaff_points_amount, genuine_minutiae_list,
                                                                                vault.get_smallest_original_minutia(), m2b)
        for chaff_point in chaff_points_list:
            vault.add_chaff_point_rep(m2b.get_uint_from_minutia(chaff_point))
        
        if echo:
            print("Amount of chaff points : ", len(chaff_points_list))
            # print("Chaff minutiae : ", chaff_points_list)
            
        # generate secret polynomial
        secret_poly_generator = PolynomialGenerator(secret, poly_degree, crc_length, gf_exp)
        if echo:
            print('Coefficients of secret polynomial: {}'.format(secret_poly_generator.coefficients))

        # evaluate polynomial at all vault minutiae points (not at chaff points)
        vault.evaluate_polynomial_on_minutiae(secret_poly_generator, echo=echo)

        # generate random evaluation for chaff points
        vault.evaluate_random_on_chaff_points(secret_poly_generator, gf_exp)

        # finalize vault (delete information on vault creation except vault_final_elements_pairs)
        vault.finalize_vault()

        return vault

# Reveal Secret
    def verify_fingerprint(xyt_path):

        db_vault = Vault()
        db_vault.read_vault() # retrieve vault
        
        if db_vault:
            # calculating secret length according to poly degree and crc
            secret_length = SecretGenerator.get_smallest_secret_length(POLY_DEGREE, CRC_LENGTH, min_size=128, echo=False) * 8
                
            db_vault.create_geom_table()
            success = FingerPrintController.verify_secret(xyt_path, MINUTIAE_POINTS_AMOUNT, POLY_DEGREE, CRC_LENGTH, secret_length,
                                    GF_2_M, db_vault, echo=False)
            
            db_vault.clear_vault()
            if success:
                secret = SecretGenerator.extract_secret_from_polynomial_for_predefined_secret(success, CRC_LENGTH, secret_length, POLY_DEGREE, min_size=128)
                print("Generated secret is : ", secret)
                print(APP_VERIFY_SUCCESS)
                return secret
            else:
                print("Secret generation failed!")
                print(APP_VERIFY_FAILURE)
                return False
            
        else:
            print(APP_VERIFY_FAILURE)
            return False

    def verify_secret(xyt_input_path, minutiae_points_amount, poly_degree, crc_length, secret_length, gf_exp, vault: Vault,
                    echo=False):
        """
        :returns: True if match is found, False otherwise
        """
        # extract minutiae from template
        nbis_minutiae_extractor = MinutiaeExtractor()
        minutiae_list = nbis_minutiae_extractor.extract_minutiae_from_xyt(xyt_input_path)

        if len(minutiae_list) < minutiae_points_amount:
            if echo:
                print('Not enough minutiae in template to proceed for extraction of secret...')
            return False

        # extract and restore minutiae from vault using minutiae list from probe, only good quality points taken
        return VaultVerifier.unlock_vault_geom(vault, minutiae_list[0:minutiae_points_amount], poly_degree, gf_exp,
                                            crc_length, secret_length, echo=echo)
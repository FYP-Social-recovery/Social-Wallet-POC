from flet import (
    UserControl,
    Tabs,
    Tab,
    Text,
    TextField,
    Column,
    ElevatedButton,
    colors,
    AppBar,
    IconButton,
    icons,
    CrossAxisAlignment,
    Container,
    FilePicker,
    FilePickerResultEvent,
    AlertDialog,
    TextAlign,
)
from controller.email_controller import EmailController
from controller.fvss_controller import VSS_Controller
from controller.nodeController import NodeContractController
from controller.finger_print_controller import FingerPrintController
from utils.fuzzy_vault_utils.Strings import *
from utils.fuzzy_vault_utils.Constants import *

from utils.symmetricEncryption import SymmetricEncryption
from controller.otp_controller import OTPController

import state

class WalletRecoveryScreen(UserControl):
    def __init__(self, on_back_click, on_submit_click, page):
        super().__init__()
        self.on_back_click = on_back_click
        self.on_submit_click = on_submit_click
        self.page = page
        
        self.txt = ""
        
        def on_dialog_result(e: FilePickerResultEvent):
            print("Selected files:", e.files[0].path)
            print("Selected file or directory:", e.path)
            if(len(e.files) != 0):
                self.biometric.value = e.files[0].path
                self.txt = e.files[0].path
                self.page.update()
        
        self.file_picker = FilePicker(on_result=on_dialog_result)
        self.page.overlay.append(self.file_picker)
        self.page.update()

    
    
    def on_submit_click_fn(self,e):
        if(self.biometric.value):
            # TODO - Request to get shares 
            shares = NodeContractController.getReceivedShares(publicKeyLocal=state.PUBLIC_KEY,privateKeyLocal=state.PRIVATE_KEY,nodeContractAddressLocal=state.NODE_CONTRACT_ADDRESS)
            # TODO - Request to get encryptedVault
            encryptedVault = NodeContractController.getVaultHash(publicKeyLocal=state.PUBLIC_KEY,privateKeyLocal=state.PRIVATE_KEY,nodeContractAddressLocal=state.NODE_CONTRACT_ADDRESS)
            print(shares)
            print(encryptedVault)
            # TODO - Generate combined key using shares
            combined_key = ""
            
            key,iv = SymmetricEncryption.deConcatanate2UnknownLenthBytesObject(SymmetricEncryption.convertIntegerToBytesObject(combined_key))
            
            decryptedVault = SymmetricEncryption.decrypt_vault(encryptedVault,key,iv)
            
            print(decryptedVault)
            
            log_path = VAULT_LOG_FOLDER + VAULT_LOG_FILENAME
            
            with open(log_path, 'w') as file:
                file.write(decryptedVault)
            
            if (len(shares)!=0 and encryptedVault == ""):
            
                print("Start Enrolling")
                # Capture Enrolling fingerprint template
                original_image_path = self.biometric.value #"../data/Original_fp.BMP"
                original_image_template = FingerPrintController.read_image(original_image_path)
                
                # Preprocessing Fingerprint
                preprocessed_image_output_path = "../data/Preprocessed_fp.jpg"

                preprocessed_image = FingerPrintController.fingerprint_pipline(original_image_template, save_image=True, save_path=preprocessed_image_output_path)
                
                # Extract minutiea
                print("Start minutiae extraction")
                good_fp = False
                
                good_fp = FingerPrintController.capture_new_fp_xyt(preprocessed_image_output_path)
                
                ## If good fp enroll
                ## else error
                if not good_fp:
                    print(APP_RETRY_FP)
                    self.open_err_dlg_err()
                else:
                    print("Start Verifying")
                    # Reveal Secret
                    FingerPrintController.verify_fingerprint(FP_TEMP_FOLDER + FP_OUTPUT_NAME + '.xyt')
                    self.on_submit_click(self)
            else:
                self.open_err_dlg_err()
        else:
            self.open_err_dlg_fp()
    
    err_dlg_fp = AlertDialog(
        title=Text("Choose a finger print.", text_align=TextAlign.CENTER), on_dismiss=lambda e: print("Dialog dismissed!")
    )
    
    def open_err_dlg_fp(self):
        self.page.dialog = self.err_dlg_fp
        self.err_dlg_fp.open = True
        self.page.update()
        
    err_dlg_err = AlertDialog(
        title=Text("Something is wrong please try again.", text_align=TextAlign.CENTER), on_dismiss=lambda e: print("Dialog dismissed!")
    )
    
    def open_err_dlg_err(self):
        self.page.dialog = self.err_dlg_err
        self.err_dlg_err.open = True
        self.page.update()
        
        
    def build(self):
        self.biometric= TextField(label="Select a Fingerprint",
                          hint_text="Please select a fingerprint", color="0xFF000000", width=600)
                        
        return Column(
            horizontal_alignment=CrossAxisAlignment.CENTER,
            controls=[
                IconButton(
                    icon=icons.ARROW_BACK_IOS_NEW_SHARP,
                    icon_color=colors.BLUE,
                    on_click=self.on_back_click,
                    icon_size=20,
                    tooltip="Back",
                ),
                Text(value="Wallet Recovery", text_align="center",
                     size=24, color="#2596be"),
                Container(
                    height=20,
                ),
                ElevatedButton("Choose finger print image...",
                    on_click=lambda _: self.file_picker.pick_files(allow_multiple=False)),
                # self.biometric,
                Container(
                    height=10,
                ),
                
                ElevatedButton("Distribute", bgcolor="#2596be",
                               color="white",on_click=self.on_submit_click_fn, width=300,tooltip="Distribute Shares"),
            ],
        )

# if __name__ == '__main__':
    # print("Start Enrolling")
    # # Capture Enrolling fingerprint template
    # original_image_path = "../data/Original_fp.BMP"
    # original_image_template = FingerPrintController.read_image(original_image_path)
    
    # # Preprocessing Fingerprint
    # preprocessed_image_output_path = "../data/Preprocessed_fp.jpg"

    # preprocessed_image = FingerPrintController.fingerprint_pipline(original_image_template, save_image=True, save_path=preprocessed_image_output_path)
    
    # # Extract minutiea
    # print("Start minutiae extraction")
    # good_fp = False
    
    # good_fp = FingerPrintController.capture_new_fp_xyt(preprocessed_image_output_path)
    
    # ## If good fp enroll
    # ## else error
    # if not good_fp:
    #     print(APP_RETRY_FP)
    # else:
    #     print("Start vault generation")
    #     # Generate vault
    #     secret = 81985529216486895
    #     fuzzy_vault = FingerPrintController.enroll_new_fingerprint(FP_TEMP_FOLDER + FP_OUTPUT_NAME + '.xyt', secret)
        
    #     print(fuzzy_vault)
    #     print("\n\n")
        
    #     fuzzy_vault_bytes_object = SymmetricEncryption.convertStringToBytesObject(fuzzy_vault)
        
    #     print(fuzzy_vault_bytes_object)
    #     print("\n\n")
        
    #     encrypted_fuzzy_vault,key,iv = SymmetricEncryption.encrypt_vault_256_bit_key(fuzzy_vault_bytes_object)
        
    #     print(encrypted_fuzzy_vault)
    #     print("\n\n")
        
    #     combined_key_bytes = SymmetricEncryption.concatanate2BytesObject(key,iv)
        
    #     combined_key = SymmetricEncryption.convertBytesObjectToInteger(combined_key_bytes)

    #     print(combined_key)
        
    #     # print("Start Verifying")
    #     # # Reveal Secret
    #     # FingerPrintController.verify_fingerprint(FP_TEMP_FOLDER + FP_OUTPUT_NAME + '.xyt')
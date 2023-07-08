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

from state import GlobalState

class DistributesharesScreen(UserControl):
    
    def __init__(self, on_back_click, on_submit_click, page):
        super().__init__()
        self.on_back_click = on_back_click
        self.on_submit_click = on_submit_click
        self.page = page
        self.email=""
        self.otpHash=""
        self.txt = ""
        self.Emailclient=EmailController()
        self.OTP_client=OTPController()
        
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

    def on_verify_email_click_fn(self,e):
        if(self.email.value):
            #email an OTP to the email address
            self.email=self.email.value
            otp,self.otpHash=self.OTP_client.generateOTPHash()
            self.Emailclient.sendEmail(self.email,otp)
        else:
            self.open_err_dlg_email()

    
    def on_submit_click_fn(self,e):
        print(self.txt)
        print(self.biometric.value)
        if(self.biometric.value):
            if(self.otp.value):
                convertToHash=self.OTP_client.convert_Hash(self.otp.value)[1]
                if (convertToHash==self.otpHash):
                    print("OTP verification successful")
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
                    else:
                        print("Start vault generation")
                        # Generate vault
                        secret = GlobalState.ENTROPHY_VALUE
                        fuzzy_vault = FingerPrintController.enroll_new_fingerprint(FP_TEMP_FOLDER + FP_OUTPUT_NAME + '.xyt', secret)
                        
                        print(fuzzy_vault)
                        print("\n\n")
                        
                        fuzzy_vault_bytes_object = SymmetricEncryption.convertStringToBytesObject(fuzzy_vault)
                        
                        print(fuzzy_vault_bytes_object)
                        print("\n\n")
                        
                        encrypted_fuzzy_vault,key  = SymmetricEncryption.encrypt_vault_128_bit_key(fuzzy_vault_bytes_object) # encrypted_fuzzy_vault,key,iv = SymmetricEncryption.encrypt_vault_256_bit_key(fuzzy_vault_bytes_object)
                        encrypted_fuzzy_vault = SymmetricEncryption.convertByteToString(encrypted_fuzzy_vault)
                        print(encrypted_fuzzy_vault)
                        print("\n\n")
                        
                        combined_key_bytes = key # SymmetricEncryption.concatanate2BytesObject(key,iv)
                        
                        combined_key = SymmetricEncryption.convertBytesObjectToInteger(combined_key_bytes)

                        #print(combined_key)
                        


                        VSS_client=VSS_Controller()
                        shares=VSS_client.get_generated_shares(int(combined_key))
                        #print(type(otpHash))
                        #print(type(encrypted_fuzzy_vault))
                        NodeContractController.addMyShares(shares=[shares[0],shares[1],shares[2]],publicKeyLocal=GlobalState.PUBLIC_KEY,privateKeyLocal=GlobalState.PRIVATE_KEY,nodeContractAddressLocal=GlobalState.NODE_CONTRACT_ADDRESS)
                        
                        #change this function to store email
                        NodeContractController.distribute(publicKeyLocal=GlobalState.PUBLIC_KEY,privateKeyLocal=GlobalState.PRIVATE_KEY,nodeContractAddressLocal=GlobalState.NODE_CONTRACT_ADDRESS,email=self.email,vault=encrypted_fuzzy_vault)
                        
                        self.on_submit_click(self)
                else:
                    self.open_err_dlg_otp()
            else:
                self.open_err_dlg_otp()
        else:
            self.open_err_dlg_fp()
    
    err_dlg_fp = AlertDialog(
        title=Text("Choose a finger print.", text_align=TextAlign.CENTER), on_dismiss=lambda e: print("Dialog dismissed!")
    )
    
    def open_err_dlg_fp(self):
        self.page.dialog = self.err_dlg_fp
        self.err_dlg_fp.open = True
        self.page.update()
        
    err_dlg_email = AlertDialog(
        title=Text("Email field cannot be empty.", text_align=TextAlign.CENTER), on_dismiss=lambda e: print("Dialog dismissed!")
    )

    def open_err_dlg_otp(self):
        self.page.dialog = self.err_dlg_otp
        self.err_dlg_fp.open = True
        self.page.update()
        
    err_dlg_otp = AlertDialog(
        title=Text("OTP verification failed", text_align=TextAlign.CENTER), on_dismiss=lambda e: print("Dialog dismissed!")
    )
    
    def open_err_dlg_email(self):
        self.page.dialog = self.err_dlg_email
        self.err_dlg_email.open = True
        self.page.update()
        
    def build(self):
        self.email=TextField(label="Email Address",
                          hint_text="Please enter a valid email address", color="0xFF000000", width=600)
        self.otp=TextField(label="Enter the One-Time password",
                          hint_text="Please enter the one-time password recieved from email", color="0xFF000000", width=600)
        
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
                Text(value="Distribute Shares", text_align="center",
                     size=24, color="#2596be"),
                Container(
                    height=20,
                ),
                self.email,
                Container(
                    height=10,
                ),
                #sending an OTP email to verify the email
                ElevatedButton("Send OTP", bgcolor="#2596be",
                               color="white",on_click=self.on_verify_email_click_fn, width=300,tooltip="Sending an OTP to verify the email"),
                Container(
                    height=70,
                ),
                self.otp,
                Container(
                    height=10,
                ),
                ElevatedButton("Choose finger print image...",
                    on_click=lambda _: self.file_picker.pick_files(allow_multiple=False)),
                # self.biometric,
                Container(
                    height=10,
                ),
                ElevatedButton("Distribute", bgcolor="#2596be",
                               color="white",on_click=self.on_submit_click_fn, width=300,tooltip="Distribute Shares"),

                Container(
                    height=20,
                ),
                Text(value="Note* : \nBefore pressing 'Distribute' button enter a valid email address\nin the email text field and press 'Send OTP' button.\nAfter that enter the OTP received to the email address in the OTP text field.\nThen select a fingerprint and press 'Distribute' button.", text_align="center", size=14, color="0xFF000000",tooltip="Wallet Public Key", italic=True)
            ],
        )
    
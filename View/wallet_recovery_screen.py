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
from controller.keyGenerationController import KeyGenerationController
from utils.fuzzy_vault_utils.Strings import *
from utils.fuzzy_vault_utils.Constants import *

from utils.symmetricEncryption import SymmetricEncryption
from controller.otp_controller import OTPController

from state import GlobalState

class WalletRecoveryScreen(UserControl):
    
    
    def __init__(self, on_back_click, on_submit_click_wallet_recovery_screen, page):
        super().__init__()
        self.on_back_click = on_back_click
        self.on_submit_click = on_submit_click_wallet_recovery_screen
        self.page = page
        self.mnemonic = ""
        
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

    def send_otp_click(self,e):
        if(self.username.value):
            #request emai for the username
            email=NodeContractController.getEmailByUserName(publicKeyLocal=GlobalState.PUBLIC_KEY,privateKeyLocal=GlobalState.PRIVATE_KEY,nodeContractAddressLocal=GlobalState.NODE_CONTRACT_ADDRESS, userName=self.username.value)
            OTP_client=OTPController()
            otp,self.generated_sigend_otp=OTP_client.generateSignedOTP()
            Email_client=EmailController()
            Email_client.sendEmail(email,otp)
    
    def on_submit_click_fn(self,e):
        if(self.biometric.value):
            if(self.otp_value.value):
                if(self.username.value):
                    shares = NodeContractController.getReceivedShares(publicKeyLocal=GlobalState.PUBLIC_KEY,privateKeyLocal=GlobalState.PRIVATE_KEY,nodeContractAddressLocal=GlobalState.NODE_CONTRACT_ADDRESS)
                    OTP_client=OTPController()
                    self.entered_signed_otp=OTP_client.add_sign(self.otp_value.value)
                    encryptedVault = NodeContractController.getVaultHash(publicKeyLocal=GlobalState.PUBLIC_KEY,privateKeyLocal=GlobalState.PRIVATE_KEY,nodeContractAddressLocal=GlobalState.NODE_CONTRACT_ADDRESS,userName=self.username.value,generated_signed_otp=self.generated_sigend_otp,entered_signed_otp=self.entered_signed_otp)
                    print(shares)
                    print("encryptedVault")
                    print(encryptedVault)

                    VSS_client=VSS_Controller()
                    combined_key = VSS_client.recoverSecret(shares)
                    print(combined_key)
                    
                    # key,iv = SymmetricEncryption.deConcatanate2UnknownLenthBytesObject(SymmetricEncryption.convertIntegerToBytesObject(combined_key))
                    key = SymmetricEncryption.convertIntegerToBytesObject(combined_key,16)
                    print(key)
                    print(type(key))
                    print(type(encryptedVault))
                    decryptedVault = SymmetricEncryption.decrypt_vault_128(SymmetricEncryption.convertStringToBytesObject(encryptedVault),key) # decryptedVault = SymmetricEncryption.decrypt_vault(encryptedVault,key,iv)
                    
                    print(decryptedVault)
                    
                    log_path = VAULT_LOG_FOLDER + VAULT_LOG_FILENAME
                    
                    with open(log_path, 'w') as file:
                        file.write(decryptedVault)
                    
                    if (len(shares)!=0 and encryptedVault != ""):
                    
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
                            secret = FingerPrintController.verify_fingerprint(FP_TEMP_FOLDER + FP_OUTPUT_NAME + '.xyt')
                            GlobalState.RECOVERED_ENTROPHY_VALUE = secret
                            mnemonic = KeyGenerationController.generateMnemonic(secret.to_bytes(16, byteorder='big'))
                            print(mnemonic)
                            self.on_submit_click(self)
                    else:
                        self.open_err_dlg_err()
                else:
                    self.open_err_dlg_uname()
            else:
                self.open_err_dlg_otp()
        else:
            self.open_err_dlg_fp()
        
    # memonic_display = AlertDialog(
    #     title=Text("Recovered Mnemonic Phrase is\n" + self.mnemonic, text_align=TextAlign.CENTER), on_dismiss=lambda e: print("Dialog dismissed!")
    # )
    
    # def open_memonic_display(self):
    #     self.page.dialog = self.memonic_display
    #     self.memonic_display.open = True
    #     self.page.update()
        
    err_dlg_otp = AlertDialog(
        title=Text("Enter a valid OTP.", text_align=TextAlign.CENTER), on_dismiss=lambda e: print("Dialog dismissed!")
    )
    
    def open_err_dlg_otp(self):
        self.page.dialog = self.err_dlg_otp
        self.err_dlg_otp.open = True
        self.page.update()
        
    err_dlg_uname = AlertDialog(
        title=Text("Enter a valid Username.", text_align=TextAlign.CENTER), on_dismiss=lambda e: print("Dialog dismissed!")
    )
    
    def open_err_dlg_uname(self):
        self.page.dialog = self.err_dlg_uname
        self.err_dlg_uname.open = True
        self.page.update()
        
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
        
        self.otp_value = TextField(label="Enter OTP", hint_text="Please enter Your OTP",color="0xFF000000",width=300,tooltip="Enter the OTP in your email")
        self.username = TextField(label="Enter Username", hint_text="Please enter Your Username",color="0xFF000000",width=300,tooltip="Enter the Username")
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
                self.username,
                Container(
                    height=10,
                ),
                ElevatedButton("Send OTP", bgcolor="#2596be",
                               color="white",on_click=self.send_otp_click, width=300,tooltip="send OTP"),
                
                Container(
                    height=50,
                ),
                ElevatedButton("Choose finger print image...",
                    on_click=lambda _: self.file_picker.pick_files(allow_multiple=False)),
                Container(
                    height=10,
                ),
                self.otp_value,
                Container(
                    height=10,
                ),
                
                ElevatedButton("Recover", bgcolor="#2596be",
                               color="white",on_click=self.on_submit_click_fn, width=300,tooltip="Distribute Shares"),
                
                Container(
                    height=20,
                ),
                Text(value="Note* : \nBefore pressing 'Recover' button enter the Username\nin the Username text field and press 'Send OTP' button.\nAfter that enter the OTP received to the email address in the OTP text field.\nThen select a fingerprint and press 'Recover' button.", text_align="center", size=14, color="0xFF000000",tooltip="Wallet Public Key", italic=True)
            ],
        )
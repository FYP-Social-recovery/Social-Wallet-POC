from controller.keyGenerationController import KeyGenerationController
from controller.publicContractController import PublicContractController
from controller.nodeController import NodeContractController
from controller.otp_controller import OTPController
from controller.email_controller import EmailController
from flet import (
    UserControl,
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
    AlertDialog,
    TextAlign,
)

from state import GlobalState

class RecoveryRequestScreen(UserControl):
    
    def __init__(self, on_back_click, on_continue_click):
        super().__init__()
        self.on_back_click = on_back_click
        self.on_continue_click = on_continue_click
        self.generated_otp_hash=""

    #function to get email address form node controller and generate an OTP to send
    def send_otp_click(self,e):
        if(self.username.value):
            #request emai for the username
            email=NodeContractController.getEmailByUserName(publicKeyLocal=GlobalState.PUBLIC_KEY,privateKeyLocal=GlobalState.PRIVATE_KEY,nodeContractAddressLocal=GlobalState.NODE_CONTRACT_ADDRESS, userName=self.username.value)
            OTP_client=OTPController()
            otp,self.generated_sigend_otp=OTP_client.generateSignedOTP()
            Email_client=EmailController()
            Email_client.sendEmail(email,otp)

            
    
    def continue_click(self,e):
        if(self.otp_value.value):
            if(self.username.value):
                print("OTP : " , self.otp_value.value)
                print("Username : " , self.username.value)
                # TODO - Request to sent wallet recovery requests
                OTP_client=OTPController()
                self.entered_signed_otp=OTP_client.add_sign(self.otp_value.value)

                #this method should add new variables signed msg1,signed msg2
                NodeContractController.requestShares(publicKeyLocal=GlobalState.PUBLIC_KEY,privateKeyLocal=GlobalState.PRIVATE_KEY,nodeContractAddressLocal=GlobalState.NODE_CONTRACT_ADDRESS, userName=self.username.value, generated_signed_otp=self.generated_sigend_otp,entered_signed_otp=self.entered_signed_otp)
                self.on_continue_click(self)
            else:
                self.open_err_dlg_uname()
        else:
            self.open_err_dlg_otp()
        
        
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
    
    def build(self):
        
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
                Text(value="Recovery Request", text_align="center",
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
                    height=70,
                ),
                self.otp_value,
                Container(
                    height=10,
                ),
                ElevatedButton("Request", bgcolor="#2596be",
                               color="white",on_click=self.continue_click, width=300,tooltip="Initiate recovery request"),
                
                Container(
                    height=20,
                ),
                Text(value="Note* : \nBefore pressing 'Request' button enter the Username\nin the Username text field and press 'Send OTP' button.\nAfter that enter the OTP received to the email address in the OTP text field.\nThen press 'Request' button.", text_align="center", size=14, color="0xFF000000",tooltip="Wallet Public Key", italic=True)
            ],
        )
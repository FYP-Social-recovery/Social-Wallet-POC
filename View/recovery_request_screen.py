from controller.keyGenerationController import KeyGenerationController
from controller.publicContractController import PublicContractController
from controller.nodeController import NodeContractController
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
)

import state

class RecoveryRequestScreen(UserControl):
    def __init__(self, on_back_click, on_continue_click):
        super().__init__()
        self.on_back_click = on_back_click
        self.on_continue_click = on_continue_click

    
    
    def continue_click(self,e):
        #otp vrification call
        self.on_continue_click(self)
        
    
    
    def build(self):
        
        self.otp_value = TextField(label="Enter OTP", hint_text="Please enter Your OTP",color="0xFF000000",width=300,tooltip="Enter the OTP in your email")
        
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
                Text(value="OTP verification", text_align="center",
                     size=24, color="#2596be"),
                Container(
                    height=100,
                ),
                self.otp_value,
                Container(
                    height=10,
                ),
                
                Container(
                    height=100,
                ),
                ElevatedButton("Verify", bgcolor="#2596be",
                               color="white",on_click=self.continue_click, width=300,tooltip="Verify OTP"),
            ],
        )
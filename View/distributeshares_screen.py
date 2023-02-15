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
)
from controller.email_controller import EmailController
from controller.fvss_controller import VSS_Controller
from controller.nodeController import NodeContractController

import state

class DistributesharesScreen(UserControl):
    def __init__(self, on_back_click,on_submit_click):
        super().__init__()
        self.on_back_click = on_back_click
        self.on_submit_click = on_submit_click

    
    def on_submit_click_fn(self,e):
        
        if(self.email.value):
            Emailclient=EmailController()
            VSS_client=VSS_Controller()
            #Emailclient.sendEmail("tharindathamaranga98@gmail.com","Successfullly added Email!")
            #shares=VSS_client.get_generated_shares(int("1222222222222222222222222"))
            #NodeContractController.addMyShares(shares=[shares[0],shares[1],shares[3]],publicKeyLocal=state.PUBLIC_KEY,privateKeyLocal=state.PRIVATE_KEY,nodeContractAddressLocal=state.NODE_CONTRACT_ADDRESS)
            NodeContractController.distribute(publicKeyLocal=state.PUBLIC_KEY,privateKeyLocal=state.PRIVATE_KEY,nodeContractAddressLocal=state.NODE_CONTRACT_ADDRESS)
            self.on_submit_click(self)
        else:
            self.open_err_dlg()

    def build(self):
        self.email=TextField(label="Email Address",
                          hint_text="Please enter a valid email address", color="0xFF000000", width=600)
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
                self.biometric,
                Container(
                    height=10,
                ),
                self.email,
                Container(
                    height=10,
                ),
                
                ElevatedButton("Distribute", bgcolor="0xFFFFAB2E",
                               color="0xFF986D34",on_click=self.on_submit_click_fn, width=300),
            ],
        )

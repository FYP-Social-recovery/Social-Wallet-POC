from controller.nodeController import NodeContractController
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
    Divider,
)

from state import GlobalState

class RecoveryHomeScreen(UserControl):
    def __init__(self, on_back_click, on_add_shareholders_click, on_shareholders_status_click, on_distribute_shares_click, on_registration_click,on_request_view_click, on_wallet_recovery_request_click, on_wallet_recovery_request_view_click, on_wallet_recovery_click):
        super().__init__()
        self.on_back_click = on_back_click
        self.on_add_shareholders_click = on_add_shareholders_click
        self.on_shareholders_status_click = on_shareholders_status_click
        self.on_distribute_shares_click = on_distribute_shares_click
        self.on_registration_click = on_registration_click
        self.on_request_view_click=on_request_view_click
        self.on_wallet_recovery_request_click = on_wallet_recovery_request_click
        self.on_wallet_recovery_request_view_click = on_wallet_recovery_request_view_click
        self.on_wallet_recovery_click = on_wallet_recovery_click
        
        self.state = "NOT_REGISTERED"
        
        # if(GlobalState.NODE_CONTRACT_ADDRESS!=""):
        #     self.state= NodeContractController.getMyState(GlobalState.PUBLIC_KEY, GlobalState.PRIVATE_KEY, GlobalState.NODE_CONTRACT_ADDRESS)
        
        print(self.state)
        
        print("Contract address is : ", GlobalState.NODE_CONTRACT_ADDRESS)
        print("Username is : ", GlobalState.USERNAME)

    def build(self):
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
                Text(value="Setup Menu", text_align="center",
                     size=24, color="#2596be"),
                Container(
                    height=20,
                ),
                # topic
                Text(value="Register user to public contract", text_align="center",
                     size=15, color="Black"),
                Container(
                    width=300,
                    content=Divider(height=9, thickness=3),
                ),
                ElevatedButton(text="registration", on_click=self.on_registration_click,bgcolor="#2596be",
                                color="white",tooltip="social recovery registration"),
                Container(
                    height=10,
                ),
                # topic
                Text(value="Wallet owner features", text_align="center",
                     size=15, color="Black"),
                Container(
                    width=300,
                    content=Divider(height=9, thickness=3),
                ),
                ElevatedButton(text="Add Shareholders", on_click=self.on_add_shareholders_click,bgcolor="#2596be",
                                color="white",tooltip="Requst to add shareholders"),
                Container(
                    height=10,
                ),
                ElevatedButton(text="Shareholder Status", on_click=self.on_shareholders_status_click,bgcolor="#2596be",
                                color="white",tooltip="view accept/reject status of shareholders"),
                Container(
                    height=10,
                ),
                ElevatedButton(text="Distribute Shares", on_click=self.on_distribute_shares_click,bgcolor="#2596be",
                                color="white",tooltip="Distribute the shares"),
                Container(
                    height=10,
                ),
                
                Text(value="Shareholder features", text_align="center",
                     size=15, color="Black"),
                Container(
                    width=300,
                    content=Divider(height=9, thickness=3),
                ),
                ElevatedButton(text="Accept Shareholder Requests", on_click=self.on_request_view_click,bgcolor="#2596be",
                                color="white",tooltip=""),
                Container(
                    height=10,
                ),
                
                Text(value="Wallet recovery features", text_align="center",
                     size=15, color="Black"),
                Container(
                    width=300,
                    content=Divider(height=9, thickness=3),
                ),
                ElevatedButton(text="Request for Wallet recovery", on_click=self.on_wallet_recovery_request_click,bgcolor="#2596be",
                                color="white",tooltip=""),
                Container(
                    height=10,
                ),
                ElevatedButton(text="Recovery request view", on_click=self.on_wallet_recovery_request_view_click,bgcolor="#2596be",
                                color="white",tooltip=""),
                Container(
                    height=10,
                ),
                ElevatedButton(text="Recover wallet", on_click=self.on_wallet_recovery_click,bgcolor="#2596be",
                                color="white",tooltip=""),
                Container(
                    height=10,
                ),
                # Container(
                #     height=10,
                # ),
                # ElevatedButton("Submit", bgcolor="#2596be",
                #                color="white", width=300),
            ],
        )

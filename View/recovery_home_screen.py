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
)

import state

class RecoveryHomeScreen(UserControl):
    def __init__(self, on_back_click, on_add_shareholders_click, on_shareholders_status_click, on_distribute_shares_click, on_registration_click,on_request_view_click):
        super().__init__()
        self.on_back_click = on_back_click
        self.on_add_shareholders_click = on_add_shareholders_click
        self.on_shareholders_status_click = on_shareholders_status_click
        self.on_distribute_shares_click = on_distribute_shares_click
        self.on_registration_click = on_registration_click
        self.on_request_view_click=on_request_view_click
        
        self.state = "NOT_REGISTERED"
        
        # if(state.NODE_CONTRACT_ADDRESS!=""):
        #     self.state= NodeContractController.getMyState(state.PUBLIC_KEY, state.PRIVATE_KEY, state.NODE_CONTRACT_ADDRESS)
        
        print(self.state)
        
        print("Contract address is : ", state.NODE_CONTRACT_ADDRESS)
        print("Username is : ", state.USERNAME)

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
                Text(value="Social Recovery Menu", text_align="center",
                     size=24, color="#2596be"),
                Container(
                    height=20,
                ),
                ElevatedButton(text="registration", on_click=self.on_registration_click,bgcolor="#2596be",
                                color="white",tooltip="social recovery registration"),
                Container(
                    height=10,
                ),
                ElevatedButton(text="Accept Shareholder Requests", on_click=self.on_request_view_click,bgcolor="#2596be",
                                color="white",tooltip="see the request list"),
                Container(
                    height=10,
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
                # Container(
                #     height=10,
                # ),
                # ElevatedButton("Submit", bgcolor="#2596be",
                #                color="white", width=300),
            ],
        )

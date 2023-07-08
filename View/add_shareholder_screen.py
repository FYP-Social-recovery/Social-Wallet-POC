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
from controller.nodeController import NodeContractController

from state import GlobalState

class AddShareholderScreen(UserControl):
    def __init__(self, on_back_click, on_request_click):
        super().__init__()
        self.on_back_click = on_back_click
        self.on_request_click = on_request_click

    def request_click(self, e):
        for i in range(3):
            NodeContractController.addTemporaryShareHolder(share_holder= self.__class__.TextFieldArray[i].value, publicKeyLocal= GlobalState.PUBLIC_KEY,privateKeyLocal= GlobalState.PRIVATE_KEY,nodeContractAddressLocal= GlobalState.NODE_CONTRACT_ADDRESS)
        
        NodeContractController.makeHolderRequests(publicKeyLocal= GlobalState.PUBLIC_KEY,privateKeyLocal= GlobalState.PRIVATE_KEY,nodeContractAddressLocal= GlobalState.NODE_CONTRACT_ADDRESS)
        
        self.on_request_click(self)

    TextFieldArray=[]
    for i in range(3):
        textFiled=TextField(label="Share Holder "+str(i+1),
                  hint_text="Please enter an address", color="0xFF000000", width=600)
        TextFieldArray.append(textFiled)

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
                Text(value="Add Shareholders", text_align="center",
                     size=24, color="#2596be"),
                Container(
                    height=20,
                ),
                self.__class__.TextFieldArray[0],
                Container(
                    height=10,
                ),
                self.__class__.TextFieldArray[1],
                Container(
                    height=10,
                ),
                self.__class__.TextFieldArray[2],
                # Container(
                #     height=10,
                # ),
                # self.__class__.TextFieldArray[3],
                # Container(
                #     height=10,
                # ),
                # self.__class__.TextFieldArray[4],
                Container(
                    height=10,
                ),
                ElevatedButton("Request", bgcolor="#2596be",
                               color="white", width=300, on_click=self.request_click),
            ],
        )

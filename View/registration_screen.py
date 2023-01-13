from controller.nodeController import NodeController
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

class RegistrationScreen(UserControl):
    def __init__(self, on_back_click, on_submit_click):
        super().__init__()
        self.on_back_click = on_back_click
        self.on_submit_click = on_submit_click

    def checkValidity(self,e):
        userNameExistence=NodeController.checkUserExists(self.user_name.value)
        print("Is user Exists : ",userNameExistence)
    
    def checkValidity_fn(self, e):
        userNameExistence= False #NodeController.checkUserExists(self.user_name.value)
        print("Is user Exists : ",userNameExistence)
        
        return userNameExistence
        
    def on_submit_click_fn(self,e):
        userNameExistence= NodeController.checkUserExists(self.user_name.value)
        print("Is user Exists : ",userNameExistence)
        if(not userNameExistence):
            print(state.PRIVATE_KEY)
            contractAddress=NodeController.deploy(state.PUBLIC_KEY, state.PRIVATE_KEY)
            print("Contract address is : ",contractAddress)
            state.NODE_CONTRACT_ADDRESS = contractAddress
            state.USERNAME = self.user_name.value
        
            self.on_submit_click(self)
    
    def build(self):
        self.user_name = TextField(label="Enter a username", hint_text="Please enter a username here",color="0xFF000000",width=600)
        return Column(
            horizontal_alignment=CrossAxisAlignment.CENTER,
            controls=[
                IconButton(
                    icon=icons.ARROW_BACK_IOS_NEW_SHARP,
                    icon_color=colors.GREEN,
                    on_click=self.on_back_click,
                    icon_size=30,
                ),
                Text(value="Enter a username", text_align="center",
                     size=24, color="0xFFA36D1D"),
                Container(
                    height=100,
                ),
                self.user_name,
                Container(
                    height=10,
                ),
                ElevatedButton(text="Check Validity",on_click=self.checkValidity),
                Container(
                    height=100,
                ),
                ElevatedButton("Submit", bgcolor="0xFFFFAB2E",
                               color="0xFF986D34",on_click=self.on_submit_click_fn, width=300),
            ],
        )

from controller.nodeController import NodeController
from controller.publicContractController import PublicContractController
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
    Page,
    TextAlign,
)

import state

class RegistrationScreen(UserControl):
    def __init__(self, on_back_click, on_submit_click, page:Page):
        super().__init__()
        self.on_back_click = on_back_click
        self.on_submit_click = on_submit_click
        self.page = page
        
        print(state.USERNAME)
        
        self.user_name_text = ""
        
        if(state.USERNAME!="" or state.NODE_CONTRACT_ADDRESS !=""):
            self.user_name_text = "Username :\n" + state.USERNAME + "\n\n" + "Node Contract address :\n" + state.NODE_CONTRACT_ADDRESS
        
        print(self.user_name_text)

    def checkValidity(self,e):
        userNameExistence=PublicContractController.checkUserExists(self.user_name.value, state.PUBLIC_KEY, state.PRIVATE_KEY)
        print("Is user Exists : ",userNameExistence)
        if(userNameExistence):
            self.open_err_dlg()
        else:
            self.open_suc_dlg()
        
    def on_submit_click_fn(self,e):
        userNameExistence= PublicContractController.checkUserExists(self.user_name.value, state.PUBLIC_KEY, state.PRIVATE_KEY)
        print("Is user Exists : ",userNameExistence)
        if(not userNameExistence):
            print(state.PRIVATE_KEY)
            contractAddress=NodeController.deploy(state.PUBLIC_KEY, state.PRIVATE_KEY)
            print("Node Contract address is : ",contractAddress)
            state.NODE_CONTRACT_ADDRESS = contractAddress
            state.USERNAME = self.user_name.value
            
            NodeController.register(self.user_name.value, state.PUBLIC_KEY, state.PRIVATE_KEY, contractAddress)
        
            self.on_submit_click(self)
        else:
            self.open_err_dlg()
    
    err_dlg = AlertDialog(
        title=Text("Name not available", text_align=TextAlign.CENTER), on_dismiss=lambda e: print("Dialog dismissed!")
    )
    
    suc_dlg = AlertDialog(
        title=Text("Name available", text_align=TextAlign.CENTER), on_dismiss=lambda e: print("Dialog dismissed!")
    )
    
    def open_err_dlg(self):
        self.page.dialog = self.err_dlg
        self.err_dlg.open = True
        self.page.update()

    def open_suc_dlg(self):
        self.page.dialog = self.suc_dlg
        self.suc_dlg.open = True
        self.page.update()
        
    def build(self):
        
        if (self.user_name_text):
            return Column(
                horizontal_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    IconButton(
                        icon=icons.ARROW_BACK_IOS_NEW_SHARP,
                        icon_color=colors.GREEN,
                        on_click=self.on_back_click,
                        icon_size=30,
                    ),
                    Text(value="Username", text_align="center",
                            size=24, color="0xFFA36D1D"),
                    Container(
                        height=100,
                    ),
                    Text(value=self.user_name_text, text_align="center",
                            size=24, color="0xFF000000"),
                    Container(
                        height=10,
                    ),
                ],
            )
        else:
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

from controller.keyGenerationController import KeyGenerationController
from controller.publicContractController import PublicContractController
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

class WalletImportScreen(UserControl):
    def __init__(self, on_back_click, on_continue_click):
        super().__init__()
        self.on_back_click = on_back_click
        self.on_continue_click = on_continue_click

    
    
    def continue_click(self,e):
        privateKey,publicKey=KeyGenerationController.importWalletFromMnemonic(self.mnemonic_phrase.value)
        print(self.mnemonic_phrase.value)
        print("privatekey: ",privateKey)
        print("Public key: ",publicKey)

        contractAddress=PublicContractController.getContractAddressByPublicAddress(publicKey, privateKey)
        userName=NodeController.getUserName(publicKey, privateKey)
       
        if(contractAddress!="0x0000000000000000000000000000000000000000"):
            state.NODE_CONTRACT_ADDRESS = contractAddress
            
            # state.USERNAME = self.user_name.value 
        
        state.PRIVATE_KEY = privateKey
        state.PUBLIC_KEY = publicKey
        
        self.on_continue_click(self)
        
    
    
    def build(self):
        
        self.mnemonic_phrase = TextField(label="Enter Mnemonic phrase", hint_text="Please enter Mnemonic phrase",color="0xFF000000",width=600,tooltip="Enter the Menmonic Phrase")
        
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
                Text(value="Import Wallet", text_align="center",
                     size=24, color="#2596be"),
                Container(
                    height=100,
                ),
                self.mnemonic_phrase,
                Container(
                    height=10,
                ),
                
                Container(
                    height=100,
                ),
                ElevatedButton("Continue", bgcolor="#2596be",
                               color="white",on_click=self.continue_click, width=300,tooltip="Import Wallet"),
            ],
        )

from controller.keyGenerationController import KeyGenerationController
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
        if(contractAddress!="0x0000000000000000000000000000000000000000"):
            state.NODE_CONTRACT_ADDRESS = contractAddress
            
            # state.USERNAME = self.user_name.value 
        
        state.PRIVATE_KEY = privateKey
        state.PUBLIC_KEY = publicKey
        
        self.on_continue_click(self)
        
    
    
    def build(self):
        
        self.mnemonic_phrase = TextField(label="Enter Mnemonic phrase", hint_text="Please enter Mnemonic phrase",color="0xFF000000",width=600)
        
        return Column(
            horizontal_alignment=CrossAxisAlignment.CENTER,
            controls=[
                IconButton(
                    icon=icons.ARROW_BACK_IOS_NEW_SHARP,
                    icon_color=colors.GREEN,
                    on_click=self.on_back_click,
                    icon_size=30,
                ),
                Text(value="Import Wallet", text_align="center",
                     size=24, color="0xFFA36D1D"),
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
                ElevatedButton("Continue", bgcolor="0xFFFFAB2E",
                               color="0xFF986D34",on_click=self.continue_click, width=300),
            ],
        )

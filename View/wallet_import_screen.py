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

from state import GlobalState

class WalletImportScreen(UserControl):
    def __init__(self, on_back_click, on_continue_click):
        super().__init__()
        self.on_back_click = on_back_click
        self.on_continue_click = on_continue_click

    
    
    def continue_click(self,e):
        GlobalState.ENTROPHY_VALUE = ""
        GlobalState.PRIVATE_KEY = ""
        GlobalState.PUBLIC_KEY = ""
        GlobalState.USERNAME = ""
        GlobalState.NODE_CONTRACT_ADDRESS = ""
        if(self.mnemonic_phrase.value=="1"):
            # Bob - 1 Owner
            privateKey,publicKey="635692a5b8c388a50c4d2c4987426a7c7b7cc9fa1815aed74e52d192244aad1a", "0xF4d86E60b3fA7f1fD4AD2b41205D52b57Ce68905"
            GlobalState.ENTROPHY_VALUE = 81985529216486895        
        elif(self.mnemonic_phrase.value=="2"):
            # Alice - 2 1
            privateKey,publicKey="7a032b39be8f54d44000fe9f7f8bb157f06a37ef1b08c6bed91d209a3202cf61", "0xA21831e3493CfAaA6f23b0efBa00B5F47A59bb34"
            GlobalState.ENTROPHY_VALUE = 81985529216486895        
        elif(self.mnemonic_phrase.value=="3"):
            # Charlie - 3 2
            privateKey,publicKey="9e0b07d20ad817db8705c10db5323b4a74dda1b07c32f931e140b5c5ef2d9a85", "0x3B413d6f4b7d69E05707Db0E29bE01BcFB774F85"
            GlobalState.ENTROPHY_VALUE = 81985529216486895        
        elif(self.mnemonic_phrase.value=="4"):
            # Tom - 4 2
            privateKey,publicKey="17f5a80058fa4b52f6d73a339f03aaf4d0959435a31a31946061a6ecb4049e9b", "0x635fA2a24282B5a157401592f39356866643125C"
            GlobalState.ENTROPHY_VALUE = 81985529216486895        
        elif(self.mnemonic_phrase.value=="5"):
            # Peter - 5 Recover
            privateKey,publicKey="ffc73e77bef189de26c48729532ca156e15a68d65c857689392eb3090a9d5a03", "0x8DFA4358CE13dB53c466D6eABDC40439B8950d0c"
            GlobalState.ENTROPHY_VALUE = 81985529216486895        
        else:
            privateKey,publicKey = KeyGenerationController.importWalletFromMnemonic(self.mnemonic_phrase.value)
            GlobalState.ENTROPHY_VALUE = int.from_bytes(KeyGenerationController.mnemonicToEntropy(self.mnemonic_phrase.value), byteorder='big')
        
        print(self.mnemonic_phrase.value)
        print("privatekey: ",privateKey)
        print("Public key: ",publicKey)
        
        

        contractAddress=PublicContractController.getContractAddressByPublicAddress(publicKey, privateKey)
        if(contractAddress!="0x0000000000000000000000000000000000000000"):
            userName=NodeContractController.getUserName(publicKeyLocal=publicKey, privateKeyLocal=privateKey, nodeContractAddressLocal=contractAddress)
            GlobalState.USERNAME = userName
       
        if(contractAddress!="0x0000000000000000000000000000000000000000"):
            GlobalState.NODE_CONTRACT_ADDRESS = contractAddress
            

        GlobalState.PRIVATE_KEY = privateKey
        GlobalState.PUBLIC_KEY = publicKey
        
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

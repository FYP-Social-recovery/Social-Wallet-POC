from controller.nodeController import NodeContractController
from controller.publicContractController import PublicContractController
from controller.keyGenerationController import KeyGenerationController

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
    Row,
    MainAxisAlignment,
)

from state import GlobalState

import pyperclip

class RecoveredScreen(UserControl):
    def __init__(self, on_back_click, on_submit_click, page:Page):
        super().__init__()
        self.on_back_click = on_back_click
        self.on_submit_click = on_submit_click
        self.page = page
        
        secret = GlobalState.RECOVERED_ENTROPHY_VALUE
        self.mnemonic = KeyGenerationController.generateMnemonic(secret.to_bytes(16, byteorder='big'))
        privateKey,publicKey=KeyGenerationController.importWalletFromMnemonic(self.mnemonic)
        self.privateKey = privateKey
        self.publicKey = publicKey
        
    def on_submit_click_fn(self,e):
        GlobalState.RECOVERED_ENTROPHY_VALUE = ""
        self.on_submit_click
    
    def copyToClipboardMP(self, e):
        pyperclip.copy(self.mnemonic)
    def copyToClipboardSK(self, e):
        pyperclip.copy(self.privateKey)
    def copyToClipboardPK(self, e):
        pyperclip.copy(self.publicKey)
        
    def build(self):
        
        mnemonic_phrase = Text(value="Mnemonic Phrase : \n"+self.mnemonic, text_align="center", size=18, color="0xFF000000",tooltip="Mnemonic Phrase",)
        privateKey_text = Text(value="Private Key : \n"+self.privateKey, text_align="center", size=18, color="0xFF000000",tooltip="Wallet Private Key",)
        publicKey_text = Text(value="Public Key : \n"+self.publicKey, text_align="center", size=18, color="0xFF000000",tooltip="Wallet Public Key",)
        return Column(
                horizontal_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    IconButton(
                        icon=icons.ARROW_BACK_IOS_NEW_SHARP,
                        icon_color=colors.BLUE,
                        on_click=self.on_submit_click,
                        icon_size=20,
                        tooltip="Back",
                    ),
                    Text(value="Recovered Wallet", text_align="center", size=24, color="#2596be"), 
                    Container(
                        height=100,
                    ),
                    Row(
                        vertical_alignment= CrossAxisAlignment.END,
                        alignment = MainAxisAlignment.CENTER,
                        controls=[
                            mnemonic_phrase, 
                            IconButton(
                                icon=icons.COPY,
                                icon_color=colors.BLACK38,
                                on_click=self.copyToClipboardMP,
                                icon_size=20,
                                tooltip="Back",
                            ),
                        ],
                    ),
                    Container(
                        height=30,
                    ),
                    Row(
                        vertical_alignment= CrossAxisAlignment.END,
                        alignment = MainAxisAlignment.CENTER,
                        controls=[
                            privateKey_text, 
                            IconButton(
                                icon=icons.COPY,
                                icon_color=colors.BLACK38,
                                on_click=self.copyToClipboardSK,
                                icon_size=20,
                                tooltip="Back",
                            ),
                        ],
                    ),
                    Container(
                        height=30,
                    ),
                    Row(
                        vertical_alignment= CrossAxisAlignment.END,
                        alignment = MainAxisAlignment.CENTER,
                        controls=[
                            publicKey_text, 
                            IconButton(
                                icon=icons.COPY,
                                icon_color=colors.BLACK38,
                                on_click=self.copyToClipboardPK,
                                icon_size=20,
                                tooltip="Back",
                            ),
                        ],
                    ),
                    Container(
                        height=100,
                    ),
                    ElevatedButton("Close",bgcolor="#2596be", color="white",on_click=self.on_submit_click_fn , width=300,tooltip="Continue to Wallet",),  
                ],
            )

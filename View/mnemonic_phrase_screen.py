from controller.keyGenerationController import KeyGenerationController


from flet import (
    UserControl,
    Text,
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

class MnemonicPhraseScreen(UserControl):
    def __init__(self, on_back_click, on_continue_click):
        super().__init__()
        self.on_back_click = on_back_click
        self.on_continue_click = on_continue_click
        
        GlobalState.ENTROPHY_VALUE = ""
        GlobalState.PRIVATE_KEY = ""
        GlobalState.PUBLIC_KEY = ""
        GlobalState.USERNAME = ""
        GlobalState.NODE_CONTRACT_ADDRESS = ""
        
        mnemonic=KeyGenerationController.generateMnemonicForNewAccount()
        privateKey,publicKey=KeyGenerationController.importWalletFromMnemonic(mnemonic)
        print("privatekey: ",privateKey)
        print("Public key: ",publicKey)
        # distribution_controller=DistributionController()
        # distribution_controller.sendShares(email.value)
        self.mnemonic_phrase = mnemonic
        
        GlobalState.PRIVATE_KEY = privateKey
        GlobalState.PUBLIC_KEY = publicKey
        # GlobalState.ENTROPHY_VALUE = entrophyValue
        
    def continue_click(self,e):
        self.on_continue_click(self)
    
    
    def build(self):
        mnemonic_phrase = Text(value=self.mnemonic_phrase, text_align="center", size=18, color="0xFF000000",tooltip="Mnemonic Phrase",)
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
                    Text(value="Mnemonic Phase", text_align="center", size=24, color="#2596be"), 
                    Container(
                        height=100,
                    ),
                    mnemonic_phrase, 
                    Container(
                        height=100,
                    ),
                    ElevatedButton("Continue",bgcolor="#2596be", color="white",on_click=self.continue_click , width=300,tooltip="Continue to Wallet",),  
                ],
            )
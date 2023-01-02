# from Controller.distribution_controller import DistributionController

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

class MnemonicPhraseScreen(UserControl):
    def __init__(self, on_back_click, on_continue_click):
        super().__init__()
        self.on_back_click = on_back_click
        self.on_continue_click = on_continue_click
        
        # distribution_controller=DistributionController()
        # distribution_controller.sendShares(email.value)
        self.mnemonic_phrase = "mnemonic phrase"
        
    def continue_click(self,e):
        self.on_continue_click(self)
    
    
    def build(self):
        mnemonic_phrase = Text(value=self.mnemonic_phrase, text_align="center", size=18, color="0xFF000000")
        return Column(
                horizontal_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    IconButton(
                        icon=icons.ARROW_BACK_IOS_NEW_SHARP,
                        icon_color=colors.GREEN,
                        on_click=self.on_back_click,
                        icon_size=30,
                    ),
                    Text(value="Mnemonic Phase", text_align="center", size=24, color="0xFFA36D1D"), 
                    Container(
                        height=100,
                    ),
                    mnemonic_phrase, 
                    Container(
                        height=100,
                    ),
                    ElevatedButton("Continue",bgcolor="0xFFFFAB2E", color="0xFF986D34",on_click=self.continue_click , width=300),  
                ],
            )
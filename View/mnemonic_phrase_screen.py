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
    def __init__(self, on_back_click):
        super().__init__()
        self.on_back_click = on_back_click
        
    def build(self):
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
                    Text(value="cat dog pig parrot cat dog pig parrot cat dog pig parrot", text_align="center", size=18, color="0xFF000000"), 
                    Container(
                        height=100,
                    ),
                    ElevatedButton("Continue",bgcolor="0xFFFFAB2E", color="0xFF986D34", width=300),  
                ],
            )
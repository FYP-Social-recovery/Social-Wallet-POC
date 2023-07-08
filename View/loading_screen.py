from flet import (
    UserControl,
    Text,
    TextField,
    Column,
    Row,
    ElevatedButton,
    colors,
    AppBar,
    IconButton,
    icons,
    CrossAxisAlignment,
    Container,
    MainAxisAlignment,
    Page,
)

from state import GlobalState

import pyperclip

from web3 import Web3

class LoadingScreen(UserControl):
    def __init__(self, on_back_click):
        super().__init__()
        self.on_back_click = on_back_click
        
        # on_back_click

    def build(self):
        return Column(
            horizontal_alignment=CrossAxisAlignment.CENTER,
            controls=[
                IconButton(
                    icon=icons.ARROW_BACK_IOS_NEW_SHARP,
                    icon_color=colors.BLUE,
                    on_click=self.on_back_click,
                    icon_size=20,
                ),
                Text(value="Loading...", text_align="center",
                        size=20, color="Black"),
            ],
        )

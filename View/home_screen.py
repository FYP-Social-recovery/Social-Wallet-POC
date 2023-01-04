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

class HomeScreen(UserControl):
    def __init__(self, on_back_click):
        super().__init__()
        self.on_back_click = on_back_click
        
        print(state.PRIVATE_KEY)
        print(state.PUBLIC_KEY)

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
                Text(value="Phoenix Wallet", text_align="center",
                     size=36, color="0xFFA36D1D"),
                Container(
                    height=100,
                ),
                Text(value="5.345267 ETH", text_align="center",
                     size=24, color="Black"),
                Text(value="Geroli Network", text_align="center",
                     size=20, color="0xFFA36D1D"),
                Container(
                    height=100,
                ),
                ElevatedButton("Social Recovery Menu", bgcolor="0xFFFFAB2E",
                               color="0xFF986D34", width=300),
            ],
        )

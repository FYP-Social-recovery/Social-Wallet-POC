from flet import (
    UserControl,
    Tabs,
    Tab,
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


class ShareholderStatusScreen(UserControl):
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
                Text(value="Shareholder Status", text_align="center",
                     size=24, color="0xFFA36D1D"),
                Container(
                    height=20,
                ),
                TextField(label="Share Holder 1",
                          hint_text="Please enter an address", color="0xFF000000", width=600),
                Container(
                    height=10,
                ),
                TextField(label="Share Holder 2",
                          hint_text="Please enter an address", color="0xFF000000", width=600),
                Container(
                    height=10,
                ),
                TextField(label="Share Holder 3",
                          hint_text="Please enter an address", color="0xFF000000", width=600),
                Container(
                    height=10,
                ),
                TextField(label="Share Holder 4",
                          hint_text="Please enter an address", color="0xFF000000", width=600),
                Container(
                    height=10,
                ),
                TextField(label="Share Holder 5",
                          hint_text="Please enter an address", color="0xFF000000", width=600),
                Container(
                    height=10,
                ),
                ElevatedButton("Request", bgcolor="0xFFFFAB2E",
                               color="0xFF986D34", width=300),
            ],
        )

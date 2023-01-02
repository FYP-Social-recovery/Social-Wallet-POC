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


class DistributesharesScreen(UserControl):
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
                Text(value="Distribute Shares", text_align="center",
                     size=24, color="0xFFA36D1D"),
                Container(
                    height=20,
                ),
                TextField(label="Select a Fingerprint",
                          hint_text="Please select a fingerprint", color="0xFF000000", width=600),
                Container(
                    height=10,
                ),
                TextField(label="Email Address",
                          hint_text="Please enter a valid email address", color="0xFF000000", width=600),
                Container(
                    height=10,
                ),
                
                ElevatedButton("Distribute", bgcolor="0xFFFFAB2E",
                               color="0xFF986D34", width=300),
            ],
        )

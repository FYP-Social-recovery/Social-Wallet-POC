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
                    icon_color=colors.BLUE,
                    on_click=self.on_back_click,
                    icon_size=20,
                    tooltip="Back",
                ),
                Text(value="Distribute Shares", text_align="center",
                     size=24, color="#2596be"),
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
                
                ElevatedButton("Distribute", bgcolor="#2596be",
                               color="white", width=300),
            ],
        )

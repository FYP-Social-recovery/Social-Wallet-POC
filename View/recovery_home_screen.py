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


class RecoveryHomeScreen(UserControl):
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
                Text(value="Social Recovery Menu", text_align="center",
                     size=24, color="0xFFA36D1D"),
                Container(
                    height=20,
                ),
                ElevatedButton(text="Add Shareholders"),
                Container(
                    height=10,
                ),
                ElevatedButton(text="Shareholder Status"),
                Container(
                    height=10,
                ),
                ElevatedButton(text="Distribute Shares"),
                Container(
                    height=10,
                ),
                ElevatedButton("Submit", bgcolor="0xFFFFAB2E",
                               color="0xFF986D34", width=300),
            ],
        )

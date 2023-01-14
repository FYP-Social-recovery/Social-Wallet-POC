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

import state

class RecoveryHomeScreen(UserControl):
    def __init__(self, on_back_click, on_add_shareholders_click, on_shareholders_status_click, on_distribute_shares_click, on_registration_click):
        super().__init__()
        self.on_back_click = on_back_click
        self.on_add_shareholders_click = on_add_shareholders_click
        self.on_shareholders_status_click = on_shareholders_status_click
        self.on_distribute_shares_click = on_distribute_shares_click
        self.on_registration_click = on_registration_click
        
        # TODO
        # method(NODE_CONTRACT_ADDRESS) -> return state
        
        print("Contract address is : ", state.NODE_CONTRACT_ADDRESS)
        print("Contract address is : ", state.USERNAME)

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
                ElevatedButton(text="registration", on_click=self.on_registration_click),
                Container(
                    height=10,
                ),
                ElevatedButton(text="Add Shareholders", on_click=self.on_add_shareholders_click),
                Container(
                    height=10,
                ),
                ElevatedButton(text="Shareholder Status", on_click=self.on_shareholders_status_click),
                Container(
                    height=10,
                ),
                ElevatedButton(text="Distribute Shares", on_click=self.on_distribute_shares_click),
                # Container(
                #     height=10,
                # ),
                # ElevatedButton("Submit", bgcolor="0xFFFFAB2E",
                #                color="0xFF986D34", width=300),
            ],
        )

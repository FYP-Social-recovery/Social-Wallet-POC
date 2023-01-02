from flet import (
    UserControl,
    Text,
    Column,
    ElevatedButton,
    AppBar,
    colors,
    CrossAxisAlignment,
    Container,
)

class OnboardingScreen(UserControl):
    def __init__(self, on_new_wallet_click, on_import_wallet_click):
        super().__init__()
        self.on_new_wallet_click = on_new_wallet_click
        self.on_import_wallet_click = on_import_wallet_click
        
    def build(self):
        return Column(
            horizontal_alignment=CrossAxisAlignment.CENTER,
            controls=[
                Text(value="Phoenix\nWallet", text_align="center", size=36, color="0xFFA36D1D"), 
                Container(
                    height=100,
                ),
                ElevatedButton("New Wallet",bgcolor="0xFFFFAB2E", color="0xFF986D34", width=300, on_click=self.on_new_wallet_click), 
                ElevatedButton("Import Wallet",bgcolor="0xFFFFAB2E", color="0xFF986D34", width=300, on_click=self.on_import_wallet_click),
            ],
        )
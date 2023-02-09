from flet import (
    UserControl,
    Text,
    Column,
    ElevatedButton,
    OutlinedButton,
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
                Text(value="Phoenix\nWallet", text_align="center", size=36,font_family="RobotoSlab", color="#2596be"), 
                Container(
                    height=100,
                ),
                ElevatedButton("New Wallet",width=300,bgcolor="#2596be",color="white" ,on_click=self.on_new_wallet_click,tooltip="Create a new wallet"),
                OutlinedButton("Import Wallet", width=300, on_click=self.on_import_wallet_click,tooltip="Import an existing wallet"),
            ],
        )
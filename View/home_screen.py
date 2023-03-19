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
    Divider,
)

from state import GlobalState

import pyperclip

from web3 import Web3

class HomeScreen(UserControl):
    def __init__(self, on_back_click, on_click_reload, on_menue_button_click):
        super().__init__()
        self.on_back_click = on_back_click
        self.on_click_reload = on_click_reload
        self.on_menue_button_click = on_menue_button_click
        
        print(GlobalState.PRIVATE_KEY)
        print(GlobalState.PUBLIC_KEY)
        print(GlobalState.NODE_CONTRACT_ADDRESS)
        
        self.public_key = GlobalState.PUBLIC_KEY
        
        web3_instance = Web3(Web3.HTTPProvider(GlobalState.RPC_URL))
        print("Is web3 connected : " + str(web3_instance.isConnected()))
        
        wallet_address = GlobalState.PUBLIC_KEY
        
        balance = web3_instance.eth.getBalance(wallet_address)
        balance_from_wei = web3_instance.fromWei(balance,"ether")
        self.balance = str(balance_from_wei)
        
        if(GlobalState.NODE_CONTRACT_ADDRESS!=""):
            if(GlobalState.USERNAME!=""):
                self.username = GlobalState.USERNAME
            else:
                self.username = GlobalState.NODE_CONTRACT_ADDRESS[0:5] + "..." + GlobalState.NODE_CONTRACT_ADDRESS[-4:-1]
        else:
            self.username = "Not Registered"
        
    def copyToClipboard(self, e):
        pyperclip.copy(GlobalState.PUBLIC_KEY)
        
    def updateBalance(self, e):
        web3_instance = Web3(Web3.HTTPProvider(GlobalState.RPC_URL))
        print(web3_instance.isConnected())
        
        wallet_address = GlobalState.PUBLIC_KEY # "0x1c36c98DC9b260564F17817241fED3BBA1402059"
        
        balance = web3_instance.eth.getBalance(wallet_address)
        balance_from_wei = web3_instance.fromWei(balance,"ether")
        self.balance = str(balance_from_wei)
        print(self.balance)
        self.page.update()

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
                Row(
                    vertical_alignment= CrossAxisAlignment.CENTER,
                    alignment = MainAxisAlignment.CENTER,
                    controls=[
                        IconButton(
                            icon=icons.PERSON,
                            icon_color=colors.BLACK38,
                            icon_size=20,
                        ),
                        Text(value=self.username, text_align="center",
                                size=20, color="Black"),
                    ],
                ),
                Text(value="Phoenix Wallet", text_align="center", size=36, color="#2596be"),
                Container(
                    height=50,
                ),
                Text(value="Public Key", text_align="center",
                     size=15, color="Black"),
                
                Row(
                    
                    vertical_alignment= CrossAxisAlignment.CENTER,
                    alignment = MainAxisAlignment.CENTER,
                    controls=[
                        Text(value=self.public_key[0:5] + "..." + self.public_key[-4:], text_align="center",
                                size=20, color="Black",tooltip="Public Key"),
                        IconButton(
                            icon=icons.COPY,
                            icon_color=colors.BLACK38,
                            on_click=self.copyToClipboard,
                            icon_size=20,
                            tooltip="Back",
                        ),
                    ],
                ),
                Container(
                    height=100,
                ),
                Text(value="Balance", text_align="center",
                     size=15, color="Black"),
                
                Row(
                    
                    vertical_alignment= CrossAxisAlignment.CENTER,
                    alignment = MainAxisAlignment.CENTER,
                    controls=[
                        Text(value=self.balance + " " + GlobalState.NETWORK_CURRENCY_SYMBOL, text_align="center",
                                size=24, color="Black",tooltip="Balance"),
                        IconButton(
                            icon=icons.REFRESH_ROUNDED,
                            icon_color=colors.BLACK38,
                            on_click=self.updateBalance,
                            icon_size=20,
                        ),
                    ],
                ),
                Text(value=GlobalState.NETWORK_TYPE, text_align="center",
                     size=20, color="#2596be",tooltip="Blockchain Network"),
                Container(
                    height=100,
                ),
                ElevatedButton("Setup Menu", bgcolor="#2596be",
                               color="white",on_click=self.on_menue_button_click, width=300,tooltip="Configuration Menu"),
            ],
        )

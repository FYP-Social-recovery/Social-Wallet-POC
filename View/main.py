import flet
from flet import (
    Page,
    Text,
    View,
    AppBar,
    ElevatedButton,
    colors,
    MainAxisAlignment,
    CrossAxisAlignment,
    IconButton,
    icons,
)

from onboarding_screen import OnboardingScreen
from mnemonic_phrase_screen import MnemonicPhraseScreen
from registration_screen import RegistrationScreen
from home_screen import HomeScreen
from wallet_import_screen import WalletImportScreen
from loading_screen import LoadingScreen
from recovery_home_screen import RecoveryHomeScreen
from add_shareholder_screen import AddShareholderScreen
from shareholder_status_screen import ShareholderStatusScreen
from distributeshares_screen import DistributesharesScreen

import state

def main(page: Page):
    state.init()
    
    page.title = "Phoenix Wallet"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.bgcolor = "0xFFFFF9F2"

    # # Navigate to Onboarding Screen
    # app = OnboardingScreen()

    # page.add(app)
    
    # OnboardingScreen "New Wallet" button click action
    def on_new_wallet_click(self):
        self.page.go("/mnemonic_phrase")
    
    # OnboardingScreen "Import Wallet" button click action
    def on_import_wallet_click(self):
        self.page.go("/wallet_import")
    
    # MnemonicPhraseScreen "Continue" button click action
    def on_mnemonic_continue_click(self):
        self.page.go("/home")
    
    # WalletImportScreen "Continue" button click action
    def on_import_continue_click(self):
        self.page.go("/home")
       
    # RegistrationScreen "Submit" button click action 
    def on_submit_click(self):
        self.page.go("/home")
        
    def on_click_reload(self):
        # self.page.go("/home/loading")
        self.page.go("/home")
    
    # HomeScreen "Social Recovery Menu" button click action 
    def on_menue_button_click(self):
        self.page.go("/recovery/home")
    
    # RecoveryHomeScreen "Registration" button click action 
    def on_registration_click(self):
        self.page.go("/recovery/home/registration")
        
    # RecoveryHomeScreen "Add Shareholders" button click action 
    def on_add_shareholders_click(self):
        self.page.go("/recovery/home/addShareholders")
    
    # RecoveryHomeScreen "Shareholder Status" button click action 
    def on_shareholders_status_click(self):
        self.page.go("/recovery/home/shareholderStatus")
    
    # RecoveryHomeScreen "Distribute Shares" button click action 
    def on_distribute_shares_click(self):
        self.page.go("/recovery/home/distributeShares")

    def route_change(route):
        page.views.clear()
        page.views.append(
            View(
                "/",
                [
                    OnboardingScreen(on_new_wallet_click=on_new_wallet_click, on_import_wallet_click=on_import_wallet_click),
                ],
                bgcolor="0xFFFFF9F2",
                vertical_alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER,
            )
        )
        if page.route == "/mnemonic_phrase":
            page.views.append(
                View(
                    "/mnemonic_phrase",
                    [
                        MnemonicPhraseScreen(on_back_click=lambda _: page.go("/"), on_continue_click=on_mnemonic_continue_click),
                    ],
                    bgcolor="0xFFFFF9F2",
                    vertical_alignment=MainAxisAlignment.CENTER,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                )
            )
        if page.route == "/wallet_import":
            page.views.append(
                View(
                    "/wallet_import",
                    [
                        WalletImportScreen(on_back_click=lambda _: page.go("/"), on_continue_click=on_import_continue_click),
                    ],
                    bgcolor="0xFFFFF9F2",
                    vertical_alignment=MainAxisAlignment.CENTER,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                )
            )
        if page.route == "/home":
            page.views.append(
                View(
                    "/home",
                    [
                        HomeScreen(on_back_click=lambda _: page.go("/"), on_click_reload=on_click_reload, on_menue_button_click=on_menue_button_click),
                    ],
                    bgcolor="0xFFFFF9F2",
                    vertical_alignment=MainAxisAlignment.CENTER,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                )
            )
        if page.route == "/home/loading":
            page.views.append(
                View(
                    "/home/loading",
                    [
                        LoadingScreen(on_back_click=lambda _: page.go("/"))
                    ],
                    bgcolor="0xFFFFF9F2",
                    vertical_alignment=MainAxisAlignment.CENTER,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                )
            )
        if page.route == "/recovery/home":
            page.views.append(
                View(
                    "/recovery/home",
                    [
                        RecoveryHomeScreen(on_back_click=lambda _: page.go("/home"), on_registration_click=on_registration_click, on_add_shareholders_click=on_add_shareholders_click, on_shareholders_status_click=on_shareholders_status_click, on_distribute_shares_click=on_distribute_shares_click)
                    ],
                    bgcolor="0xFFFFF9F2",
                    vertical_alignment=MainAxisAlignment.CENTER,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                )
            )
        if page.route == "/recovery/home/registration":
            page.views.append(
                View(
                    "/recovery/home/registration",
                    [
                        RegistrationScreen(on_back_click=lambda _: page.go("/recovery/home"), on_submit_click=on_submit_click),
                    ],
                    bgcolor="0xFFFFF9F2",
                    vertical_alignment=MainAxisAlignment.CENTER,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                )
            )
        if page.route == "/recovery/home/addShareholders":
            page.views.append(
                View(
                    "/recovery/home/addShareholders",
                    [
                        AddShareholderScreen(on_back_click=lambda _: page.go("/recovery/home"))
                    ],
                    bgcolor="0xFFFFF9F2",
                    vertical_alignment=MainAxisAlignment.CENTER,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                )
            )
        if page.route == "/recovery/home/shareholderStatus":
            page.views.append(
                View(
                    "/recovery/home/shareholderStatus",
                    [
                        ShareholderStatusScreen(on_back_click=lambda _: page.go("/recovery/home"),)
                    ],
                    bgcolor="0xFFFFF9F2",
                    vertical_alignment=MainAxisAlignment.CENTER,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                )
            )
        if page.route == "/recovery/home/distributeShares":
            page.views.append(
                View(
                    "/recovery/home/distributeShares",
                    [
                        DistributesharesScreen(on_back_click=lambda _: page.go("/recovery/home"))
                    ],
                    bgcolor="0xFFFFF9F2",
                    vertical_alignment=MainAxisAlignment.CENTER,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                )
            )
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


flet.app(target=main, view=flet.FLET_APP)
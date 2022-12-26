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
)

from onboarding_screen import OnboardingScreen
from mnemonic_phrase_screen import MnemonicPhraseScreen

def main(page: Page):
    page.title = "Phoenix Wallet"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.bgcolor = "0xFFFFF9F2"

    # # Navigate to Onboarding Screen
    # app = OnboardingScreen()

    # page.add(app)
    
    def route_change(route):
        page.views.clear()
        page.views.append(
            View(
                "/",
                [
                    OnboardingScreen(on_new_wallet_click=lambda _: page.go("/mnemonic_phrase")),
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
                        MnemonicPhraseScreen(on_back_click=lambda _: page.go("/")),
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
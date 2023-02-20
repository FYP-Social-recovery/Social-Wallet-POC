from controller.nodeController import NodeContractController

from flet import (
    UserControl,
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
    BorderRadius,
    MainAxisAlignment,
    Row
)

import state

class ShareHolderScreen(UserControl):
    def __init__(self, on_back_click, on_continue_click):
        super().__init__()
        self.on_back_click = on_back_click
        self.on_continue_click = on_continue_click

        
        ShareOwnerAdresses=NodeContractController.checkRequestsForBeAHolder()
        print(ShareOwnerAdresses)
        
        self.TextArray=[]
        for i in range(3):
            if (i<=ShareOwnerAdresses.length()):
                textRow=Row(
                            vertical_alignment= CrossAxisAlignment.CENTER,
                            alignment = MainAxisAlignment.CENTER,
                            controls=[
                                    Text(value=ShareOwnerAdresses[i], text_align="center", size=24, color="0xFF000000"),
                                    ElevatedButton(text="Accepet", bgcolor="0xFFD9BE38", color="0xFFFFFFFF", elevation=0,on_click=self.accept(ShareOwnerAdresses[i])),
                                    ElevatedButton(text="Reject", bgcolor="0xFFA62E2E", color="0xFFFFFFFF", elevation=0,on_click=self.reject(ShareOwnerAdresses[i])),
                                ],
                        )
            else:
                textRow=Row(
                            vertical_alignment= CrossAxisAlignment.CENTER,
                            alignment = MainAxisAlignment.CENTER,
                            controls=[
                                    Text(value="", text_align="center", size=24, color="0xFF000000"),
                                ],
                        )
            self.TextArray.append(textRow)

    def accept(self,e,ownerAddress):
        NodeContractController.acceptInvitation(ownerAddress)

    def reject(self,e,ownerAddress):
        NodeContractController.rejectInvitation(ownerAddress)

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
                Text(value="Share Holding Requests", text_align="center",
                     size=24, color="#2596be"),
                Container(
                    height=20,
                ),
                self.TextArray[0],
                Container(
                    height=10,
                ),
                self.TextArray[1],
                Container(
                    height=10,
                ),
                self.TextArray[2],
                Container(
                    height=10,
                ),
            ],
        )
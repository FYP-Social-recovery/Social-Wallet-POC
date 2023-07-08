from controller.nodeController import NodeContractController
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
    Row,
    MainAxisAlignment,
)

from state import GlobalState

class ShareholderStatusScreen(UserControl):
    def __init__(self, on_back_click):
        super().__init__()
        self.on_back_click = on_back_click
        
        PENDING = "Pending"
        ACCEPTED = "Accepted"
        REJECTED = "Rejected"
        
        self.shareholders = []
        self.status = []
        
        shareHolderStatus=NodeContractController.getHolderStatus(GlobalState.PUBLIC_KEY, GlobalState.PRIVATE_KEY, GlobalState.NODE_CONTRACT_ADDRESS)
        print(shareHolderStatus)
        for shareholder in shareHolderStatus:
            self.shareholders.append(shareholder[0])
            self.status.append(shareholder[1])
        # Load shareholder list for the user
        # getShareholders(pubkey,privkey) -> [["0xa","Pending"],]
        # self.shareholders = ["0x1", "0x2", "0x3", "0x4", "0x5"]
        # Get status of each shareholder and display
        # self.status = [PENDING, ACCEPTED, REJECTED, PENDING, REJECTED]
        
        self.TextArray=[]
        for i in range(3):
            if(self.status[i]==PENDING):
                color = "0xFFD9BE38"
            elif(self.status[i]==ACCEPTED):
                color = "0xFF33A64C"
            elif(self.status[i]==REJECTED):
                color = "0xFFA62E2E"

            textRow=Row(
                        vertical_alignment= CrossAxisAlignment.CENTER,
                        alignment = MainAxisAlignment.CENTER,
                        controls=[
                                Text(value=self.shareholders[i], text_align="center", size=24, color="0xFF000000"),
                                ElevatedButton(text=self.status[i], bgcolor=color, color="0xFFFFFFFF", elevation=0,),
                            ],
                    )

            self.TextArray.append(textRow)

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
                Text(value="Shareholder Status", text_align="center", size=24, color="#2596be"),
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
                # Container(
                #     height=10,
                # ),
                # self.TextArray[3],
                # Container(
                #     height=10,
                # ),
                # self.TextArray[4],
                # Container(
                #     height=10,
                # ),
                # ElevatedButton("Request", bgcolor="#2596be",
                #                color="white", width=300,),
                
            ],
        )

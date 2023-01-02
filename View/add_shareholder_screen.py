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
from controller.nodeController import NodeController


class AddShareholderScreen(UserControl):
    def __init__(self, on_back_click):
        super().__init__()
        self.on_back_click = on_back_click

    def request_click(self, e):
        nodeController=NodeController()
        for i in range(5):
            nodeController.addTemporaryShareHolder(self.__class__.TextFieldArray[i].value)
        #self.on_request_click(self)

    TextFieldArray=[]
    for i in range(5):
        textFiled=TextField(label="Share Holder "+str(i+1),
                  hint_text="Please enter an address", color="0xFF000000", width=600)
        TextFieldArray.append(textFiled)

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
                Text(value="Add Shareholders", text_align="center",
                     size=24, color="0xFFA36D1D"),
                Container(
                    height=20,
                ),
                self.__class__.TextFieldArray[0],
                Container(
                    height=10,
                ),
                self.__class__.TextFieldArray[1],
                Container(
                    height=10,
                ),
                self.__class__.TextFieldArray[2],
                Container(
                    height=10,
                ),
                self.__class__.TextFieldArray[3],
                Container(
                    height=10,
                ),
                self.__class__.TextFieldArray[4],
                Container(
                    height=10,
                ),
                ElevatedButton("Request", bgcolor="0xFFFFAB2E",
                               color="0xFF986D34", width=300, on_click=self.request_click),
            ],
        )

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
    FilePicker,
    FilePickerResultEvent,
    AlertDialog,
    TextAlign,
)

class RecoveryScreen(UserControl):
    def __init__(self, on_back_click, on_submit_click, page):
        super().__init__()
        self.on_back_click = on_back_click
        self.on_submit_click = on_submit_click
        self.page = page
        
        self.txt = ""
        
        def on_dialog_result(e: FilePickerResultEvent):
            print("Selected files:", e.files[0].path)
            print("Selected file or directory:", e.path)
            if(len(e.files) != 0):
                self.biometric.value = e.files[0].path
                self.txt = e.files[0].path
                self.page.update()
        
        self.file_picker = FilePicker(on_result=on_dialog_result)
        self.page.overlay.append(self.file_picker)
        self.page.update()
    def on_submit_click_fn(self,e):
        print(self.biometric.value)
    def build(self):
        self.biometric= TextField(label="Select a Fingerprint",
                          hint_text="Please select a fingerprint", color="0xFF000000", width=600)
                        
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
                Text(value="Key Recovery Menu", text_align="center",
                     size=24, color="#2596be"),
                Container(
                    height=20,
                ),
                ElevatedButton("Choose finger print image...",
                    on_click=lambda _: self.file_picker.pick_files(allow_multiple=False)),
                # self.biometric,
                Container(
                    height=10,
                ),
                
                ElevatedButton("Recover", bgcolor="#2596be",
                               color="white",on_click=self.on_submit_click_fn, width=300,tooltip="Recover the private key"),
            ],
        )
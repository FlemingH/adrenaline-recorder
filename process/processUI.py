from uiControl import FormControl

# to check if app open and focus
def startUIProcess(if_window_open_focus):
    while True:

        formControl = FormControl()
        formControl.bindActiveWindow()
        formControl.bindWindowByName(win_name = "AMD Software: Adrenalin Edition")

        isWinVisible = formControl.isWinVisible()
        getForegroundWindow = formControl.getForegroundWindow()

        if isWinVisible and getForegroundWindow:
            if_window_open_focus.value = 1
        else:
            if_window_open_focus.value = 0
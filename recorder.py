import psutil
from pywinauto.application import Application
from win32gui import FindWindow, GetWindowRect
from uiControl import FormControl

def getRadeonSoftwareWindow():

    # get pid
    pl = psutil.pids()
    radeonPid = 0
    for pid in pl:
        if psutil.Process(pid).name() == "RadeonSoftware.exe":
            radeonPid = pid
            break        

    app = Application().connect(process=radeonPid)
    window = app.window()

    # wait window open
    window.wait("visible", timeout=60)
    return window

window = getRadeonSoftwareWindow()

formControl = FormControl()
formControl.bindWindowByName(win_name = "AMD Software: Adrenalin Edition")
rect = formControl.getWinRect()
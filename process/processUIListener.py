import psutil
from pywinauto.application import Application

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
    print("finding window")
    window.wait("visible", timeout=60)
    return window
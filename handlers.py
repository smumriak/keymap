include("windowClasses.py")
include("utilities.py")

def handleWindowCloseRequest():
    id = getCurrentWindowID()
    if id is not None:
        closeWindow(id)
    return None

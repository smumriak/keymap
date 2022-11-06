from Xlib import X
from Xlib.display import Display
from Xlib.error import XError
from Xlib.xobject.drawable import Window
from Xlib.protocol.rq import Event  

import subprocess

display = Display()
rootWindow = display.screen().root

NET_ACTIVE_WINDOW = display.intern_atom('_NET_ACTIVE_WINDOW')

def getCurrentWindowID():
    response = rootWindow.get_full_property(NET_ACTIVE_WINDOW, X.AnyPropertyType)

    if not response:
        return None

    result =  response.value[0]

    if result == rootWindow.id:
        return None

    return result

def runWMCtrl(args):
    try:
        with subprocess.Popen(["wmctrl"] + args, stdout=subprocess.PIPE) as p:
            output = p.communicate()[0].decode()[:-1]  # Drop trailing newline
            returncode = p.returncode
    except FileNotFoundError:
        return 1, 'wmctrl not found'

def closeWindow(id):
    return runWMCtrl(["-c", f"{id}", "-i"])

    return returncode, output

def makeWindowsRegex(windows, inverse: bool = False):
    partialResult = "|".join(str('^'+x+'$') for x in  windows)
    if inverse == True:
        partialResult = f"(?i)^(?!({partialResult})).*$"
    else:
        partialResult = f"(?i)({partialResult})"
    print(partialResult)
    return re.compile(partialResult)  

def defineKeymap(name, windows, keymapDictionary):
    regex = makeWindowsRegex(windows, False)
    return keymap(name, keymapDictionary, when = lambda context: regex.fullmatch(context.wm_class))

def defineKeymapInverse(name, windows, keymapDictionary):
    regex = makeWindowsRegex(windows, True)
    return keymap(name, keymapDictionary, when = lambda context: regex.fullmatch(context.wm_class))
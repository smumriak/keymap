ignoredWindows = frozenset(
    [
        "codium",
        "vscodium",
        "vscode",
        "dota",
        "qemu",
        "realvnc-vncviewer",
        "VNC Viewer",
    ]
)

def isIgnored(windowClass: str) -> bool:
    return windowClass.casefold() in ignoredWindows

terminals = frozenset(
    [
        "alacritty",
        "cutefish-terminal",
        "deepin-terminal",
        "eterm",
        "gnome-terminal",
        "gnome-terminal-server",
        "guake",
        "hyper",
        "io.elementary.terminal",
        "kinto-gui.py",
        "kitty",
        "kgx",
        "konsole",
        "lxterminal",
        "mate-terminal",
        "org.gnome.console",
        "qterminal",
        "st",
        "sakura",
        "station",
        "tabby",
        "terminator",
        "termite",
        "tilda",
        "tilix",
        "urxvt",
        "xfce4-terminal",
        "xterm",
    ]
)

def isTerminal(windowClass: str) -> bool:
    return windowClass.casefold() in terminals

tabbedTerminals = frozenset(
    [
        "gnome-terminal",
    ]
)

def isTabbedTerminal(windowClass: str) -> bool:
    return windowClass.casefold() in tabbedTerminals

vscode = frozenset(["code", "vscodium", "codium"])

def isVSCode(windowClass: str) -> bool:
    return windowClass.casefold() in vscode

sublime = frozenset(["sublime_text", "subl"])

def isSublime(windowClass: str) -> bool:
    return windowClass.casefold() in sublime

remotes = frozenset(
    [
        "gnome-boxes",
        "org.remmina.remmina",
        "remmina",
        "qemu",
        "spicy",
        "virt-manager",
        "virtualbox",
        "virtualbox machine",
        "xfreerdp",
        "wfica",
        "realvnc-vncviewer",
    ]
)

def isRemote(windowClass: str) -> bool:
    return windowClass.casefold() in remotes

chrome = frozenset(
    [
        "chromium",
        "chromium-browser",
        "google-chrome",
        "microsoft-edge",
        "microsoft-edge-dev",
        "org.deepin.browser",
    ]
)

firefox = frozenset(
    [
        "firefox",
        "firefox",
        "firefox-beta",
        "firefox developer edition",
        "navigator",
        "firefoxdeveloperedition",
        "waterfox",
    ]
)

browsers = frozenset(
    [
        "discord",
        "epiphany",
        "brave-browser",
    ]
) \
    | chrome \
    | firefox \


def isBrowser(windowClass: str) -> bool:
    return windowClass.casefold() in browsers

filemanagers = frozenset(
    [
        "caja",
        "cutefish-filemanager",
        "dde-file-manager",
        "dolphin",
        "io.elementary.files",
        "nautilus",
        "nemo",
        "org.gnome.nautilus",
        "pcmanfm",
        "pcmanfm-qt",
        "spacefm",
        "thunar",
    ]
)

def isFileManager(windowClass: str) -> bool:
    return windowClass.casefold() in filemanagers

closeableWindows = frozenset(
    [
        "bitwarden",
        "signal",
        "Viber",
        "vlc",
        "bluebubbles-desktop-app",
        "gnome-tweaks",
        "autokey-gtk",
    ]
)

def isCloseable(windowClass: str) -> bool:
    return windowClass.casefold() in closeableWindows

tabbedWindows = frozenset(
    [
        
    ]
) \
    | browsers \
    | sublime \
    | filemanagers \
    | tabbedTerminals \


def isTabbed(windowClass: str) -> bool:
    return windowClass.casefold() in tabbedWindows

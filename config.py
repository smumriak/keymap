# this stuff is using greedy algorithm to resolve conditions!
# i.e. first rule defined will be executed. think as "override comes before declaration"

timeouts(
    multipurpose = 0,
    suspend = 0,
)

include("windowClasses.py")
include("utilities.py")
include("handlers.py")

multipurpose_modmap("multipurpose modmap",
    {
    }
)

modmap("Global Modmap",
    {
        # no gnome activities
        Key.RIGHT_META: Key.LEFT_META,

        # remapped in firmware :D (except Fn)
        # Key.LEFT_ALT:   Key.LEFT_META,  # Left Alt is Left Command (Meta/Cmd in Linux)
        # Key.LEFT_META:  Key.LEFT_ALT,   # Left Meta is Left Option (Alt in linux)
        # Key.LEFT_CTRL:  Key.LEFT_CTRL,  # Left Control is Left Control
        # Key.RIGHT_ALT:  Key.RIGHT_META, # Right Alt is Right Command (Meta/Cmd in Linux)
        # Key.RIGHT_META: Key.RIGHT_CTRL, # Right Control is Right Control
        # Key.RIGHT_CTRL: Key.RIGHT_ALT,  # Right Meta is Right Option (Alt in linux)
        # Key.KEY_FN: Key.LEFT_CTRL,
    }
)

defineKeymap("Nautilus", ["org.gnome.nautilus", "nautilus"], 
    {
        # needs revision, does key combinations have changed some time ago
        # K("Backspace"): K("Alt-Left"), # go up
    }
)

defineKeymap("Firefox", firefox, 
    {
    }
)

defineKeymap("Chrome", chrome, 
    {
        K("Cmd-q"): handleWindowCloseRequest, # chrome stupid
    }
)

defineKeymap("Ulauncher", ["ulauncher"], 
    {
        K("Cmd-Key_0"): K("Alt-Key_0"),
        K("Cmd-Key_1"): K("Alt-Key_1"),
        K("Cmd-Key_2"): K("Alt-Key_2"),
        K("Cmd-Key_3"): K("Alt-Key_3"),
        K("Cmd-Key_4"): K("Alt-Key_4"),
        K("Cmd-Key_5"): K("Alt-Key_5"),
        K("Cmd-Key_6"): K("Alt-Key_6"),
        K("Cmd-Key_7"): K("Alt-Key_7"),
        K("Cmd-Key_8"): K("Alt-Key_8"),
        K("Cmd-Key_9"): K("Alt-Key_9"),
    }
)

defineKeymap("Terminals", terminals, 
    {
        K("Cmd-A"): K("Ctrl-Shift-A"),
        K("Cmd-B"): K("Ctrl-Shift-B"),
        K("Cmd-C"): K("Ctrl-Shift-C"),
        K("Cmd-D"): K("Ctrl-Shift-D"),
        K("Cmd-E"): K("Ctrl-Shift-E"),
        K("Cmd-F"): K("Ctrl-Shift-F"),
        K("Cmd-G"): K("Ctrl-Shift-G"),
        # K("Cmd-H"): K("Ctrl-Shift-H"),
        K("Cmd-I"): K("Ctrl-Shift-I"),
        K("Cmd-J"): K("Ctrl-Shift-J"),
        K("Cmd-K"): K("Ctrl-Shift-K"),
        K("Cmd-L"): K("Ctrl-Shift-L"),
        # K("Cmd-M"): K("Ctrl-Shift-M"),
        K("Cmd-N"): K("Ctrl-Shift-N"),
        K("Cmd-O"): K("Ctrl-Shift-O"),
        K("Cmd-P"): K("Ctrl-Shift-P"),
        K("Cmd-Q"): K("Ctrl-Shift-Q"),
        K("Cmd-R"): K("Ctrl-Shift-R"),
        K("Cmd-S"): K("Ctrl-Shift-S"),
        K("Cmd-T"): K("Ctrl-Shift-T"),
        K("Cmd-U"): K("Ctrl-Shift-U"),
        K("Cmd-V"): K("Ctrl-Shift-V"),
        K("Cmd-W"): K("Ctrl-Shift-W"),
        K("Cmd-X"): K("Ctrl-Shift-X"),
        K("Cmd-Z"): K("Ctrl-Shift-Z"),

        K("Cmd-Shift-Equal"): K("Ctrl-Shift-Equal"),
        K("Cmd-Shift-Minus"): K("Ctrl-Shift-Minus"),
        K("Cmd-Shift-Key_0"): K("Ctrl-Shift-Key_0"),
        K("Cmd-Shift-Key_1"): K("Ctrl-Shift-Key_1"),
        K("Cmd-Shift-Key_2"): K("Ctrl-Shift-Key_2"),
        K("Cmd-Shift-Key_3"): K("Ctrl-Shift-Key_3"),
        # K("Cmd-Shift-Key_4"): K("Ctrl-Shift-Key_4"),
        # K("Cmd-Shift-Key_5"): K("Ctrl-Shift-Key_5"),
        K("Cmd-Shift-Key_6"): K("Ctrl-Shift-Key_6"),
        K("Cmd-Shift-Key_7"): K("Ctrl-Shift-Key_7"),
        K("Cmd-Shift-Key_8"): K("Ctrl-Shift-Key_8"),
        K("Cmd-Shift-Key_9"): K("Ctrl-Shift-Key_9"),

        K("Cmd-Equal"): K("Ctrl-Shift-Equal"),
        K("Cmd-Minus"): K("Ctrl-Minus"),
        K("Cmd-Key_0"): K("Ctrl-Key_0"),

        K("Alt-Backspace"): K("Alt-Shift-Backspace"), # delete word to the left
        K("Alt-Delete"): [K("Esc"), K("D")], # delete word to the right
        K("Cmd-Backspace"): K("Ctrl-U"), # delete line to the left
        K("Cmd-Delete"): K("Ctrl-K"), # delete line to the right

        K("Ctrl-Tab"): K("Ctrl-Page_Down"),
        K("Ctrl-Shift-Tab"): K("Ctrl-Page_Up"),
        K("Cmd-Shift-Left_Brace"): K("Ctrl-Page_Down"),
        K("Cmd-Shift-Right_Brace"): K("Ctrl-Page_Up"),
    }
)

defineKeymap("Tabbed applications", tabbedWindows,
    {
        K("Cmd-T"): K("Ctrl-T"),
        K("Cmd-W"): K("Ctrl-W"),
        K("Cmd-Shift-Left_Brace"): K("Ctrl-Shift-Tab"),
        K("Cmd-Shift-Right_Brace"): K("Ctrl-Tab"),
    }
)

defineKeymap("File managers", filemanagers, 
    {
        K("Cmd-Up"): K("Cmd-Up"),
        K("Cmd-Down"): K("Enter"),
        K("Cmd-Left"): K("Cmd-Left"),
        K("Cmd-Right"): K("Cmd-Right"),
        K("Cmd-Shift-dot"): K("Cmd-H"), # toggle hidden files
        K("Enter"): K("F2"), # rename
        K("Cmd-Backspace"): K("Delete"), # delete
        K("Cmd-Shift-Left_Brace"): K("Ctrl-Page_Up"), # previous tab
        K("Cmd-Shift-Right_Brace"): K("Ctrl-Page_Down"), # next tag
        K("Cmd-Shift-Left"): K("Ctrl-Page_Up"), # previous tab
        K("Cmd-Shift-Right"): K("Ctrl-Page_Down"), # next tag
    }
)

defineKeymap("Browsers", browsers, 
    {
        K("Cmd-Backslash"): K("Ctrl-Shift-L"),
        K("Cmd-Opt-Backslash"): K("Ctrl-Shift-U"),
        # K("Cmd-Left"): K("Alt-Left"), # back
        # K("Cmd-Right"): K("Alt-Right"), # forward
        K("Cmd-Left_Brace"): K("Alt-Left"), # back
        K("Cmd-Right_Brace"): K("Alt-Right"), # forward
    }
)

defineKeymapInverse("Global", ignoredWindows,
    {
        K("Cmd-A"): K("Ctrl-A"),
        K("Cmd-B"): K("Ctrl-B"),
        K("Cmd-C"): K("Ctrl-C"),
        K("Cmd-D"): K("Ctrl-D"),
        K("Cmd-E"): K("Ctrl-E"),
        K("Cmd-F"): K("Ctrl-F"),
        K("Cmd-G"): K("Ctrl-G"),
        # K("Cmd-H"): K("Ctrl-H"),
        K("Cmd-I"): K("Ctrl-I"),
        K("Cmd-J"): K("Ctrl-J"),
        K("Cmd-K"): K("Ctrl-K"),
        K("Cmd-L"): K("Ctrl-L"),
        # K("Cmd-M"): K("Ctrl-M"),
        K("Cmd-N"): K("Ctrl-N"),
        K("Cmd-O"): K("Ctrl-O"),
        K("Cmd-P"): K("Ctrl-P"),
        K("Cmd-Q"): K("Ctrl-Q"),
        K("Cmd-R"): K("Ctrl-R"),
        K("Cmd-S"): K("Ctrl-S"),
        K("Cmd-T"): K("Ctrl-T"),
        K("Cmd-U"): K("Ctrl-U"),
        K("Cmd-V"): K("Ctrl-V"),
        K("Cmd-W"): handleWindowCloseRequest,
        K("Cmd-X"): K("Ctrl-X"),
        K("Cmd-Z"): K("Ctrl-Z"),

        K("Cmd-Equal"): K("Ctrl-Equal"),
        K("Cmd-Minus"): K("Ctrl-Minus"),
        K("Cmd-Key_0"): K("Ctrl-Key_0"),
        K("Cmd-Key_1"): K("Ctrl-Key_1"),
        K("Cmd-Key_2"): K("Ctrl-Key_2"),
        K("Cmd-Key_3"): K("Ctrl-Key_3"),
        K("Cmd-Key_4"): K("Ctrl-Key_4"),
        K("Cmd-Key_5"): K("Ctrl-Key_5"),
        K("Cmd-Key_6"): K("Ctrl-Key_6"),
        K("Cmd-Key_7"): K("Ctrl-Key_7"),
        K("Cmd-Key_8"): K("Ctrl-Key_8"),
        K("Cmd-Key_9"): K("Ctrl-Key_9"),
        K("Cmd-Slash"): K("Ctrl-Slash"),

        K("Cmd-Shift-A"): K("Ctrl-Shift-A"),
        K("Cmd-Shift-B"): K("Ctrl-Shift-B"),
        K("Cmd-Shift-C"): K("Ctrl-Shift-C"),
        K("Cmd-Shift-D"): K("Ctrl-Shift-D"),
        K("Cmd-Shift-E"): K("Ctrl-Shift-E"),
        K("Cmd-Shift-F"): K("Ctrl-Shift-F"),
        K("Cmd-Shift-G"): K("Ctrl-Shift-G"),
        K("Cmd-Shift-H"): K("Ctrl-Shift-H"),
        K("Cmd-Shift-I"): K("Ctrl-Shift-I"),
        K("Cmd-Shift-J"): K("Ctrl-Shift-J"),
        K("Cmd-Shift-K"): K("Ctrl-Shift-K"),
        K("Cmd-Shift-L"): K("Ctrl-Shift-L"),
        K("Cmd-Shift-M"): K("Ctrl-Shift-M"),
        K("Cmd-Shift-N"): K("Ctrl-Shift-N"),
        K("Cmd-Shift-O"): K("Ctrl-Shift-O"),
        K("Cmd-Shift-P"): K("Ctrl-Shift-P"),
        K("Cmd-Shift-Q"): K("Ctrl-Shift-Q"),
        K("Cmd-Shift-R"): K("Ctrl-Shift-R"),
        K("Cmd-Shift-S"): K("Ctrl-Shift-S"),
        K("Cmd-Shift-T"): K("Ctrl-Shift-T"),
        K("Cmd-Shift-U"): K("Ctrl-Shift-U"),
        K("Cmd-Shift-V"): K("Ctrl-Shift-V"),
        K("Cmd-Shift-W"): K("Ctrl-Shift-W"),
        K("Cmd-Shift-X"): K("Ctrl-Shift-X"),
        K("Cmd-Shift-Z"): K("Ctrl-Shift-Z"),

        K("Cmd-Shift-Equal"): K("Ctrl-Shift-Equal"),
        K("Cmd-Shift-Minus"): K("Ctrl-Shift-Minus"),
        K("Cmd-Shift-Key_0"): K("Ctrl-Shift-Key_0"),
        K("Cmd-Shift-Key_1"): K("Ctrl-Shift-Key_1"),
        K("Cmd-Shift-Key_2"): K("Ctrl-Shift-Key_2"),
        K("Cmd-Shift-Key_3"): K("Ctrl-Shift-Key_3"),
        # K("Cmd-Shift-Key_4"): K("Ctrl-Shift-Key_4"),
        # K("Cmd-Shift-Key_5"): K("Ctrl-Shift-Key_5"),
        K("Cmd-Shift-Key_6"): K("Ctrl-Shift-Key_6"),
        K("Cmd-Shift-Key_7"): K("Ctrl-Shift-Key_7"),
        K("Cmd-Shift-Key_8"): K("Ctrl-Shift-Key_8"),
        K("Cmd-Shift-Key_9"): K("Ctrl-Shift-Key_9"),

        K("Opt-Backspace"): K("Ctrl-Backspace"),
        K("Opt-Delete"):    K("Ctrl-Delete"),

        # arrows
        K("Cmd-Up"):    K("Ctrl-Home"),
        K("Cmd-Down"):  K("Ctrl-End"),
        K("Cmd-Left"):  K("Home"),
        K("Cmd-Right"): K("End"),

        K("Cmd-Shift-Up"):      K("Ctrl-Shift-Home"),
        K("Cmd-Shift-Down"):    K("Ctrl-Shift-End"),
        K("Cmd-Shift-Left"):    K("Shift-Home"),
        K("Cmd-Shift-Right"):   K("Shift-End"),

        K("Opt-Up"):    K("Ctrl-Up"),
        K("Opt-Down"):  K("Ctrl-Down"),
        K("Opt-Left"):  K("Ctrl-Left"),
        K("Opt-Right"): K("Ctrl-Right"),

        K("Opt-Shift-Up"):      K("Ctrl-Shift-Up"),
        K("Opt-Shift-Down"):    K("Ctrl-Shift-Down"),
        K("Opt-Shift-Left"):    K("Ctrl-Shift-Left"),
        K("Opt-Shift-Right"):   K("Ctrl-Shift-Right"),

        # special symbols
        K("Cmd-Shift-Slash"): K("Ctrl-Shift-Slash"),
        K("Cmd-Backslash"): K("Cmd-Backslash"),
        K("Cmd-Backspace"): [
            K("Shift-Home"),
            K("Backspace"),
        ],
        K("Cmd-Delete"):  [
            K("Shift-End"),
            K("Backspace"),
        ],
        K("Cmd-Opt-Backslash"): K("Cmd-Opt-Backslash"),

        # K("Cmd-Ctrl-F"): K("Alt-F10"), # maximize

        # K("Cmd-a"): K("Home"),
        # K("Cmd-e"): K("End"),
        # K("Cmd-b"): K("Left"),
        # K("Cmd-f"): K("Right"),
        # K("Cmd-n"): K("Down"),
        # K("Cmd-p"): K("Up"),
        # K("Cmd-k"): [K("Shift-End"), K("Backspace")],
        # K("Cmd-d"): K("Delete"),
    }
)

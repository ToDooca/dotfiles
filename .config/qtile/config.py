#  ____        _        ____             __ _
# |  _ \ _   _( )___   / ___|___  _ __  / _(_) __ _
# | | | | | | |// __| | |   / _ \| '_ \| |_| |/ _` |
# | |_| | |_| | \__ \ | |__| (_) | | | |  _| | (_| |
# |____/ \__,_| |___/  \____\___/|_| |_|_| |_|\__, |
#                                             |___/
import os
import subprocess
from libqtile import hook, qtile
from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen, ScratchPad, DropDown
from libqtile.lazy import lazy

mod = "mod4"
terminal = "alacritty"
browser = "brave"

#  _  __          _     _           _
# | |/ /___ _   _| |__ (_)_ __   __| |___
# | ' // _ \ | | | '_ \| | '_ \ / _` / __|
# | . \  __/ |_| | |_) | | | | | (_| \__ \
# |_|\_\___|\__, |_.__/|_|_| |_|\__,_|___/
#           |___/

keys = [
    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "mod1"], "Left", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "mod1"], "Right", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "mod1"], "Down", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "mod1"], "Up", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "a", lazy.spawn('rofi -show combi'), desc="Open rofi combi"),
    Key([mod], "d", lazy.spawn('rofi -show drun'), desc="Open drun drun"),
    Key([mod], "w", lazy.spawn(browser), desc="Launch default browser"),
    Key([mod, "mod1"], "d", lazy.spawn('discord'), desc="Launch Discord"),
    Key([], "Print", lazy.spawn('flameshot gui'), desc="Take a Screenshot"),
    Key([mod], "e", lazy.spawn('thunar'), desc="Open thunar"),
    Key([mod], "m", lazy.group['scratchpad'].dropdown_toggle('spotify'), desc="Open spotify floating window"),
    Key([mod, "shift"], "m", lazy.spawn('pavucontrol'), desc="Launch volume control"),
    Key([mod, "shift"], "x", lazy.spawn('xkill'), desc="Launch volume control"),
]

#   ____
#  / ___|_ __ ___  _   _ _ __  ___
# | |  _| '__/ _ \| | | | '_ \/ __|
# | |_| | | | (_) | |_| | |_) \__ \
#  \____|_|  \___/ \__,_| .__/|___/
#                       |_|

groups = [
    Group('1', matches=[Match(wm_class='brave'), Match(wm_class='chrome')], layout="spiral"),
    Group('2', layout="spiral"),
    Group('3', layout="spiral"),
    Group('4', layout="spiral"),
    Group('5', layout="spiral"),
    Group('6', layout="spiral"),
    Group('7', layout="spiral"),
    Group('8', label="", layout="spiral"),
    Group('9', label="", layout="spiral"),
]

for i in groups:
    keys.extend([
        # mod + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen(),
            desc="Switch to group{}".format(i.name)),
        # Or, use below if you prefer not to switch to that group.
        # mod + control + letter of group = move focused window to group.
        Key([mod, "control"], i.name, lazy.window.togroup(i.name),
            desc="move focused window to group{}".format(i.name)),
    ])

# Append ScratchPad to groups list
groups.append(
    ScratchPad("scratchpad", [
        # define a drop down terminal.
        DropDown("term", terminal, opacity=0.75, height=0.5, width=0.8),
        DropDown("spotify", "spotify", y=0.13, x=0.17, opacity=1, height=0.7, width=0.65),
    ]),
)

#  _                            _
# | |    __ _ _   _  ___  _   _| |_ ___
# | |   / _` | | | |/ _ \| | | | __/ __|
# | |__| (_| | |_| | (_) | |_| | |_\__ \
# |_____\__,_|\__, |\___/ \__,_|\__|___/
#             |___/

layouts = [
    layout.Spiral(
        border_focus='#794dce',
        border_normal='#bbaee1',
        clockwise=True,
        main_pane='left',
        border_width=2,
        margin=10,
        new_client_position='after_current',
        ratio=0.5
    ),
    layout.Floating(
        border_focus='#794dce',
        border_normal='#bbaee1',
        border_width=2,
        float_rules=[
            Match(wm_class="pavucontrol"),
        ]
    ),
]

# __        ___     _            _
# \ \      / (_) __| | __ _  ___| |_ ___
#  \ \ /\ / /| |/ _` |/ _` |/ _ \ __/ __|
#   \ V  V / | | (_| | (_| |  __/ |_\__ \
#    \_/\_/  |_|\__,_|\__, |\___|\__|___/
#                     |___/

widget_defaults = dict(
    font="Fira Code",
    fontsize=14,
    padding=3,
)
extension_defaults = widget_defaults.copy()

arrowPinkInitial = widget.TextBox(
    text='',
    background='#404040',
    foreground='#bbaee1',
    padding=0,
    fontsize=45
)
arrowPink = widget.TextBox(
    text='',
    background='#794dce',
    foreground='#bbaee1',
    padding=0,
    fontsize=45
)
arrowPurple = widget.TextBox(
    text='',
    background='#bbaee1',
    foreground='#794dce',
    padding=0,
    fontsize=45
)
thermalSensorCPU = widget.ThermalSensor(
    foreground='#ffffff',
    background='#794dce',
    threshold=90,
    fmt=' CPU:{}',
    tag_sensor='Tccd1',
    padding=5
)
thermalSensorGPU = widget.ThermalSensor(
    foreground='#ffffff',
    background='#794dce',
    threshold=90,
    fmt='GPU:{}',
    tag_sensor='edge',
    padding=5
)
keyboardLayout = widget.KeyboardLayout(
                foreground='#ffffff',
                background='#794dce',
                fmt=' {}',
                padding=5
            )
ramMemory = widget.Memory(
    foreground='#ffffff',
    background='#bbaee1',
    measure_mem='G',
    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(terminal + ' -e htop')},
    fmt=' {}',
    padding=5
)
checkPackageUpdates = widget.CheckUpdates(
    update_interval=1800,
    distro="Arch_checkupdates",
    display_format=" {updates} ",
    no_update_string=' ',
    colour_have_updates='#ff5677',
    colour_no_updates='#ffffff',
    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(terminal + ' -e yay -Syu')},
    padding=5,
    background='#794dce'
)
pulseVolume = widget.PulseVolume(
    foreground='#ffffff',
    background='#bbaee1',
    fmt=' {}',
    padding=5
)
currentPlayer = widget.Mpris2(
    background='#404040',
    foreground='#bbaee1',
    padding=5,
    name='spotify',
    objname="org.mpris.MediaPlayer2.spotify",
    display_metadata=['xesam:title', 'xesam:artist'],
    fmt=' {}',
    mouse_callbacks='',
    stop_pause_text=' ',
)
diskFreeRoot = widget.DF(
    background='#404040',
    foreground='#ffffff',
    # fmt='{}',
    partition='/'
)
diskFreeHome = widget.DF(
    background='#404040',
    foreground='#ffffff',
    fmt='{}',
    partition='/home'
)
diskFreeHDD = widget.DF(
    background='#404040',
    foreground='#ffffff',
    fmt='{}',
    partition='/run/mount/sda1'
)

systemClock = widget.Clock(format="%e/%B/%Y %T", background='#794dce')

#  ____
# / ___|  ___ _ __ ___  ___ _ __  ___
# \___ \ / __| '__/ _ \/ _ \ '_ \/ __|
#  ___) | (__| | |  __/  __/ | | \__ \
# |____/ \___|_|  \___|\___|_| |_|___/

screens = [
    Screen(
        top=bar.Bar([
            widget.GroupBox(
                font='Fira Code Bold',
                fontsize=14,
                margin_y=3,
                margin_x=0,
                padding_y=7,
                padding_x=7,
                borderwidth=5,
                highlight_method='line',
                background='#404040',
                highlight_color='#404040',
                active='#ffffff',
                inactive='#bbaee1',
                this_current_screen_border='#794dce',
                this_screen_border='#794dce',
                hide_unused=True,
                rounded=False,
                disable_drag=True
            ),
            widget.Spacer(background='#404040'),
            currentPlayer,
            arrowPinkInitial,
            # diskFreeRoot,
            # diskFreeHome,
            # diskFreeHDD,
            widget.CPU(format=' {load_percent}%', background='#bbaee1'),
            arrowPurple,
            thermalSensorCPU,
            thermalSensorGPU,
            arrowPink,
            ramMemory,
            arrowPurple,
            checkPackageUpdates,
            arrowPink,
            pulseVolume,
            arrowPurple,
            keyboardLayout,
            arrowPink,
            widget.Systray(background='#bbaee1', padding=5),
            arrowPurple,
            systemClock
        ], 25),
    ),
    Screen(
        top=bar.Bar([
            widget.GroupBox(
                font='Fira Code Bold',
                fontsize=14,
                margin_y=3,
                margin_x=0,
                padding_y=7,
                padding_x=7,
                borderwidth=5,
                highlight_method='line',
                background='#404040',
                highlight_color='#404040',
                active='#ffffff',
                inactive='#bbaee1',
                this_current_screen_border='#794dce',
                this_screen_border='#794dce',
                hide_unused=True,
                rounded=False,
                disable_drag=True
            ),
            widget.Spacer(background='#404040'),
            currentPlayer,
            arrowPinkInitial,
            widget.CPU(format=' {load_percent}%', background='#bbaee1'),
            arrowPurple,
            thermalSensorCPU,
            thermalSensorGPU,
            arrowPink,
            ramMemory,
            arrowPurple,
            checkPackageUpdates,
            arrowPink,
            pulseVolume,
            arrowPurple,
            systemClock
        ], 25),
    ),
    Screen(
        top=bar.Bar([
            widget.GroupBox(
                font='Fira Code Bold',
                fontsize=14,
                margin_y=3,
                margin_x=0,
                padding_y=7,
                padding_x=7,
                borderwidth=5,
                highlight_method='line',
                background='#404040',
                highlight_color='#404040',
                active='#ffffff',
                inactive='#bbaee1',
                this_current_screen_border='#794dce',
                this_screen_border='#794dce',
                hide_unused=True,
                rounded=False,
                disable_drag=True
            ),
            widget.Spacer(background='#404040'),
            currentPlayer,
            arrowPinkInitial,
            widget.CPU(format=' {load_percent}%', background='#bbaee1'),
            arrowPurple,
            thermalSensorCPU,
            thermalSensorGPU,
            arrowPink,
            ramMemory,
            arrowPurple,
            checkPackageUpdates,
            arrowPink,
            pulseVolume,
            arrowPurple,
            systemClock
        ], 25),
    )
]

#  __  __
# |  \/  | ___  _   _ ___  ___
# | |\/| |/ _ \| | | / __|/ _ \
# | |  | | (_) | |_| \__ \  __/
# |_|  |_|\___/ \__,_|___/\___|

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

#  _   _             _
# | | | | ___   ___ | | _____
# | |_| |/ _ \ / _ \| |/ / __|
# |  _  | (_) | (_) |   <\__ \
# |_| |_|\___/ \___/|_|\_\___/

dgroups_app_rules = []  # type: list
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None
bring_front_click = False
auto_fullscreen = True
follow_mouse_focus = True
cursor_warp = False
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wmname = "LG3D"


#  ____  _             _
# / ___|| |_ __ _ _ __| |_ _   _ _ __
# \___ \| __/ _` | '__| __| | | | '_ \
#  ___) | || (_| | |  | |_| |_| | |_) |
# |____/ \__\__,_|_|   \__|\__,_| .__/
#                               |_|

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.run([home])

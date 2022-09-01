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
from libqtile.config import Drag, Group, Key, KeyChord, Match, Screen, ScratchPad, DropDown
from libqtile.lazy import lazy

mod = "mod4"
alt = "mod1"
shift = "shift"
control = "control"
terminal = "alacritty"
browser = "brave"

#  _  __          _     _           _
# | |/ /___ _   _| |__ (_)_ __   __| |___
# | ' // _ \ | | | '_ \| | '_ \ / _` / __|
# | . \  __/ |_| | |_) | | | | | (_| \__ \
# |_|\_\___|\__, |_.__/|_|_| |_|\__,_|___/
#           |___/
# @formatter:off
keys = [

    Key([mod], "Return",            lazy.spawn(terminal),                     desc="Launch terminal"),
    Key([mod], "Tab",               lazy.next_layout(),                       desc="Toggle between layouts"),
    Key([mod], "q",                 lazy.window.kill(),                       desc="Kill focused window"),
    Key([mod, control], "r",        lazy.reload_config(),                     desc="Reload the config"),
    Key([mod, control], "q",        lazy.shutdown(),                          desc="Shutdown Qtile"),
    Key([mod], "a",                 lazy.spawn('rofi -show combi'),           desc="Open rofi combi"),
    Key([mod], "d",                 lazy.spawn('rofi -show drun'),            desc="Open drun drun"),
    Key([mod], "w",                 lazy.spawn(browser),                      desc="Launch default browser"),
    Key([mod, shift], "f",          lazy.window.toggle_floating(),            desc="Toggle Floating layout"),
    Key([mod, alt], "f",            lazy.window.toggle_maximize(),            desc="Toggle Full-screen layout"),
    Key([mod], "f",                 lazy.window.toggle_fullscreen(),          desc="Toggle Full-screen layout"),
    Key([], "Print",                lazy.spawn('flameshot gui'),              desc="Take a Screenshot"),
    Key([mod], "e",                 lazy.spawn('nautilus'),                   desc="Open thunar"),
    Key([mod, shift], "x",          lazy.spawn('xkill'),                      desc="Launch xkill"),
    Key([mod, shift], "p",          lazy.spawn('killall picom'),              desc="turn off picom"),
    Key([mod, shift], "c",          lazy.group['6'].toscreen(),               desc="go to coding group"),
    Key([mod], "p",                 lazy.spawn('picom --experimental-backends')),
    Key([mod, alt], "l",            lazy.spawn('lutris')),
    Key([mod, alt], "d",            lazy.spawn('discord')),
    Key([mod], "t",                 lazy.spawn('telegram-desktop')),
    Key([mod, shift], "t",          lazy.spawn('whatsapp-for-linux')),

    # Layout Keybinds
    Key([mod], "Left",              lazy.layout.left(),                       desc="Move focus to left"),
    Key([mod], "Right",             lazy.layout.right(),                      desc="Move focus to right"),
    Key([mod], "Down",              lazy.layout.down(),                       desc="Move focus down"),
    Key([mod], "Up",                lazy.layout.up(),                         desc="Move focus up"),
    Key([mod], "space",             lazy.layout.next(),                       desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    Key([mod, shift], "Left",       lazy.layout.shuffle_left(),               desc="Move window to the left"),
    Key([mod, shift], "Right",      lazy.layout.shuffle_right(),              desc="Move window to the right"),
    Key([mod, shift], "Down",       lazy.layout.shuffle_down(),               desc="Move window down"),
    Key([mod, shift], "Up",         lazy.layout.shuffle_up(),                 desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, alt], "Left",         lazy.layout.grow_left(),                  desc="Grow window to the left"),
    Key([mod, alt], "Right",        lazy.layout.grow_right(),                 desc="Grow window to the right"),
    Key([mod, alt], "Down",         lazy.layout.grow_down(),                  desc="Grow window down"),
    Key([mod, alt], "Up",           lazy.layout.grow_up(),                    desc="Grow window up"),
    Key([mod], "n",                 lazy.layout.normalize(),                  desc="Reset all window sizes"),

    # Toggle between monitors
    Key([mod], "x",                 lazy.to_screen(0),                        desc='Keyboard focus to monitor 1'),
    Key([mod], "z",                 lazy.to_screen(1),                        desc='Keyboard focus to monitor 2'),
    Key([mod], "c",                 lazy.to_screen(2),                        desc='Keyboard focus to monitor 3'),

    # Notifications
    Key([mod, alt], "n",            lazy.spawn("dunstctl set-paused toggle"), desc='Toggle notifications'),
    Key([mod], "n",                 lazy.spawn("dunstctl close-all"),         desc='Toggle notifications'),

    # Keyboard Layouts
    Key([mod], "l",                 lazy.spawn("setxkbmap -layout us"),       desc='Toggle us layout'),
    Key([mod, shift], "l",          lazy.spawn("setxkbmap -layout rs latin"), desc='Toggle Serbian latin layout'),

    # Power options
    KeyChord([mod], "0", [
        Key([shift], "s",           lazy.spawn('systemctl poweroff'),         desc='Turn off the computer'),
        Key([], "r",                lazy.spawn('systemctl reboot'),           desc='Reboot the computer'),
        Key([], "s",                lazy.spawn('systemctl suspend'),          desc='Suspend'),
        Key([], "h",                lazy.spawn('systemctl hibernate'),        desc='Hibernate'),
    ]),

    # Code Editors
    KeyChord([mod, shift], "o", [
        Key([], "i",                lazy.spawn('idea'),     lazy.group['6'].toscreen()),
        Key([], "p",                lazy.spawn('pycharm'),  lazy.group['6'].toscreen()),
        Key([], "w",                lazy.spawn('webstorm'), lazy.group['6'].toscreen()),
    ]),
    KeyChord([mod], "o", [
        Key([], "i",                lazy.spawn('codeopen -m rofi -t idea'),     lazy.group['6'].toscreen()),
        Key([], "p",                lazy.spawn('codeopen -m rofi -t pycharm'),  lazy.group['6'].toscreen()),
        Key([], "w",                lazy.spawn('codeopen -m rofi -t webstorm'), lazy.group['6'].toscreen()),
    ]),

    # Music and audio related keybinds
    Key([mod, shift], "m",             lazy.group['scratchpad'].dropdown_toggle('pavucontrol')),
    Key([mod], "m",                    lazy.group['scratchpad'].dropdown_toggle('spotify')),
    Key([mod, alt, control], "m",      lazy.spawn('stremio'), lazy.group['8'].toscreen()),
    Key([mod], "comma",                lazy.spawn("playerctl --player=spotify,%any previous")),
    Key([mod], "period",               lazy.spawn("playerctl --player=spotify,%any next")),
    Key([mod], "slash",                lazy.spawn("playerctl --player=spotify,%any play-pause")),
    Key([], "XF86AudioPlay",           lazy.spawn("playerctl --player=spotify,%any play-pause")),
    Key([], "XF86AudioPause",          lazy.spawn("playerctl --player=spotify,%any play-pause")),
    Key([], "XF86AudioStop",           lazy.spawn("playerctl --player=spotify,%any stop")),
    Key([], "XF86AudioNext",           lazy.spawn("playerctl --player=spotify,%any next")),
    Key([], "XF86AudioPrev",           lazy.spawn("playerctl --player=spotify,%any previous")),
    Key([mod, control, alt], "comma",  lazy.spawn("padefault volume-focus -5%")),
    Key([mod, control, alt], "period", lazy.spawn("padefault volume-focus +5%")),
    Key([mod, control, alt], "slash",  lazy.spawn("padefault volume-focus 100%")),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, shift], "Return",           lazy.layout.toggle_split()),

]
# @formatter:on
#   ____
#  / ___|_ __ ___  _   _ _ __  ___
# | |  _| '__/ _ \| | | | '_ \/ __|
# | |_| | | | (_) | |_| | |_) \__ \
#  \____|_|  \___/ \__,_| .__/|___/
#                       |_|

groups = [
    Group('1', matches=[Match(wm_class='brave')], layout="columns"),
    Group('2', layout="columns"),
    Group('3', layout="columns"),
    Group('4', layout="columns"),
    Group('5', layout="columns"),
    Group('6', label="", layout="stack", matches=[
        Match(wm_class="jetbrains-idea"),
        Match(wm_class="jetbrains-webstorm"),
        Match(wm_class="jetbrains-pycharm"),
    ]),
    Group('7', label="", layout="monadwide", matches=[
        Match(wm_class="steam"),
        Match(wm_class="lutris"),
    ]),
    Group('8', label="", layout="columns", matches=[
        Match(wm_class="netflix"),
        Match(wm_class="stremio"),
    ]),
    Group('9', label="", layout="columns", matches=[
        Match(wm_class="telegram-desktop"),
        Match(wm_class="discord"),
        Match(wm_class="whatsapp-for-linux"),
    ]),
]

for i in groups:
    keys.extend([
        # mod + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen(),
            desc="Switch to group{}".format(i.name)),
        # Or, use below if you prefer not to switch to that group.
        # mod + control + letter of group = move focused window to group.
        Key([mod, control], i.name, lazy.window.togroup(i.name),
            desc="move focused window to group{}".format(i.name)),
        Key([mod, shift], i.name, lazy.window.togroup(i.name), lazy.group[i.name].toscreen(),
            desc="move focused window and screen to group{}".format(i.name)),
    ])

# Append ScratchPad to groups list
groups.append(
    ScratchPad("scratchpad", [
        # define a drop down terminal.
        DropDown("term", terminal, opacity=0.75, height=0.5, width=0.8),
        DropDown("spotify", "spotify", y=0.13, x=0.17, opacity=1, height=0.7, width=0.65),
        DropDown("steam", "steam", y=0.13, x=0.17, opacity=1, height=0.7, width=0.65),
        DropDown("pavucontrol", "pavucontrol", y=0.13, x=0.17, opacity=1, height=0.7, width=0.65),
    ]),
)

#  _                            _
# | |    __ _ _   _  ___  _   _| |_ ___
# | |   / _` | | | |/ _ \| | | | __/ __|
# | |__| (_| | |_| | (_) | |_| | |_\__ \
# |_____\__,_|\__, |\___/ \__,_|\__|___/
#             |___/

default_layout_settings = dict(
    border_focus="#4d4c7d",
    border_normal="#e9d5da",
    border_width=2,
)

layouts = [
    layout.Columns(
        **default_layout_settings,
        margin=7,
        border_on_single=True,
    ),
    layout.Stack(
        **default_layout_settings,
        margin=7,
        num_stacks=1,
    ),
    layout.MonadWide(
        **default_layout_settings
    )
]

# __        ___     _            _
# \ \      / (_) __| | __ _  ___| |_ ___
#  \ \ /\ / /| |/ _` |/ _` |/ _ \ __/ __|
#   \ V  V / | | (_| | (_| |  __/ |_\__ \
#    \_/\_/  |_|\__,_|\__, |\___|\__|___/
#                     |___/

widget_defaults = dict(
    font="Fira Code Bold",
    fontsize=14,
    padding=3,
)
extension_defaults = widget_defaults.copy()


def notification_widget():
    return widget.TextBox(
        font='Fira Code',
        background='#363062',
        foreground='#827397',
        text='',
        mouse_callbacks={
            'Button1': lazy.spawn("dunstctl history-pop"),
            'Button2': lazy.spawn("dunstctl set-paused toggle"),
            'Button3': lazy.spawn("dunstctl close-all")
        }
    )


def widget_icon(icon):
    return widget.TextBox(
        font='Fira Code',
        text=icon,
        background='#363062',
        foreground='#827397'
    )


divider = widget.TextBox(
    text='|',
    background='#363062',
    foreground='#4d4c7d'
)
thermalSensorCPU = widget.ThermalSensor(
    foreground='#e9d5da',
    background='#363062',
    threshold=90,
    fmt='CPU:{}',
    tag_sensor='Tccd1',
    padding=5
)
thermalSensorGPU = widget.ThermalSensor(
    foreground='#e9d5da',
    background='#363062',
    threshold=90,
    fmt='GPU:{}',
    tag_sensor='edge',
    padding=5
)
keyboardLayout = widget.KeyboardLayout(
    foreground='#e9d5da',
    background='#363062',
    padding=5,
    configured_keyboards=['us', 'rs latin', 'rs']

)
ramMemory = widget.Memory(
    foreground='#e9d5da',
    background='#363062',
    measure_mem='G',
    format='{MemUsed:.0f}{mm}/{MemTotal:.0f}{mm}',
    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(terminal + ' -e htop')},
    padding=5
)
checkPackageUpdates = widget.CheckUpdates(
    update_interval=1800,
    distro="Arch_checkupdates",
    display_format="{updates} ",
    no_update_string=' ',
    colour_have_updates='#ff5677',
    colour_no_updates='#e9d5da',
    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(terminal + ' -e yay -Syu')},
    padding=5,
    background='#363062'
)
pulseVolume = widget.PulseVolume(
    foreground='#e9d5da',
    background='#363062',
    padding=5
)
currentPlayer = widget.Mpris2(
    background='#363062',
    foreground='#e9d5da',
    name='spotify',
    objname="org.mpris.MediaPlayer2.spotify",
    display_metadata=['xesam:title', 'xesam:artist'],
    fmt=' {}',
    stop_pause_text=' ',
)

diskFreeRoot = widget.DF(
    background='#363062',
    foreground='#e9d5da',
    warn_color='#ff5677',
    fmt=' {}',
    format='{f}GB',
    partition="/",
)

diskFreeHome = widget.DF(
    background='#363062',
    foreground='#e9d5da',
    warn_color='#ff5677',
    fmt=' {}',
    format='{f}GB',
    partition="/home",
)
diskFreeHDD = widget.DF(
    background='#363062',
    foreground='#e9d5da',
    warn_color='#ff5677',
    fmt=' {}',
    format='{f}GB',
    partition="/run/mount/sda1",
)
systemClock = widget.Clock(
    format="%e/%B/%Y %T",
    background='#363062',
    foreground='#e9d5da',
)

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
                borderwidth=3,
                highlight_method='line',
                background='#363062',
                highlight_color='#363062',
                inactive='#827397',
                active='#e9d5da',
                this_current_screen_border='#e9d5da',
                this_screen_border='#e9d5da',
                rounded=False,
                disable_drag=True
            ),
            divider,
            widget_icon(''),
            keyboardLayout,
            divider,
            widget_icon(''),
            pulseVolume,
            divider,
            notification_widget(),
            divider,
            widget_icon(''),
            checkPackageUpdates,
            divider,
            widget.Spacer(background='#363062'),
            systemClock,
            widget.Spacer(background='#363062'),
            divider,
            widget_icon(''),
            ramMemory,
            divider,
            widget_icon(''),
            widget.CPU(format='{load_percent}%', background='#363062', foreground='#e9d5da'),
            divider,
            widget_icon(''),
            thermalSensorCPU,
            thermalSensorGPU,
            divider,
            diskFreeRoot,
            diskFreeHome,
            diskFreeHDD,
            widget.Systray(background='#363062', padding=5),
            widget.Spacer(background='#363062', length=15)
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
                borderwidth=3,
                highlight_method='line',
                background='#363062',
                highlight_color='#363062',
                inactive='#827397',
                active='#e9d5da',
                this_current_screen_border='#e9d5da',
                this_screen_border='#e9d5da',
                rounded=False,
                disable_drag=True
            ),
            divider,
            widget_icon(''),
            keyboardLayout,
            divider,
            widget_icon(''),
            pulseVolume,
            divider,
            notification_widget(),
            divider,
            widget_icon(''),
            checkPackageUpdates,
            divider,
            widget.Spacer(background='#363062'),
            systemClock,
            widget.Spacer(background='#363062'),
            divider,
            widget_icon(''),
            ramMemory,
            divider,
            widget_icon(''),
            widget.CPU(format='{load_percent}%', background='#363062', foreground='#e9d5da'),
            divider,
            widget_icon(''),
            thermalSensorCPU,
            thermalSensorGPU,
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
                borderwidth=3,
                highlight_method='line',
                background='#363062',
                highlight_color='#363062',
                inactive='#827397',
                active='#e9d5da',
                this_current_screen_border='#e9d5da',
                this_screen_border='#e9d5da',
                rounded=False,
                disable_drag=True
            ),
            divider,
            widget_icon(''),
            keyboardLayout,
            divider,
            widget_icon(''),
            pulseVolume,
            divider,
            notification_widget(),
            divider,
            widget_icon(''),
            checkPackageUpdates,
            divider,
            widget.Spacer(background='#363062'),
            systemClock,
            widget.Spacer(background='#363062'),
            divider,
            widget_icon(''),
            ramMemory,
            divider,
            widget_icon(''),
            widget.CPU(format='{load_percent}%', background='#363062', foreground='#e9d5da'),
            divider,
            widget_icon(''),
            thermalSensorCPU,
            thermalSensorGPU,
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
    Drag([mod], "Button2", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
]

#  _   _             _
# | | | | ___   ___ | | _____
# | |_| |/ _ \ / _ \| |/ / __|
# |  _  | (_) | (_) |   <\__ \
# |_| |_|\___/ \___/|_|\_\___/

floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="spotify"),
        Match(wm_class="pavucontrol"),
        Match(wm_class="steam"),
        Match(wm_class="lutris"),
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ], **default_layout_settings)
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

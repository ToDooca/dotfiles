#   ________        _        ____             __ _      ____
#  / / /  _ \ _   _( )___   / ___|___  _ __  / _(_) __ _\ \ \   Copyright (c) 2022 Dušan Stanković
# / / /| | | | | | |// __| | |   / _ \| '_ \| |_| |/ _` |\ \ \
# \ \ \| |_| | |_| | \__ \ | |__| (_) | | | |  _| | (_| |/ / /
#  \_\_\____/ \__,_| |___/  \____\___/|_| |_|_| |_|\__, /_/_/   http://www.github.com/ToDooca
#                                                  |___/
import os
import subprocess
from libqtile import hook, qtile
from libqtile import bar, layout, widget
from libqtile.config import Drag, Group, Key, KeyChord, Match, Screen, ScratchPad, DropDown
from libqtile.lazy import lazy
from qtile_extras.widget.decorations import RectDecoration
from qtile_extras import widget as qtile_extras_widget

mod = "mod4"
alt = "mod1"
shift = "shift"
control = "control"
terminal = "alacritty"
browser = "brave"

#   ____      _
#  / ___|___ | | ___  _ __ ___
# | |   / _ \| |/ _ \| '__/ __|
# | |__| (_) | | (_) | |  \__ \
#  \____\___/|_|\___/|_|  |___/
#

purple = '#827397'
light_purple = '#4d4c7d'
dark_purple = '#363062'
warn_pink = '#ff5677'
light_pink = '#e9d5da'
picom_transparent = '#00000000'

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
    Key([mod, control], "r",        lazy.reload_config(),
                                    lazy.spawn("xmodmap /home/du/.Xmodmap"),  desc="Reload the config"),
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
    Key([mod], "p",                 lazy.spawn('picom')),
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
    Key([mod], "l",                 lazy.spawn("setxkbmap -layout us"),
                                    lazy.spawn("xmodmap /home/du/.Xmodmap"),  desc='Toggle us layout'),
    Key([alt], "Tab",               lazy.widget["keyboardlayout"].next_keyboard(),
                                    lazy.spawn("xmodmap /home/du/.Xmodmap"),  desc='Cycle through keyboard layouts'),

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
    Key([mod, control], "m",           lazy.group['scratchpad'].dropdown_toggle('spt')),
    Key([mod, alt, control], "m",      lazy.spawn('stremio'), lazy.group['8'].toscreen()),
    Key([mod], "comma",                lazy.spawn("playerctl --player=spotify,%any previous")),
    Key([mod], "period",               lazy.spawn("playerctl --player=spotify,%any next")),
    Key([mod], "slash",                lazy.spawn("playerctl --player=spotify,%any play-pause")),
    Key([control], "XF86AudioMute",    lazy.spawn("playerctl --player=spotify,%any next")),
    Key([], "XF86AudioMute",           lazy.spawn("playerctl -p spotify play-pause")),
    Key([], "XF86AudioRaiseVolume",    lazy.spawn("playerctl -p spotify volume 0.05+")),
    Key([], "XF86AudioLowerVolume",    lazy.spawn("playerctl -p spotify volume 0.05-")),
    Key([], "XF86AudioPlay",           lazy.spawn("playerctl --player=spotify,%any play-pause")),
    Key([], "XF86AudioPlay",           lazy.spawn("playerctl --player=spotify,%any play-pause")),
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
        Match(wm_class="Steam"),
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
        DropDown("term", terminal, y=0.13, x=0.17, opacity=1, height=0.9, width=0.65),
        DropDown("spt", terminal + " -e spt", y=0.13, x=0.17, opacity=0.75, height=0.7, width=0.65),
        DropDown("spotify", "spotify", y=0.13, x=0.17, opacity=1, height=0.7, width=0.65),
        DropDown("Steam", "Steam", y=0.13, x=0.17, opacity=1, height=0.7, width=0.65),
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
    border_focus=light_purple,
    border_normal=light_pink,
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
    padding=10,
)
decoration_group = {
    "decorations": [
        RectDecoration(colour=dark_purple, radius=12, filled=True, padding_y=4, group=True)
    ],
    "decoration_width": 0,
    "decoration_height": 0,
}
extension_defaults = widget_defaults.copy()


def notification_widget():
    return qtile_extras_widget.TextBox(
        **decoration_group,
        font='Fira Code',
        foreground=purple,
        text='',
        padding=10,
        mouse_callbacks={
            'Button1': lazy.spawn("dunstctl history-pop"),
            'Button2': lazy.spawn("dunstctl set-paused toggle"),
            'Button3': lazy.spawn("dunstctl close-all")
        }
    )


def widget_icon(icon):
    return qtile_extras_widget.TextBox(
        **decoration_group,
        font='Fira Code',
        text=icon,
        foreground=purple,
    )


def keyboard_layout():
    return qtile_extras_widget.KeyboardLayout(
        **decoration_group,
        foreground=light_pink,
        configured_keyboards=['us', 'rs latin', 'rs']
    )


def ram_memory():
    return qtile_extras_widget.Memory(
        **decoration_group,
        width=80,
        foreground=light_pink,
        measure_mem='G',
        format='{MemUsed:.0f}{mm}/{MemTotal:.0f}{mm}',
        mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(terminal + ' -e htop')},
    )


def check_package_updates():
    return qtile_extras_widget.CheckUpdates(
        **decoration_group,
        update_interval=1800,
        distro="Arch_checkupdates",
        display_format="{updates} ",
        no_update_string=' ',
        colour_have_updates=warn_pink,
        colour_no_updates=light_pink,
        mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(terminal + ' -e yay -Syu')},
    )


def pulse_volume():
    return qtile_extras_widget.PulseVolume(
        **decoration_group,
        foreground=light_pink,
    )


def disk_free(disk_fmt, disk_partition):
    return qtile_extras_widget.DF(
        **decoration_group,
        foreground=light_pink,
        warn_color=warn_pink,
        fmt=disk_fmt,
        format='{f}GB',
        partition=disk_partition,
    )


def system_clock():
    return qtile_extras_widget.Clock(
        **decoration_group,
        format="%e/%B/%Y %T",
        foreground=light_pink,
        popup_text=['%A, %B %d %Y', 'Time in UTC: %T'],
    )


def thermal_sensor(sensor_fmt, sensor, sensor_threshold):
    return qtile_extras_widget.ThermalSensor(
        **decoration_group,
        foreground=light_pink,
        foreground_alert=warn_pink,
        threshold=sensor_threshold,
        fmt=sensor_fmt,
        tag_sensor=sensor,
    )


def music_widget():
    return qtile_extras_widget.Mpris2(
        **decoration_group,
        foreground=light_pink,
        width=200,
        name='spotify',
        objname='org.mpris.MediaPlayer2.spotify',
        display_metadata=['xesam:title', 'xesam:artist'],
        paused_text='',
        stopped_text='',
        scroll_interval=0.025,
        scroll_delay=3,
        mouse_callbacks={
            'Button1': lambda: qtile.cmd_spawn("playerctl -p spotify next"),
            'Button2': lambda: qtile.cmd_spawn("playerctl -p spotify play-pause"),
            'Button3': lambda: qtile.cmd_spawn("playerctl -p spotify previous"),
        },
    )


def drawer(widgets_arr):
    return qtile_extras_widget.WidgetBox(
        **decoration_group,
        foreground=light_pink,
        text_open='',
        text_closed='  ',
        widgets=widgets_arr,
    )


#  ____
# / ___|  ___ _ __ ___  ___ _ __  ___
# \___ \ / __| '__/ _ \/ _ \ '_ \/ __|
#  ___) | (__| | |  __/  __/ | | \__ \
# |____/ \___|_|  \___|\___|_| |_|___/

def screen_widgets(primary=False):
    widgets = [
        widget.Spacer(length=7),
        qtile_extras_widget.GroupBox(
            **decoration_group,
            font='Fira Code Bold',
            fontsize=14,
            margin_y=3,
            margin_x=0,
            padding_y=7,
            padding_x=7,
            borderwidth=3,
            highlight_method='text',
            urgent_alert_method='text',
            urgent_border=warn_pink,
            border_color=dark_purple,
            highlight_color=dark_purple,
            inactive=purple,
            active=light_pink,
            this_current_screen_border=light_pink,
            this_screen_border=light_pink,
            rounded=False,
            disable_drag=True
        ),
        widget.Spacer(length=3),
        widget_icon(''),
        keyboard_layout(),
        widget.Spacer(length=3),
        widget_icon(''),
        pulse_volume(),
        widget.Spacer(length=3),
        widget_icon(''),
        check_package_updates(),
        widget.Spacer(length=3),
        notification_widget(),
        widget.Spacer(),
        system_clock(),
        widget.Spacer(),
        widget_icon(''),
        music_widget(),
        widget.Spacer(length=3),
        widget_icon(''),
        ram_memory(),
        widget.Spacer(length=3),
        widget_icon(''),
        qtile_extras_widget.CPU(format='{load_percent}%', foreground=light_pink, width=65, **decoration_group),
        widget.Spacer(length=3),
        widget_icon(''),
        drawer([thermal_sensor('CPU:{}', 'Tccd1', 45), thermal_sensor('GPU:{}', 'edge', 75)]),
        widget.Spacer(length=7),
    ]
    if primary:
        widgets.extend([
            qtile_extras_widget.Systray(),
            widget.Spacer(length=7),
        ])
        return widgets
    return widgets


screens = [
    Screen(
        top=bar.Bar(
            screen_widgets(primary=True),
            38,
            background=picom_transparent),
    ),
    Screen(
        top=bar.Bar(
            screen_widgets(),
            38,
            background=picom_transparent),
    ),
    # Remove code block below for a two monitor setup
    Screen(
        top=bar.Bar(
            screen_widgets(),
            38,
            background=picom_transparent),
    ),
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
        Match(wm_class="Steam"),
        Match(wm_class="lutris"),
        Match(wm_class="battle.net.exe"),
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

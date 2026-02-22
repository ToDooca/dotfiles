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
from libqtile.log_utils import logger
# from openrazer.client import DeviceManager

terminal = os.getenv("terminal", "alacritty")
browser = os.getenv("browser", "floorp")

mod = "mod4"
alt = "mod1"
shift = "shift"
control = "control"
mouse_left = "Button1"
mouse_middle = "Button2"
mouse_right = "Button3"
scroll_up = "Button4"
scroll_down = "Button5"

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
    Key([mod], "d",                 lazy.spawn('rofi -show drun'),            desc="Open rofi drun"),
    Key([alt], "tab",               lazy.spawn('rofi -show window'),          desc="Open rofi windows"),
    Key([mod], "w",                 lazy.spawn(browser),                      desc="Launch default browser"),
    Key([mod, shift], "w",          lazy.spawn('google-chrome-stable'),       desc="Launch google chrome"),
    Key([mod, shift], "f",          lazy.window.toggle_floating(),            desc="Toggle Floating layout"),
    Key([mod, alt], "f",            lazy.window.toggle_maximize(),            desc="Toggle Full-screen layout"),
    Key([mod], "f",                 lazy.window.toggle_fullscreen(),          desc="Toggle Full-screen layout"),
    Key([], "Print",                lazy.spawn('flameshot gui'),              desc="Take a Screenshot"),
    Key([mod], "e",                 lazy.spawn('thunar'),                     desc="Open thunar"),
    Key([mod, shift], "x",          lazy.spawn('xkill'),                      desc="Launch xkill"),
    Key([mod, shift], "p",          lazy.spawn('killall picom'),              desc="turn off picom"),
    Key([mod, shift], "c",          lazy.group['6'].toscreen(),               desc="go to coding group"),
    Key([mod], "p",                 lazy.spawn('picom')),
    Key([mod, alt], "l",            lazy.spawn('lutris')),
    Key([mod, alt], "d",            lazy.spawn('discord')),
    Key([mod], "t",                 lazy.spawn('Telegram')),
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
    Key([mod], "z",                 lazy.to_screen(2),                        desc='Keyboard focus to monitor 2'),
    Key([mod], "c",                 lazy.to_screen(1),                        desc='Keyboard focus to monitor 3'),

    # Notifications
    Key([mod, alt], "n",            lazy.spawn("dunstctl set-paused toggle"), desc='Toggle notifications'),
    Key([mod], "n",                 lazy.spawn("dunstctl close-all"),         desc='Toggle notifications'),

    # Keyboard Layouts
    Key([mod], "l",                 lazy.spawn("setxkbmap -layout us"),
                                    lazy.spawn("xmodmap /home/du/.Xmodmap"),  desc='Toggle us layout'),
    Key([control], "Tab",           lazy.widget["keyboardlayout"].next_keyboard(),
                                    lazy.spawn("xmodmap /home/du/.Xmodmap"),  desc='Cycle through keyboard layouts'),
    # Power options
    Key([mod], "0",                 lazy.spawn("xfce4-session-logout"),       desc='poweroff settings'),

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
    Key([mod], "XF86AudioLowerVolume", lazy.spawn("padefault volume-focus -5%")),
    Key([mod], "XF86AudioRaiseVolume", lazy.spawn("padefault volume-focus +5%")),
    Key([mod], "XF86AudioMute",        lazy.spawn("playerctl --player=spotify,%any play-pause")),
    Key([mod, alt], "XF86AudioMute",   lazy.spawn('reload-headphones')),

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
    Group('1', matches=[Match(wm_class='floorp')], layout="columns"),
    Group('2', layout="columns"),
    Group('3', layout="columns"),
    Group('4', layout="columns"),
    Group('5', layout="columns"),
    Group('6', layout="stack", matches=[
        Match(wm_class="jetbrains-idea"),
        Match(wm_class="jetbrains-webstorm"),
        Match(wm_class="jetbrains-pycharm"),
    ]),
    Group('7', layout="max", matches=[
        Match(wm_class="steam"),
        Match(wm_class="net.lutris.Lutris"),
        Match(wm_class="battle.net.exe"),
        Match(wm_class="hearthstone.exe"),
        Match(wm_class="hearthstonedecktracker.exe"),
    ]),
    Group('8', layout="columns", matches=[
        Match(wm_class="netflix"),
        Match(wm_class="stremio"),
    ]),
    Group('9', layout="columns", matches=[
        Match(wm_class="Telegram"),
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
    border_focus=light_pink,
    border_normal=light_purple,
    border_width=2,
)

layouts = [
    layout.Columns(
        **default_layout_settings,
        margin=6,
        border_on_single=True,
    ),
    layout.Stack(
        **default_layout_settings,
        margin=6,
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
        RectDecoration(colour=dark_purple, radius=9, filled=True, padding_y=4, group=True)
    ],
    "decoration_width": 0,
    "decoration_height": 0,
}

extension_defaults = widget_defaults.copy()


def notification_widget():
    return qtile_extras_widget.TextBox(
        **decoration_group,
        foreground=purple,
        text=' ',
        padding=14,
        mouse_callbacks={
            mouse_left: lazy.spawn("dunstctl history-pop"),
            mouse_middle: lazy.spawn("dunstctl set-paused toggle"),
            mouse_right: lazy.spawn("dunstctl close-all")
        }
    )


def headset_battery():
    return qtile_extras_widget.GenPollText(
        **decoration_group,
        foreground=light_pink,
        font='Fira Code',
        fontsize=17,
        func=(
            lambda: subprocess.getoutput(
                "headsetcontrol -b 2>&1 | grep  -Eo '([0-9]{1,3}%|Charging|Unavailable|No supported headset found)'"
                " | sed 's/Charging/󰂄/;s/Unavailable/󰥇/;s/No supported headset found//"
                ";s/25%/󱊡/;s/50%/󱊢/;s/75%/󱊣/;s/100%/󱊣/'"
            )
        ),
        mouse_callbacks={"Button1": lazy.widget["genpolltext"].function(lambda w: w.update(w.poll()))},
        update_interval=180
    )


# def get_basilisk_battery_level():
#     device_manager = DeviceManager()
#     basilisk = None
#     for device in device_manager.devices:
#         if "Razer Basilisk V3 Pro (Wireless)" == device.name:
#             basilisk = device
#             break
#
#     if basilisk is None:
#         return ''
#
#     charging = basilisk.is_charging
#     battery_level = basilisk.battery_level
#
#     if charging is False:
#         if battery_level == 0:
#             return '󰒲'
#         elif battery_level > 75:
#             return '󱊣'
#         elif battery_level > 25:
#             return '󱊢'
#         elif battery_level > 10:
#             return '󱊡'
#         elif battery_level > 0:
#             return '󰂎'
#         else:
#             return ''
#     else:
#         return '󰂄'


# def mouse_battery():
#     return qtile_extras_widget.GenPollText(
#         **decoration_group,
#         foreground=light_pink,
#         font='Fira Code',
#         fontsize=17,
#         update_interval=180,
#         func=get_basilisk_battery_level,
#         fmt='{}'
#     )


def spotify_widget():
    return qtile_extras_widget.Mpris2(
        **decoration_group,
        name='spotify',
        foreground=light_pink,
        objname='org.mpris.MediaPlayer2.spotify',
        format='{xesam:title} - {xesam:artist}',
        width=250,
        scroll_interval=0.02,
        stopped_text='',
        paused_text='',
    )


def widget_icon(icon: str):
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
        mouse_callbacks={mouse_left: lambda: qtile.cmd_spawn(terminal + ' -e htop')},
    )


def check_package_updates():
    return qtile_extras_widget.CheckUpdates(
        **decoration_group,
        update_interval=1800,
        distro="Arch_checkupdates",
        display_format="{updates} ",
        no_update_string='󰸞',
        colour_have_updates=warn_pink,
        colour_no_updates=light_pink,
        mouse_callbacks={mouse_left: lambda: qtile.cmd_spawn(terminal + ' -e yay -Syu')},
    )


def disk_free(disk_fmt: str, disk_partition: str):
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
        format="%T",
        foreground=light_pink,
    )


def calendar_widget():
    return qtile_extras_widget.Clock(
        **decoration_group,
        format="%e/%B/%Y",
        foreground=light_pink,
    )


def thermal_sensor():
    return qtile_extras_widget.ThermalZone(
        **decoration_group,
        fgcolor_normal=light_pink,
        high=60,
        crit=85,
        format='{temp}°C',
        format_crit='{temp}°C  ',
        fgcolor_crit=warn_pink,
    )


def drawer(widgets_arr: list):
    return qtile_extras_widget.WidgetBox(
        **decoration_group,
        foreground=light_pink,
        text_open='',
        text_closed=' ',
        widgets=widgets_arr,
    )


def spacer(spacer_width: int):
    return widget.Spacer(
        length=spacer_width
    )


def cpu_widget():
    return qtile_extras_widget.CPU(
        **decoration_group,
        format='{load_percent}%',
        foreground=light_pink,
        width=65
    )


def groupbox_widget():
    return qtile_extras_widget.GroupBox(
        **decoration_group,
        fontsize=14,
        margin_y=3,
        margin_x=5,
        padding_y=1,
        padding_x=5,
        borderwidth=1.1,
        urgent_border=warn_pink,
        urgent_text=warn_pink,
        inactive=purple,
        active=light_pink,
        this_current_screen_border=light_pink,
        this_screen_border=light_pink,
        other_current_screen_border=purple,
        other_screen_border=purple,
        disable_drag=True,
    )


#  ____
# / ___|  ___ _ __ ___  ___ _ __  ___
# \___ \ / __| '__/ _ \/ _ \ '_ \/ __|
#  ___) | (__| | |  __/  __/ | | \__ \
# |____/ \___|_|  \___|\___|_| |_|___/

def screen_widgets(primary=False):
    widgets = [
        spacer(7),
        groupbox_widget(),
        spacer(3),
        widget_icon('󰋋'),
        headset_battery(),
        # widget_icon('󰍽'),
        # mouse_battery(),
        spacer(3),
        notification_widget(),
        spacer(3),
        widget_icon(' '),
        spotify_widget(),
        widget.Spacer(),
        widget_icon('󰥔'),
        system_clock(),
        widget_icon(''),
        calendar_widget(),
        widget.Spacer(),
        widget_icon(''),
        check_package_updates(),
        spacer(3),
        widget_icon(''),
        keyboard_layout(),
        spacer(3),
        widget_icon(''),
        ram_memory(),
        widget_icon(''),
        cpu_widget(),
        widget_icon(''),
        thermal_sensor(),
        spacer(7),
    ]
    if primary:
        widgets.extend([
            qtile_extras_widget.Systray(),
            spacer(7),
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
    Drag([mod], mouse_middle, lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], mouse_right, lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
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
        Match(wm_class="nitrogen"),
        Match(wm_class="pavucontrol"),
        Match(wm_class="steam"),
        Match(wm_class="net.lutris.Lutris"),
        Match(wm_class="battle.net.exe"),
        Match(wm_class="hearthstonedecktracker.exe"),
        Match(wm_class="transmission-qt"),
        Match(wm_class="zoom"),
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ], **default_layout_settings)
# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None
bring_front_click = "floating_only"
floats_kept_above = False
auto_fullscreen = True
follow_mouse_focus = False
cursor_warp = False
focus_on_window_activation = "never"
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

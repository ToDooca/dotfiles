#  ____        _        ____             __ _
# |  _ \ _   _( )___   / ___|___  _ __  / _(_) __ _
# | | | | | | |// __| | |   / _ \| '_ \| |_| |/ _` |
# | |_| | |_| | \__ \ | |__| (_) | | | |  _| | (_| |
# |____/ \__,_| |___/  \____\___/|_| |_|_| |_|\__, |
#                                             |___/

from libqtile import hook
from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

# __     __         _       _     _
# \ \   / /_ _ _ __(_) __ _| |__ | | ___  ___   _
#  \ \ / / _` | '__| |/ _` | '_ \| |/ _ \/ __| (_)
#   \ V / (_| | |  | | (_| | |_) | |  __/\__ \  _
#    \_/ \__,_|_|  |_|\__,_|_.__/|_|\___||___/ (_)
# 

mod = "mod4"
terminal = "alacritty"
browser = "brave"

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
    Key([mod], "w", lazy.spawn(browser),  desc="Launch default browser"),
    Key([mod, "mod1"], "d", lazy.spawn('discord'),  desc="Launch Discord"),
    Key([], "Print", lazy.spawn('flameshot gui'), desc="Take a Screenshot"),
    Key([mod], "e", lazy.spawn('thunar'), desc="Open thunar"),
    Key([mod], "m", lazy.spawn('spotify'), desc="Open spotify floating window"),
]

groups = [
    Group('1', label="main", matches=[Match(wm_class='brave'), Match(wm_class='chrome')], layout="spiral"),
    Group('2', label="", layout="spiral"),
    Group('3', layout="spiral"),
    Group('4', layout="spiral"),
    Group('5', layout="spiral"),
    Group('6', layout="spiral"),
    Group('7', label="", layout="spiral"),
    Group('8', label="", layout="max"),
    Group('9', label="戮", layout="max"),
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

layouts = [
    layout.Max(
        border_focus='#794dce',
        border_normal='#bbaee1',
        border_width=2,
        margin=10
     ),
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
        
    ),
]

widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        bottom=bar.Bar(
            [
                widget.CurrentLayout(),
                widget.GroupBox(),
                widget.Prompt(),
                widget.WindowName(),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.TextBox("default config", name="default"),
                widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
                widget.Systray(),
                widget.Clock(format="%Y-%m-%d %a %I:%M %p"),
                widget.QuickExit(),
            ],
            24,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
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
auto_fullscreen = True
follow_mouse_focus = True
cursor_warp = False
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wmname = "LG3D"

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.Popen([home])

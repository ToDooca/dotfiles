# <p align="center"><font color="darkcyan" >**Du custom dotfiles**</font></p>


## <font color="teal">Dependencies:</font>

- [Qtile](http://www.qtile.org/)
- [qtile-extras](https://github.com/qtile-extras/qtile-extras) (for extended widgets)
- [Alacritty](https://alacritty.org/)
- [Dunst](https://dunst-project.org/)
- [Rofi](https://github.com/davatorium/rofi)
- [Picom](https://wiki.archlinux.org/title/picom)
- [Neovim](https://neovim.io/)
- [Nerd Fonts](https://www.nerdfonts.com/)

## <font color="teal">Description:</font>

This is my custom dotfiles for my Arch based Linux system, but my config files should work on any Linux system as long as you have the required dependencies installed.

As my desktop environment I use qtile, and as my terminal emulator I use alacritty.

Along the files, you will find I use dunst for notifications, rofi for application launching and searching, and picom for compositing.

You will also find that I have a neovim config as well, which I don't use as my main editor, but I'm aspiring to!

### Qtile setup

The Qtile config provides a top bar across 3 screens with a scratchpad for dropdown terminals and apps. Keybind summary (mod = Super/Windows key):

| Keybind | Action |
|---------|--------|
| mod+Return | Terminal |
| mod+d | Rofi drun |
| mod+a | Rofi combi |
| mod+w | Browser |
| mod+Tab | Next layout |
| mod+1..9 | Switch groups |
| mod+alt+n | Toggle notifications |
| mod+m | Spotify dropdown |
| mod+0 | Power/session logout |

**Widgets:** GroupBox, headset battery, mouse battery (Razer), notifications, Spotify/Mpris2, clock, calendar, package updates, keyboard layout, RAM, CPU, thermal sensor. Systray on primary screen only.

**Optional dependencies:** `headsetcontrol` (headset battery), `openrazer` daemon (mouse battery), `playerctl` (media keys), `dunst` (notifications).

**Theme switching:** Set `QTILE_THEME` environment variable (e.g. `purple`) or edit `THEME` in `config.py` to switch themes.

Nerdfont is used for icons in all of my config files, as well as the FiraCode font.

## <font color="teal">Installation:</font>

**Warning:** If you want to give my dotfiles a try, you should first fork this repository, review the code, and remove things you don't want or need. Don't blindly use my settings unless you know what that entails. Use at your own risk!

> **Note**: I do not currently have a script to install my dotfiles, hence I install my dependencies manually, but I will be working on creating one in the future.

## <font color="teal">Screenshots:</font>

> ToDo - Add screenshots

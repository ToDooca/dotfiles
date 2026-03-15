#!/bin/sh
xmodmap ~/.Xmodmap
picom -b &
nitrogen --restore
xfce4-power-manager --daemon

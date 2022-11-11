#!/bin/sh
xrandr --output DVI-D-0 --primary --auto --output HDMI-A-0 --left-of DVI-D-0 --output HDMI-A-1 --right-of DVI-D-0
nitrogen --restore
xfce4-power-manager --daemon

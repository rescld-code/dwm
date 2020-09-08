#!/bin/bash

# AutoStart
compton &
# variety &
fcitx &
feh --bg-scale /home/cy/Pictures/yousa/3D/6.jpg &
# oneko &
# screenkey &

# TIM gnome-settings-daemon
/usr/lib/gsd-xsettings &

# dwm-status-bar
python3 /home/cy/.dwm/autostart/dwm-status.py &

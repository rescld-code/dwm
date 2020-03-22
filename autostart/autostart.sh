#!/bin/bash

# AutoStart
compton &
# variety &
fcitx &
feh --bg-scale /home/cy/Images/54.jpeg &
# oneko &
# screenkey &

# TIM gnome-settings-daemon
/usr/lib/gsd-xsettings &

# dwm-status
/home/cy/.dwm/autostart/dwm-status.sh &

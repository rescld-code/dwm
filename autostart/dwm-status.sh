#!/bin/bash

function get_time() {
	echo "$(date +"%F %R:%S")"
}

function get_chared() {
	battery="$(acpi | awk '{ print $4 }' | grep -Eo '[0-9]+')"
	status="$(acpi | awk '{ print $3 }' | grep -Eo '[a-zA-Z]+')"
	echo Battery: $battery% $status
}

function get_ip() {
	lan="$(ip a | grep 'inet' | grep 'brd' | awk '{ print $2 }')"
	if test "$lan"
	then
		echo IPv4: $lan
	else
		echo no lan
	fi
}

function get_sound() {
	echo Sound: "$(amixer | grep Left: | grep Playback | awk '{ print $5 }' | grep -Eo '[0-9]+')"%
}

while true; do
	status=`get_ip`
	status+=" | "
	status+=`get_sound`
	status+=" | "
	status+=`get_chared`
	status+=" | "
	status+=`get_time`
	xsetroot -name "$status"
	sleep 1
done &

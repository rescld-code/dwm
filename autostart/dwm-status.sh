#!/bin/bash

function get_time() {
	echo "$(date +"%F %R:%S")"
}

function get_chared() {
	echo "$(acpi | awk '{ print $4 }' | grep -Eo '[0-9]+')"
}

function get_ip() {
	echo "$(ip a | grep 'inet' | grep 'brd' | awk '{ print $2 }')"
}

function get_sound() {
	echo "$(amixer | grep Left: | grep Playback | awk '{ print $5 }' | grep -Eo '[0-9]+')"
}

while true; do
	status='ip: '
	status+=`get_ip`
	status+=" | Sound: "
	status+=`get_sound`
	status+="% | Battery: "
	status+=`get_chared`
	status+="% | "
	status+=`get_time`
	xsetroot -name "$status"
	sleep 1
done &

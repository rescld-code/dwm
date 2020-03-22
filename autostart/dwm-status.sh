#!/bin/bash

function get_time() {
	echo "$(date +"%F %R:%S")"
}

function get_chared() {
	echo "$(acpi)"
}

function get_ip() {
	echo "$(ip a | grep 'inet' | grep 'brd' | awk '{ print $2 }')"
}

while true; do
	status='ip: '
	status+=`get_ip`
	status+=" | "
	status+=`get_chared`
	status+=" | "
	status+=`get_time`
	xsetroot -name "$status"
	sleep 1
done &

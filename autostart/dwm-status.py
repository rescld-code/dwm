#!/usr/bin/env python
# coding=utf-8

import re
import os
import time
import datetime
import threading

ip = ""  # IPv4地址

date = ""  # 系统时间
countDown = 0 # 考试倒计时

battery = ""  # 系统电量
batteryStatus = ""  # 充电状态
batteryWarned = False  # 是否已经提醒
batteryWarning = False  # 电量是否过低

soundLeft = ""   # 左声道音量
soundRight = ""  # 右声道音量
soundStatus = ""  # 音量状态

backLight = 50  # 笔记本屏幕亮度


class Bar(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def CountDown(self):
        # 学考倒计时
        global countDown
        s = datetime.date.today()
        t = datetime.date(2020, 6, 20)
        countDown = str(t.__sub__(s)).split(' ')[0]

    def getTime(self):
        # 获取时间
        global date
        date = time.strftime("%Y-%m-%d %a %H:%M:%S", time.localtime())

    def notice(self):
        # 发出提示
        global batteryStatus
        global batteryWarned
        global batteryWarning
        if batteryWarning == True and batteryWarned == False:
            batteryWarned = True
            os.system("st -e ~/.dwm/autostart/notice 电量不足....")
        elif batteryWarning == False:
            batteryWarned = False

    def getBattery(self):
        # 获取电量与状态
        global battery
        global batteryWarning
        global batteryStatus
        status = os.popen("acpi").read().split(' ')[2]
        if status == 'Not':
            battery = os.popen("acpi").read().split(' ')[4].split('\n')[0]
            batteryStatus = os.popen("acpi").read().split(' ')[3].split(',')[0]
        else:
            battery = os.popen("acpi").read().split(' ')[3].split(',')[0]
            batteryStatus = os.popen("acpi").read().split(' ')[2].split(',')[0]

        if int(battery.split('%')[0]) < 20 and batteryStatus == 'Discharging':
            batteryWarning = True
        else:
            batteryWarning = False

    def getSound(self):
        # 获取系统音量与状态
        global soundLeft
        global soundRight
        global soundStatus
        soundLeft = re.search(
            r'[0-9%]+', os.popen("amixer").read().split('\n')[5].split(' ')[6]).group()
        soundRight = re.search(
            r'[0-9%]+', os.popen("amixer").read().split('\n')[6].split(' ')[6]).group()
        soundStatus = re.search(
            r'[a-z]+', os.popen("amixer").read().split('\n')[6].split(' ')[7]).group()

    def getIP(self):
        # 获取ip地址
        global ip
        address = os.popen(
            "ip a | grep 'inet' | grep 'brd' | awk '{ print $2 }'").read().split('\n')[0]
        if address == "":
            ip = "no lan"
        else:
            ip = address

    def getBackLight(self):
        # 获取笔记本屏幕背光
        global backLight
        backLight = os.popen("xbacklight -get").read().split('\n')[0]

    def run(self):
        self.getIP()
        self.notice()
        self.getTime()
        self.getSound()
        self.CountDown()
        self.getBattery()
        self.getBackLight()


while True:
    # 线程获取数据
    data = Bar()
    data.start()

    # 状态条
    bar = "学考倒计时: {} days".format(countDown)
    bar += " | IP: {}".format(ip)
    bar += " | Sound: {} {} {}".format(soundLeft, soundRight, soundStatus)
    bar += " | Light: {}".format(backLight)
    bar += " | Battery: {} {}".format(battery, batteryStatus)
    bar += " | {}".format(date)

    os.system("xsetroot -name \"" + bar + "\"")

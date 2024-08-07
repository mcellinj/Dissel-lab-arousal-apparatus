# imports
import board
import busio 
import adafruit_drv2605
import time
import os
import subprocess
import shlex
from subprocess import Popen
import datetime

import RPi.GPIO as GPIO

#init LED
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)

# init I2C bus amd DRV2605 module
i2c = busio.I2C(board.SCL, board.SDA)
drv = adafruit_drv2605.DRV2605(i2c, address = 0x5a)

x = datetime.datetime.now()

today = (x.strftime("%m") + "-" + x.strftime("%d") + "-" + x.strftime("%Y"))

#subprocess.call(['sh', './checkTime.sh'])

# ask for user input
delayLen = input("length of delay before start of cycles (min): ")
#videoLen = input("length of video (minutes, minimum 10): ")
#while int(videoLen) < 0:
#   videoLen = input("length of video (in minutes, minimum 10): ")
#videoBreak = input("length of break betweeen vids: ")
#cycles = input("num of cycles: ")
videoLen = 22
videoBreak = 38
cycles = 7
# user input compatibility

# seconds to min
delayLen = int(delayLen)*60
# millisecond to minutes
videoLen = int(videoLen)*60000
# to minutes
videoBreak = int(videoBreak)*60
cycles = int(cycles)
#print(videoLen)

# create command for subprocess
cmd = "./vid.sh "  + str(videoLen) + " " + today

# delay
time.sleep(delayLen)

# this will loop desired num of times
for i in range(cycles):
#subprocess.call(shlex.split(f"./vid.sh {videoLen}"))
#os.system("raspivid -o "Videos/video_$currDT.h264" -t ${videoLen}")

    # subprocess
    p = Popen([cmd], shell=True, stdin=None, stdout=None, stderr=None, close_fds=True)

    # break before motor starts
    time.sleep(600)

    # start motoreffect
    effect_id = 62
    buzz = True
    
    # motor sequence
    while buzz:
        #turn on LED
        GPIO.output(18, GPIO.HIGH)
        
        #motor seq
        drv.sequence[0] = adafruit_drv2605.Effect(effect_id)
        drv.sequence[1] = adafruit_drv2605.Pause(0.8)
        drv.sequence[2] = adafruit_drv2605.Effect(effect_id)
        drv.sequence[3] = adafruit_drv2605.Pause(0.8)
        drv.sequence[4] = adafruit_drv2605.Effect(effect_id)
        drv.sequence[5] = adafruit_drv2605.Pause(0.8)
        drv.sequence[6] = adafruit_drv2605.Effect(effect_id)
        drv.sequence[7] = adafruit_drv2605.Effect(effect_id)
        drv.play()
        time.sleep(15)
        drv.stop()
    #if effect_id == 66:
     #   os.system("raspivid -o "Videos/video_$currDT.h264" -t $lenVid")
        if effect_id == 58:
            buzz = False
        
        effect_id -= 1
    
    #turn off LED
    GPIO.output(18, GPIO.LOW)
    
    #wait for subprocess to finish
    p.communicate()
    
    # run break between cycles if it isnt the last cycle
    if i+1 != cycles:
        time.sleep(videoBreak)
        #print(i)
#time.sleep(videoBreak)

#!


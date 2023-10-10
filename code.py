import time
from adafruit_servokit import ServoKit 

#config
NumControllers = 1
NumMotorsSupportedPer = 8

#initialize
kit = []
for i in range(0, NumControllers):
    kit.append(ServoKit(channels=NumMotorsSupportedPer, address=(0x40+i)))
    for j in range(0, NumMotorsSupportedPer): 
        kit[i].servo[j].set_pulse_width_range(500,2400)   

#test all servos 0 - 7
kit[0].servo[0].angle = 0
kit[0].servo[1].angle = 0
kit[0].servo[2].angle = 0
kit[0].servo[3].angle = 0
kit[0].servo[4].angle = 0
kit[0].servo[5].angle = 0
kit[0].servo[6].angle = 0
kit[0].servo[7].angle = 0
time.sleep(1)
kit[0].servo[0].angle = 180
kit[0].servo[1].angle = 180
kit[0].servo[2].angle = 180
kit[0].servo[3].angle = 180
kit[0].servo[4].angle = 180
kit[0].servo[5].angle = 180
kit[0].servo[6].angle = 180
kit[0].servo[7].angle = 180
time.sleep(1)
kit[0].servo[0].angle = 90
kit[0].servo[1].angle = 90
kit[0].servo[2].angle = 90
kit[0].servo[3].angle = 90
kit[0].servo[4].angle = 90
kit[0].servo[5].angle = 90
kit[0].servo[6].angle = 90
kit[0].servo[7].angle = 90
time.sleep(1)
kit[0].servo[0].angle = 0
kit[0].servo[1].angle = 0
kit[0].servo[2].angle = 0
kit[0].servo[3].angle = 0
kit[0].servo[4].angle = 0
kit[0].servo[5].angle = 0
kit[0].servo[6].angle = 0
kit[0].servo[7].angle = 0
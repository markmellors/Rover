
from approxeng.input.selectbinder import ControllerResource
from time import sleep
import math

from adafruit_motorkit import MotorKit
drive = MotorKit()
frontright = drive.motor2
frontleft = drive.motor1
rearright = drive.motor4
rearleft = drive.motor3



def strafing(x, y, w):

    FL = x - y - w
    FR = x + y - w
    RL = x - y + w
    RR = x + y + w
    
    maximum = max(abs(FL), abs(FR), abs(RL), abs(RR))
    if maximum > 1:
        FL = FL/maximum
        FR = FR/maximum
        RL = RL/maximum
        RR = RR/maximum
 
    return FL, FR, RL, RR 
    

while True:
    try:
        with ControllerResource() as joystick:
            print('Found a joystick and connected')
            while joystick.connected:                
                x, y = joystick['rx','ry']
                w = joystick['lx']
                FL, FR, RL, RR = strafing(x, y, w)
                frontleft.throttle = -FL
                frontright.throttle = FR
                rearleft.throttle = -RL
                rearright.throttle = RR

        # Joystick disconnected...
        print('Connection to joystick lost')
    except IOError:
        # No joystick found, wait for a bit before trying again
        print('Unable to find any joysticks')
        sleep(0.1)
    except Exception as inst:
        print(type(inst))    # the exception instance
        print(inst.args)     # arguments stored in .args
        print(inst)          # __str__ allows args to be printed directly,
#                             # but may be overridden in exception subclasses
#        x, y = inst.args     # unpack args
#        print('x =', x)
#        print('y =', y)
#        sleep(1.0)

import time
from digitalio import DigitalInOut, Direction
import board
import usb_cdc
from boot import *
# For seeed xiao on-board LED
led = DigitalInOut(board.IO21)
led.direction = Direction.OUTPUT
led.value = True

# establish USB CDC
serial = usb_cdc.console
in_data = bytearray()
out_data = bytearray()
serial.timeout = 1
# If timeout is None, readlines() will never return, because there is no way to indicate end of stream.


'''
functions!!
'''
class Actions:
    def act(self, action, param):
        if hasattr(self, 'case_' + str(action)):
            return getattr(self, 'case_' + str(action))(param)
        else:
            print('Error: Unknown action')
    
    def case_blink(self, param):
        led.value = False
        time.sleep(float(param))
        led.value = True


    def case_spec(self, param=None):
        sensor.led_current = int(param) # set LED current using the input argument
        time.sleep(1) # let it illuminate for 1 second
        # read the sensor data
        data = { 
            '415': sensor.channel_415nm,
            '445': sensor.channel_445nm,
            '480': sensor.channel_480nm,
            '515': sensor.channel_515nm,
            '555': sensor.channel_555nm,
            '590': sensor.channel_590nm,
            '630': sensor.channel_630nm,
            '680': sensor.channel_680nm,
        }
        print(data) # print the sensor data via serial back to science jubilee
        sensor.led_current = 0 #turn off LED


action = Actions()

'''
loop!
'''
while True:
    if serial.in_waiting > 0:
        line = serial.readline()
        data = str(line, 'UTF-8').strip()
        arguments = data.split(',')
        if len(arguments) == 2:
            header, param = arguments
            action.act(header, param)
        

        elif line == b'\r':
            continue

        else: 
            print('Error: wrong arguments')
            continue
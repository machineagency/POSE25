import pwmio
import busio
import board
from adafruit_as7341 import AS7341

def initialize_peripherals():
    i2c = busio.I2C(board.IO6, board.IO5)
    sensor = AS7341(i2c)
    return sensor

# Initialize
sensor = initialize_peripherals()
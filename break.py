import serial
import time
import sys

port = '/dev/tty.SLAB_USBtoUART'
ser = serial.Serial(port, 115200)
ser.write(b'\x1b')
time.sleep(0.1)
ser.close()

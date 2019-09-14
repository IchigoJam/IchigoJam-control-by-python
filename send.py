import serial
import time
import sys

port = '/dev/tty.SLAB_USBtoUART'
ser = serial.Serial(port, 115200)
ser.write(sys.argv[1].encode('utf-8'))
ser.write(b'\x0a')
time.sleep(0.1)
ser.close()

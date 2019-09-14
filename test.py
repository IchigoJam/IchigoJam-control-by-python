import serial
import time

port = '/dev/tty.SLAB_USBtoUART'
ser = serial.Serial(port, 115200)
ser.write(b'LED1\n')
time.sleep(0.1)
ser.close()

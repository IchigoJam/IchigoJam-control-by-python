import serial
import time

port = '/dev/tty.SLAB_USBtoUART'
ser = serial.Serial(port, 115200)
ser.write(b'?ANA(2)*32/10-500\n')
print(ser.readline())
time.sleep(0.1)
ser.close()

import serial
import time

port = '/dev/tty.SLAB_USBtoUART'
#ser = serial.Serial(port, 115200, rtscts=False, dsrdtr=False)
ser = serial.Serial()
ser.port = port
ser.baudrate = 115200
ser.timeout = 1
ser.setDTR(False)
ser.open()

ser.write(b'LED1\n')
time.sleep(0.1)
ser.close()

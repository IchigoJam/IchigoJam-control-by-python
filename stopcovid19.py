import serial
import time
import requests

url = ''
txt = requests.get('https://www.stopcovid19.jp/data/covid19japan-trend.txt')
data = txt.text.split('\n')
print(data)

port = '/dev/tty.SLAB_USBtoUART'
ser = serial.Serial()
ser.port = port
ser.baudrate = 115200
ser.timeout = 1
ser.setDTR(False)
ser.open()

def locate(x, y):
  ser.write(b'\x15')
  ser.write(chr(32 + x).encode())
  ser.write(chr(32 + y).encode())

ser.write(b'\x13\x0c')
locate(2, 2)
ser.write(b'COVID19 ')
for i in range(1, int(data[0]), 3):
  print(i, data[i])
  pref = data[i].encode()
  cur = data[i + 1].encode()
  
  dcur = data[i + 2]
  if (not dcur.startswith('-') and not dcur == '0'):
    dcur = '+' + dcur
  dcur = dcur.rjust(4, ' ')
  dcur = dcur.encode()

  n = i // 3 + 2
  div = 7
  x = n % div * 4 + 2
  y = n // div * 3 + 2
  locate(x, y)
  ser.write(pref)
  locate(x - 1, y + 1)
  ser.write(dcur)
  time.sleep(0.5)

ser.close()

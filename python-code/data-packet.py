import serial
import datetime
import time

#port = serial.Serial('/dev/ttyS0', baudrate=9600, timeout=2.0)

def read_pm_line(_port):
    rv = b''
    while True:
        ch1 = _port.read()
        if ch1 == b'\x42':
            ch2 = _port.read()
            if ch2 == b'\x4d':
                rv += ch1 + ch2
                rv += _port.read(28)
                return rv

with serial.Serial('/dev/ttyS0', baudrate=9600, timeout=2.0) as port:
    rcv = read_pm_line(port)
    print(rcv)
    print(type(rcv))
    res = {'timestamp': datetime.datetime.now(),
           'apm10': rcv[4] * 256 + rcv[5],
           'apm25': rcv[6] * 256 + rcv[7],
           'apm100': rcv[8] * 256 + rcv[9],
           'pm10': rcv[10] * 256 + rcv[11],
           'pm25': rcv[12] * 256 + rcv[13],
           'pm100': rcv[14] * 256 + rcv[15]
           }
    print('==============\n'
            'PM2.5: {}\n'
            'PM10:  {}\n'.format(res['apm25'], res['apm100']))
    print(res)

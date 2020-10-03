import serial
import datetime
import time

#port = serial.Serial('/dev/ttyS0', baudrate=9600, timeout=2.0)

""" Class to handle UART transactions from the PMS5003 sensor """
class PMS5003:

    """ Initializes sensor using string com_port """
    def __init__(self, com_port):
        self.ser = serial.Serial(com_port, baudrate=9600, timeout=2.0)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.ser.close()

    def read_packet(self):
        rv = b''
        while True:
            ch1 = self.ser.read()
            if ch1 == b'\x42':
                ch2 = self.ser.read()
                if ch2 == b'\x4d':
                    rv += ch1 + ch2
                    rv += self.ser.read(28)
                    return rv

with PMS5003('/dev/ttyS0') as sensor:
    rcv = sensor.read_packet()
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
    print(type(res['apm25']))

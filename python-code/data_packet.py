import time
import datetime

class DataPacket:

    """ Accepts a byte buffer (as returned by PMS5003.read_data()) and 
    parses into member variables containing values. Based heavily on 
    IOCT.tech's PMS5003 how-to """
    def __init__(self, buff):
        self.timestamp = datetime.datetime.now()
        self.apm10 =  buff[4]  * 256 + buff[5]
        self.apm25 =  buff[6]  * 256 + buff[7]
        self.apm100 = buff[8]  * 256 + buff[9]
        self.pm10 =   buff[10] * 256 + buff[11]
        self.pm25 =   buff[12] * 256 + buff[13]
        self.pm100 =  buff[14] * 256 + buff[24]
    
    def __str__(self):
        return ('Timestamp                : {}\n'
                'PM1.0, ug/m3, standard   : {}\n'
                'PM2.5, ug/m3, standard   : {}\n'
                'PM10,  ug/m3, standard   : {}\n'
                'PM1.0, ug/m3, atmospheric: {}\n'
                'PM2.5, ug/m3, atmospheric: {}\n'
                'PM10,  ug/m3, atmospheric: {}\n').format(self.amp10,
                                                          self.apm25,
                                                          self.apm100,
                                                          self.pm10,
                                                          self.pm25,
                                                          self.pm100)



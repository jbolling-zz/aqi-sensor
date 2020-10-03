from pms5003 import *
from data_packet import *
import time

with PMS5003("/dev/ttyS0") as sensor:
    packet = DataPacket(sensor.read_packet())
    print(packet)


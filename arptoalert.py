#!/usr/bin/env python3
import pandas as pd
import numpy as np
import codecs
import os
import datetime

alert= pd.read_csv('/home/alert')
#read alerts
arp=pd.read_csv('/home/arp')
#read arp+ip from core arp table

alert['switch']=alert['ip']


for i in range (0, len(alert)):
    q=arp.loc[arp['mac']==alert['hex-full'].loc[i]].index.values
    #print(q)
    #hist['ip'].loc[i]=arp['ip'].loc[q]
    #print(arp['ip'].iloc[q].values)
    alert['ip'].loc[i]=arp['ip'].loc[q].values
    #print(arp['ip'].loc[q].values)
    #print(alert['ip'].loc[i])

#if mac in alert_file is in arp table , save ip from arp_file to alert_file 

html=alert.to_html()
text_file = open("/home/alertarp.html", "w")
text_file.write(html)
text_file.close()

alert.to_csv(r"/home/alertarp", index=False)


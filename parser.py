#!/usr/bin/env python3

import pandas as pd
import numpy as np
import codecs
import os
import datetime

#collecting data from switches to files
snmp='/home/snmpcollect'
os.system(snmp)
#function takes data from files,  adding producer and timestamp
def fun1(file1, file2):

	directory='/home/switches'
	files=os.listdir(directory)

	data=open(r"/home/switches/" + file1)
	macs=data.readlines()
	data.close()

	data=open(r"//home/switches/" + file2)
	ports=data.readlines()
	data.close()

	data=codecs.open("/usr/lib/zabbix/externalscripts/oui.txt", "r", "utf-8")
	oui=data.readlines()
	data.close()

	macs=pd.DataFrame(data=macs)
	ports=pd.DataFrame(data=ports)
	oui=pd.DataFrame(data=oui)
	oui.columns=['values']
	oui=oui[oui['values'].str.contains("hex")]
	oui_new=oui['values'].str.split('hex', expand=True)
	oui_new=oui_new.drop(2, axis=1)
	oui_new.columns=['mac', 'producer']
	oui_new.mac=oui_new.mac.str.replace("(", "")
	oui_new.mac=oui_new.mac.str.replace(" ", "")
	oui_new.producer=oui_new.producer.str.replace(")", "")
	oui_new.producer=oui_new.producer.str.replace("\\t", "")
	oui_new.producer=oui_new.producer.str.replace("\\r", "")
	oui_new.producer=oui_new.producer.str.replace("\\n", "")
	oui_new.producer=oui_new.producer.astype(str)
	oui_new=oui_new.reset_index(drop=True)
	macs.columns=['values']
	ports.columns=['values']
	macs_new=macs['values'].str.split(': ', expand=True)
	macs_new.columns=['mibm', 'hex']
	ports_new=ports['values'].str.split(': ', expand=True)
	ports_new.columns=['mibp', 'port']

	final=pd.concat([ports_new, macs_new], axis=1)
	final=final.drop('mibm', axis=1).drop('mibp', axis=1)

	final['hex']=final['hex'].astype(str)
	final.port=final.port.str.replace("\\n", "")
	final.hex=final.hex.str.replace("\\n", "")
	final.hex=final.hex.str.replace(" ", "-")
	final.port.fillna(0, inplace=True)
	final['port']=final.port.astype(str).astype(int)
	final=final.sort_values('port')
	final=final.reset_index(drop=True)
	final['producer']='text'
	final['hex-full']=final['hex']

	for i in range(0, len(final)):
	    final.loc[i, 'hex']=final.loc[i, 'hex'][0:8]

	i=0
	while i<len(final.index):
	    final.producer.loc[i]=str(oui_new[oui_new['mac'].str.contains(final.hex.loc[i])].producer)
	    final.producer.loc[i]=final.producer.loc[i][7:].replace("Name: producer, dtype: object", "")
	    final.producer.loc[i]=final.producer.loc[i].replace("\n", "")
	    i=i+1

	final['ip']='172.31.' + file1[0:6]
	now=datetime.datetime.now()
	final['datetime']=now.strftime("%d-%m-%Y %H:%M")
	#final['datetime']=now.ctime()
	final2=final[['port', 'hex-full', 'producer', 'ip', 'datetime']]
	final2.to_csv(r"/home/" + file1[0:6] + "-final", index=False)


fun1('130.16-m', '130.16-p')
fun1('130.17-m', '130.17-p')
fun1('130.18-m', '130.18-p')
fun1('130.19-m', '130.19-p')
fun1('130.20-m', '130.20-p')
fun1('130.21-m', '130.21-p')
fun1('130.22-m', '130.22-p')

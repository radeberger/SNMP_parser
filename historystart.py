#!/usr/bin/env python3

import pandas as pd
import numpy as np
import codecs
import os
import datetime


f13016 = pd.read_csv('/home/130.16-final')
f13017 = pd.read_csv('/home/130.17-final')
f13018 = pd.read_csv('/home/130.18-final')
f13019 = pd.read_csv('/home/130.19-final')
f13020 = pd.read_csv('/home/130.20-final')
f13021 = pd.read_csv('/home/130.21-final')
f13022 = pd.read_csv('/home/130.22-final')

historystart=pd.concat([f13016, f13017, f13018, f13019, f13020, f13021, f13022], axis=0).reset_index(drop=True)

historystart.to_csv(r"/home/historystart", index=False)

#file  to start history 

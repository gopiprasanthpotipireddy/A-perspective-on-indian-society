# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import os
file_path="./data/DS0002"
hh_path=os.path.join(file_path,"36151-0002-Data.tsv")
hh_data=pd.read_csv(hh_path,sep='\t')

#ID13 SG
#ID11 RG

for i in hh_data.ID13.unique():
    hh_data.loc[hh_data.ID13 ==i, 'ID13'] = str(i)

hh_data.ID13.unique()

for i in hh_data.TR4A.unique():
    hh_data.loc[hh_data.TR4A ==i, 'TR4A'] = str(i)

hh_data.TR4A.unique()
for c in ['A','B','C','D','E','F','G','H','I','J','K']:
    for i in ['1','0']:
        hh_data.loc[hh_data['SN2'+c+'1'] ==i, 'SN2'+c+'1'] = int(i)

for c in ['A','B','C','D','E','F','G','H','I','J','K']:
    for i in ['1','0']:
        hh_data.loc[hh_data['SN2'+c+'2'] ==i, 'SN2'+c+'2'] = int(i)
    
for c in ['A','B','C','D','E','F','G','H','I','J','K']:
    print (hh_data['SN2'+c+'1'].unique())
    print (hh_data['SN2'+c+'2'].unique())

SN=[]
SN_IN=[]
SN_OUT=[]
for c in ['A','B','C','D','E','F','G','H','I','J','K']:
    SN.append('SN2'+c+'1')
    SN.append('SN2'+c+'2')
SN.append('ID13')
SN.append('TR4A')
SN.sort()
for c in ['A','B','C','D','E','F','G','H','I','J','K']:
    SN_OUT.append('SN2'+c+'2')

for c in ['A','B','C','D','E','F','G','H','I','J','K']:
    SN_IN.append('SN2'+c+'1')

SG_SN_data=hh_data[SN]

for c in ['A','B','C','D','E','F','G','H','I','J','K']:
        SG_SN_data.loc[SG_SN_data['SN2'+c+'1'] ==' ', 'SN2'+c+'1'] = 0
        SG_SN_data.loc[SG_SN_data['SN2'+c+'2'] ==' ', 'SN2'+c+'2'] = 0

SG_SN_data['WITHIN_NETWORK']=SG_SN_data[SN_IN].sum(axis=1)
SG_SN_data['OUTSIDE_NETWORK']=SG_SN_data[SN_OUT].sum(axis=1)

#SN_Practice=SG_SN_data.loc[SG_SN_data.TR4A=='1',:]
SG_SN_data.groupby(['TR4A']).sum()
SG_SN_data.groupby(['TR4A']).mean()

ax=sns.factorplot(x='TR4A', y='WITHIN_NETWORK', data=SG_SN_data,kind='box')

sns.factorplot(x='TR4A', y='OUTSIDE_NETWORK', data=SG_SN_data,kind='box')


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

SG_SN_data=hh_data[SN]


#SOCIAL Groups and Network Size.
for c in ['A','B','C','D','E','F','G','H','I','J','K']:
        SG_SN_data.loc[SG_SN_data['SN2'+c+'1'] ==' ', 'SN2'+c+'1'] = 0
        SG_SN_data.loc[SG_SN_data['SN2'+c+'2'] ==' ', 'SN2'+c+'2'] = 0

for c in ['A','B','C','D','E','F','G','H','I','J','K']:
        print (SG_SN_data['SN2'+c+'1'].unique())
        print (SG_SN_data['SN2'+c+'2'].unique())

for c in ['A','B','C','D','E','F','G','H','I','J','K']:
    SN_OUT.append('SN2'+c+'2')

for c in ['A','B','C','D','E','F','G','H','I','J','K']:
    SN_IN.append('SN2'+c+'1')
SG_SN_data['WITHIN_NETWORK']=SG_SN_data[SN_IN].sum(axis=1)
SG_SN_data['OUTSIDE_NETWORK']=SG_SN_data[SN_OUT].sum(axis=1)

SN_MEANS=pd.DataFrame(SG_SN_data.groupby(['ID13']).mean())
SN_MEANS['ID13']=[' ','1','2','3','4','5','6']

SN_MEANS=pd.melt(SN_MEANS, id_vars="ID13", var_name="NETWORK", value_name="SIZE")
ax=sns.factorplot(x='ID13', y='SIZE',hue='NETWORK', data=SN_MEANS,kind='bar').savefig('SG_NETWORK.jpg')


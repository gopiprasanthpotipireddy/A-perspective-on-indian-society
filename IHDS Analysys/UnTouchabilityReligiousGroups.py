# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 17:53:30 2019

@author: gopiprasanthp
"""

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import os
file_path="./data/DS0002"
hh_path=os.path.join(file_path,"36151-0002-Data.tsv")
hh_data=pd.read_csv(hh_path,sep='\t')

#Data Pre Processing
for i in hh_data.ID11.unique():
    hh_data.loc [hh_data.ID11 ==i, 'ID11'] = str(i)
                    

for i in hh_data.TR4A.unique():
    hh_data.loc[hh_data.TR4A ==i, 'TR4A'] = str(i)

#TR4A  HOUSEHOLDS PRACTICING[YES/NO]
#TR4B problem if someone who is scheduled caste were to enter your kitchen or share utensils [YES/NO]
#TR4C HOUSEHOLDS EXPERIENCED[YES/NO]

hh_religious_yes=hh_data.loc[hh_data['TR4A']=='1',['ID11','TR4A']]

hh_data.groupby(['ID11']).size().reset_index(name='total')

hh_religious_groups=hh_data.groupby(['ID11','TR4A']).size()

rg_un_practice=hh_religious_groups.groupby(level=0).apply(lambda x:100 * x / float(x.sum())).reset_index(name='Percentage')

rg_un_practice=rg_un_practice.loc[rg_un_practice.TR4A=='1',:]

rg_un_practice['RG']=['Hindu','Muslim','Christian','Sikh','Buddhist','Jain','Tribal','Others']

#plotting social groups practicing untouchability
ax=sns.barplot(x='RG', y='Percentage', data=rg_un_practice,palette="Blues",errwidth=100)




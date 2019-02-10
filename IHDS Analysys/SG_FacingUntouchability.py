# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 13:35:28 2019

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


#TR4A  HOUSEHOLDS PRACTICING[YES/NO]
#TR4B problem if someone who is scheduled caste were to enter your kitchen or share utensils [YES/NO]
#TR4C HOUSEHOLDS EXPERIENCED[YES/NO]

sg_faced_yes=hh_data.loc[hh_data['TR4C']=='1',['ID13','TR4C']]

hh_data.groupby(['ID13']).size().reset_index(name='total')

sg_faced_groups=hh_data.groupby(['ID13','TR4C']).size().reset_index(name='counts')

sg_faced_groups=hh_data.groupby(['ID13','TR4C']).size()

sg_faced=sg_faced_groups.groupby(level=0).apply(lambda x:100 * x / float(x.sum())).reset_index(name='Percentage')

#sg_un_practice=sg_un_practice.loc[sg_un_practice.TR4A=='1',:]
#household percentage practicing untouchability 
untouchability_percentage= (hh_data.loc[hh_data['TR4A']=='1',:].shape[0])/(hh_data.shape[0])*100

sg_faced['SocialGroup']=["Not Mentioned","Brahmin","Forward/General (except Brahmin)","Other Backward Castes"," Scheduled Castes"," Scheduled Tribes","Others"]
sg_faced.columns=['SocialGroup','FacedUntouchability','Percentage']
#plotting social groups practicing untouchability
ax=sns.barplot(x='SocialGroup', y='Percentage', data=sg_faced,hue='FacedUntouchability',errwidth=100)


#Religious and SocialGroups Facing Untouchability

Rs_UnTochability=hh_data.groupby(['ID11','ID13','TR4A']).size()
Rs_Practice=Rs_UnTochability.groupby(level=0).apply(lambda x:100 * x / float(x.sum())).reset_index(name='Percentage')

Rs_Practice=Rs_Practice.loc[Rs_Practice.TR4A=='1',:]
ax=sns.barplot(x='ID11', y='Percentage', data=Rs_Practice,hue='ID13')

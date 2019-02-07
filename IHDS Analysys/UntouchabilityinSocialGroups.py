# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 11:19:50 2019

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

#Data PreProcessing

for i in hh_data.ID13.unique():
    hh_data.loc[hh_data.ID13 ==i, 'ID13'] = str(i)

hh_data.ID13.unique()

for i in hh_data.TR4A.unique():
    hh_data.loc[hh_data.TR4A ==i, 'TR4A'] = str(i)

hh_data.TR4A.unique()

#TR4A  HOUSEHOLDS PRACTICING[YES/NO]
#TR4B problem if someone who is scheduled caste were to enter your kitchen or share utensils [YES/NO]
#TR4C HOUSEHOLDS EXPERIENCED[YES/NO]

hh_social_yes=hh_data.loc[hh_data['TR4A']=='1',['ID13','TR4A']]

hh_data.groupby(['ID13']).size().reset_index(name='total')

hh_social_groups=hh_data.groupby(['ID13','TR4A']).size().reset_index(name='counts')

sg_un_practice=hh_social_groups.groupby(level=0).apply(lambda x:100 * x / float(x.sum())).reset_index(name='Percentage')

sg_un_practice=sg_un_practice.loc[sg_un_practice.TR4A=='1',:]
#household percentage practicing untouchability 
untouchability_percentage= (hh_data.loc[hh_data['TR4A']=='1',:].shape[0])/(hh_data.shape[0])*100

sg_un_practice['SocialGroup']=["Not Mentioned","Brahmin","Forward/General (except Brahmin)","Other Backward Castes"," Scheduled Castes"," Scheduled Tribes","Others"]
#plotting social groups practicing untouchability
ax=sns.barplot(x='SocialGroup', y='Percentage', data=sg_un_practice,palette="Blues",errwidth=100)

def plot_bar_x():
    # this is for plotting purpose
    index = np.arange(len(sg_un_practice))
    plt.bar(index, sg_un_practice.Percentage)
    plt.xlabel('SocialGroup', fontsize=10)
    plt.ylabel('Percentage', fontsize=10)
    plt.xticks(index, sg_un_practice['SocialGroup'], fontsize=10,rotation=90)
    plt.title('Social Groups Practicing UnTouchability')
    plt.show()
    

plot_bar_x()

# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 11:19:50 2019

@author: gopiprasanthp
"""
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import os
file_path="C:/Users/gopiprasanthp/Desktop/MyWork/ihds/ICPSR_36151/DS0002"
hh_path=os.path.join(file_path,"36151-0002-Data.tsv")
hh_data=pd.read_csv(hh_path,sep='\t')

#TR4A  HOUSEHOLDS PRACTICING[YES/NO]
#TR4B problem if someone who is scheduled caste were to enter your kitchen or share utensils [YES/NO]
#TR4C HOUSEHOLDS EXPERIENCED[YES/NO]
hh_data.ID13
hh_data['ID13']=hh_data['ID13'].astype('category')
hh_data['ID13']
#EXTRACT Only TR4A=YES
hh_social_yes=hh_data.loc[hh_data['TR4A']=='1',['ID13','TR4A']]

plt.hist(hh_social_yes.ID13,label="rgeg")

plt.hist()
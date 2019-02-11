# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 18:32:38 2019

@author: gopiprasanthp
"""

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


#TR4A  HOUSEHOLDS PRACTICING[YES/NO]
#TR4B problem if someone who is scheduled caste were to enter your kitchen or share utensils [YES/NO]
#TR4C HOUSEHOLDS EXPERIENCED[YES/NO]

hh_economic_yes=hh_data.loc[hh_data['TR4A']=='1',['INCOME','TR4A']]
for i in hh_data.ID13.unique():
    hh_data.loc[hh_data.ID13 ==i, 'ID13'] = str(i)

hh_data.ID13.unique()

for i in hh_data.TR4C.unique():
    hh_data.loc[hh_data.TR4C ==i, 'TR4C'] = str(i)

hh_data.TR4C.unique()


hh_data.groupby(['INCCLASS']).size().reset_index(name='total')

hh_economic_groups=hh_data.groupby(['INCCLASS','TR4A']).size()

eg_un_practice=hh_economic_groups.groupby(level=0).apply(lambda x:100 * x / float(x.sum())).reset_index(name='Percentage')

eg_un_practice=eg_un_practice.loc[eg_un_practice.TR4A=='1',:]


#plotting social groups practicing untouchability
ax=sns.barplot(x='INCCLASS', y='Percentage', data=eg_un_practice,palette="Blues").savefig('EG_UNTOUCHABILITY.jpg')

def plot_bar_x():
    # this is for plotting purpose
    #index = np.arange(len(sg_un_practice))
    plt.bar(eg_un_practice['INCCLASS'], eg_un_practice.Percentage)
    plt.xlabel('Economic Group(RS)', fontsize=10)
    plt.ylabel('Percentage', fontsize=10)
    #plt.xticks(index, sg_un_practice['SocialGroup'], fontsize=10,rotation=90)
    plt.title('Economic Groups Practicing UnTouchability')
    plt.legend(['Rich:>=1700000\n'
                'Middle Class:<1700000 & >=340000\n'
                'Aspirers:<340000 & >=150000\n'
                'Poor:<150000'])
    plt.show()
    

plot_bar_x()


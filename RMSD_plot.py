#!/usr/bin/env python
# coding: utf-8

# In[2]:


from re import T
import pandas as pd
import numpy as np


# In[3]:


df = pd.read_csv('rmsd.xvg', skiprows=18, delimiter="\s+")
print(df)


# In[4]:


df2 = df['time']*0.001
print(df2)


# In[5]:


df3= df2.round(2)
df3.to_csv(r'rmsd_time.dat', header=True, index=False, sep=' ', mode='a')
df4= (df['RMSD']*10).round(2)
print(df4)


# In[6]:


print(df3, df4)
df4.to_csv(r'rmsd_rmsd.dat', header=True, index=False, sep=' ', mode='a')


# In[10]:





# In[19]:


bigdata = pd.concat([df3, df4], axis=1)
print(bigdata)
bigdata.to_csv(r'rmsd_data.txt', header=False, index=False, sep='$', mode='a')

# In[23]:
#####you have to save rmsd_data as a txt file then manually convert to xvg and use that.

from matplotlib import pyplot as plt


# In[28]:


x, y = [], []

with open("rmsd_data.xvg") as f:
    for line in f:
        cols = line.split()

        if len(cols) == 2:
            x.append(float(cols[0]))
            y.append(float(cols[1]))


fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.set_title(" ")    
ax1.set_xlabel('Time(ns)')
ax1.set_ylabel('RMSD(Å)')
ax1.plot(x,y, c='r', label='the data')
leg = ax1.legend()
plt.show() 


# In[ ]:





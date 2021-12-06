#!/usr/bin/env python
# coding: utf-8

# In[99]:


import random
import csv


# In[100]:


hexa = []
for i in range(100):
    hexa.append(hex(random.randint(10,100)))


# In[101]:


names1 = ['pratik','satyajit','harshad']
names2 = []
for i in range(100):
    a = random.randint(0,2)
    names2.append(names1[a])


# In[102]:


times = []
for hour in range(20):
    for minute in range(0, 60, 12):
        times.append('{:02d}:{:02d}'.format(hour, minute))


# In[103]:


F_list = []
for i in range(100):
    List = []
    List.append(times[i])
    List.append(names2[i])    
    List.append(l[i]) 
    F_list.append(ls)


# In[104]:


fields = ["Time","Name","Hex"]

with open('dataset.csv', 'w') as f:
    write = csv.writer(f)
      
    write.writerow(fields)
    write.writerows(lol)


# In[ ]:





# In[105]:


import pandas as pd

df = pd.read_csv("dataset.csv")
df


# In[ ]:





# In[ ]:





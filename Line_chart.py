#!/usr/bin/env python
# coding: utf-8

# In[158]:


get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
import matplotlib.pyplot as plt


# In[159]:


import pandas as pd

df = pd.read_csv("dataset.csv")
df


# In[160]:


dict1 = {"Time":[],
        "Name":[],
        "Hex":[]}
df2 = pd.DataFrame(dict1)


# In[161]:


# df2


# In[162]:


for i in range(100):
    if df["Name"][i] == "satyajit":
        df2 = df2.append(df[i:i+1], ignore_index="True")
#         df2[i+1] = df[i+1]


# In[163]:


for i in range(len(df2)):
    df2["Hex"][i] = df2["Hex"][i].lstrip("0x")


# In[164]:


len(df2)


# In[165]:


df2


# In[167]:


from matplotlib.pyplot import figure

figure(figsize=(25, 10), dpi=80)

plt.plot(df2["Time"], df2["Hex"], marker='o')
plt.title("Data Representation", fontweight='bold')
plt.xlabel("Time in HH:MM", fontweight='bold')
plt.ylabel("Hexadecimal Numbers", fontweight='bold')
plt.xticks(rotation=45)
plt.show()


# In[ ]:





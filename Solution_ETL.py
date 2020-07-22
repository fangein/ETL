#!/usr/bin/env python
# coding: utf-8

# In[5]:


legacy_data = {
            1: ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"],
            2: ["D", "G"],
            3: ["B", "C", "M", "P"],
            4: ["F", "H", "V", "W", "Y"],
            5: ["K"],
            8: ["J", "X"],
            10: ["Q", "Z"],
        }
data = {"a": 1}


# In[6]:


def transform(LegacyData):
    newData = {}
    
    for scores, letters in LegacyData.items():
        for l in letters:
            newData[l.lower()]= scores
    return newData


# In[7]:


transform(legacy_data)


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[2]:


def transform(LegacyData):
    newData = {}
    
    for scores, letters in LegacyData.items():
        for l in letters:
            newData[l.lower()]= scores
    return newData


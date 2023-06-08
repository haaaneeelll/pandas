#!/usr/bin/env python
# coding: utf-8

# # 데이터프레임이란?

# In[ ]:


import pandas as pd


# In[10]:


df1 = pd.DataFrame([[3,2,5], [10,0,2],[6,5,3]],
                    columns = ["사과", "자두", "포도"],
                    index=["이성계", "김유신", "이순신"])
s1 = df1["사과"];


# In[12]:


df1 #데이터프레임


# In[15]:


df1.sum() #세로가 default


# In[18]:


df1.values #가운데 내용물이 나온다.


# In[21]:


df1.index #인덱스


# In[22]:


df1.columns


# In[24]:


df1.values # pandas의 df1.values가 넘파이의 array


# In[26]:


df1.values > 3 #넘파이는 bool형태로 변환이 용이하다. 대소비교만 해도 bool로 변환됨


# In[28]:


s1 > 3


# In[37]:


pd.DataFrame([[3,2,5],[10,0,2],[6,5,3]], index=["이성계","김유신","이순신"], columns=["사과", "자두","포도"]) 


# In[ ]:


pd.Series([3,10,6])


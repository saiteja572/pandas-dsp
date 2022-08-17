#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
ds = pd.read_csv('Ecommerce_Purchases.csv')
ds.head()


# In[2]:


ds.info()


# In[3]:


ds['Purchase Price'].mean()


# In[6]:


ds['Purchase Price'].max()


# In[7]:


ds['Purchase Price'].min()


# In[10]:


ds[ds['Language']=='en'].count()


# In[15]:


ds[ds['Job']=='Lawyer'].info()


# In[13]:


ds['AM or PM'].value_counts()


# In[16]:


ds['Job'].value_counts().head(5)


# In[17]:


ds[ds['Lot']=='90 WT']['Purchase Price']


# In[19]:


ds[ds['Credit Card']==4926535242672853]['Email']


# In[24]:


ds[(ds['CC Provider']=='American Express') & (ds['Purchase Price']>95)].count()


# In[25]:


sum(ds['CC Exp Date'].apply(lambda x: x[3:]) == '25')


# In[26]:


ds['Email'].apply(lambda x: x.split('@')[1]).value_counts().head(5)


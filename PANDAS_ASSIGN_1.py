#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
dataset  = pd.read_csv('Salaries_1.csv')
dataset.head()


# In[2]:


dataset.info()


# In[5]:


dataset['BasePay'].mean()


# In[6]:


dataset['OvertimePay'].max()


# In[10]:


dataset[dataset['EmployeeName']=='JOSEPH DRISCOLL']['JobTitle']


# In[11]:


dataset[dataset['EmployeeName']=='JOSEPH DRISCOLL']['TotalPayBenefits']


# In[15]:


dataset[dataset['TotalPayBenefits']==dataset['TotalPayBenefits'].max()]


# In[16]:


dataset[dataset['TotalPayBenefits']==dataset['TotalPayBenefits'].min()]


# In[19]:


dataset.groupby('Year').mean()['BasePay']


# In[21]:


dataset['JobTitle'].nunique()


# In[24]:


jobs = dataset.groupby('JobTitle').count()
top_five = jobs.sort_values(by='Id',  ascending=False)[:5]
top_five['Id']


# In[26]:


year=dataset[dataset['Year'] == 2013]
group = year.groupby('JobTitle').count()
count = group[group['Id'] == 1]
count.count()['Id']


# In[29]:


def go_chief(job_title):    
    if 'chief' in job_title.lower().split():
        return True
    else:
        return False

df= pd.read_csv('Salaries_1.csv')

sum(df['JobTitle'].apply(lambda x: go_chief(x)))


# In[30]:


dataset['title_len'] = dataset['JobTitle'].apply(len)

dataset[['title_len', 'TotalPayBenefits']].corr()


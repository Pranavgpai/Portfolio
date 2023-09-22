#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[7]:


df = pd.read_csv(r"D:\Pranav\file.csv")


# In[8]:


df.head()


# In[ ]:


# Q1. How will you hide indices of the dataframe?


# In[9]:


df.style.hide_index()


# In[ ]:


# Q.2 How can we set caption/ heading on the dataframe?


# In[10]:


df.head(2)


# In[11]:


df.style.set_caption('India Census 2011 Dataset')


# In[ ]:


# Q.3 show the records related with districts - New Delhi ,Lucknow , Jaipur?


# In[20]:


df[df['District_name'].isin(['New Delhi', 'Lucknow', 'Jaipur'])]


# In[ ]:


#Q.4 Calculate the statewise :a). Total Number of population b). Total Number of population with different religions


# In[21]:


df.head(2)


# In[24]:


df.groupby('State_name').Population.sum().sort_values(ascending = False)


# In[34]:


df.groupby('State_name')['Hindus', 'Muslims', 'Christians', 'Sikhs', 'Buddhists', 'Jains'].sum().sort_values(by ='Hindus')


# In[ ]:





# In[ ]:


#Q5 How many Male workers were there in Maharashtra ?


# In[42]:


df[df.State_name =='MAHARASHTRA']['Male_Workers'].sum()


# In[ ]:





# In[ ]:


#Q6 How to set a column as index of Dataframe?


# In[44]:


df.set_index('District_code')


# In[ ]:





# In[ ]:


# Q 7 a) Add a suffix to column names B) Add a prefix to column Names


# In[ ]:





# In[45]:


df.head(1)


# In[ ]:





# In[47]:


df=df.add_suffix('Suffix')


# In[48]:


df


# In[49]:


df=df.add_prefix('prefix')


# In[50]:


df


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd


# In[4]:


data = pd.read_csv(r"C:\Users\Home\Downloads\1. Weather Data.csv")


# In[5]:


data


# In[7]:


data.head()


# In[8]:


data.shape


# In[9]:


data.index


# In[10]:


data.columns


# In[11]:


data.dtypes


# In[12]:


data['Weather'].unique()


# In[13]:


data.nunique()


# In[14]:


data.count()


# In[15]:


data['Weather'].value_counts()


# In[16]:


data.info()


# In[ ]:


#Find all unique 'Wind Speed' values in the data


# In[17]:


data.nunique()


# In[18]:


data['Wind Speed_km/h'].nunique()


# In[19]:


data['Wind Speed_km/h'].unique()


# In[ ]:


#Find the number of times the 'Weather is Exactly Clear'.


# In[20]:


#Value counts
data.Weather.value_counts()


# In[21]:


#Filtering
data[data.Weather== 'Clear']


# In[22]:


#groupby
data.groupby('Weather').get_group('Clear')


# In[ ]:


#Find the number of times the 'Wind Speed was exactly 4km/h'.


# In[23]:


data[data['Wind Speed_km/h']== 4]


# In[ ]:


#Findout all the null values in the data.


# In[24]:


data.isnull().sum()


# In[25]:


data.notnull().sum()


# In[ ]:


#Rename the column name 'Weather' of the dataframe to 'Weather Condition'


# In[26]:


data.rename(columns={'Weather' : 'Weather Condition'} , inplace = True)


# In[27]:


data.head()


# In[ ]:


#What is the mean visibility?


# In[28]:


data.Visibility_km.mean()


# In[ ]:


#What is the standard deviation of pressure in this data?


# In[29]:


data.Press_kPa.std()


# In[44]:


#What is theVariance of 'Relative Humidity' in this data?


# In[30]:


data['Rel Hum_%'].var()


# In[ ]:


#Find all instances when 'Snow' was recorded?


# In[31]:


data[data['Weather Condition'] == 'Snow']


# In[32]:


data[data['Weather Condition'].str.contains('Snow')].tail(50)


# In[ ]:


#Find all instances when 'Wind Speed is above 24' and 'Visibility is 25'.


# In[33]:


data[(data['Wind Speed_km/h']>24) & (data['Visibility_km']==25)]


# In[ ]:


#what is the mean value of each column against each 'Weather Condition'


# In[34]:


data.groupby('Weather Condition').mean()


# In[ ]:


#What is the minimum & maximum value of each coulmn against each "weather condition"?


# In[35]:


data.groupby('Weather Condition').min()


# In[36]:


data.groupby('Weather Condition').max()


# In[ ]:


#Show all the records ehere weather condition is fog?


# In[37]:


data[data['Weather Condition']== 'Fog']


# In[ ]:


#Find all instances when 'Weather is Clear'or 'Visibility is above 40'


# In[42]:


data[(data['Weather Condition']== 'Clear')|(data['Visibility_km']>40)].tail(50)


# In[ ]:


#Find all instances when:
#A. "weather is clear" and 'Relative Humidityis greater than 50' or
#B. 'Visibility is above 40'


# In[43]:


data[(data['Weather Condition']== 'Clear') & (data['Rel Hum_%']>50) |(data['Visibility_km']>40)]


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





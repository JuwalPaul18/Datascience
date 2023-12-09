#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
from scipy.stats import skew


# In[2]:


df=pd.read_csv('heart.csv')


# In[3]:


df.head()


# In[4]:


df.info


# In[5]:


df.describe()


# In[6]:


df.size


# In[7]:


df.shape


# In[8]:


df.isnull().sum()


# In[9]:


print(skew(df,axis=0,bias=True))


# # Data Visualization
# 

# In[10]:


import warnings
warnings.filterwarnings("ignore")


# In[11]:


for i in df.columns:
    sns.distplot(df[i])
    plt.show()


# In[12]:


sns.distplot(df['age'])
plt.show()


# In[13]:


sns.distplot(df['cp'])


# In[14]:


df.corr()


# In[15]:


pic=plt.figure(figsize=(14,7),dpi=100)
sns.heatmap(df.corr(),annot=True)


# In[16]:


sns.pairplot(data=df,vars=['age','chol','trestbps','sex'],hue='target')


# # Analysis Based on Age, Cholostrol and Heart Disease

# In[46]:


sns.barplot(x='target',y='age',data=df)


# In[44]:


sns.barplot(x='target',y='chol',data=df)


# In[19]:


sns.relplot(y='age',x='chol',hue='target',data=df)


# # Analysis based on Resting Blood Presuree, Age and Heart Disease

# In[20]:


sns.catplot(x='target',y='trestbps',kind='box',data=df)


# In[21]:


sns.catplot(x='target',y='age',kind='box',data=df)


# In[22]:


sns.relplot(x='age',y='trestbps',hue='target',data=df)


# # Analysis based on Talach, Age and Heart Disease

# In[23]:


sns.barplot(y='thalach',x='target',data=df)


# In[24]:


sns.barplot(y='age',x='target',data=df)


# In[25]:


sns.relplot(y='age',x='thalach',hue='target',data=df)


# # Analysis Based of HeartBeat,Age and Heart Disease 

# In[26]:


df["Heart Beat"]=220-df['age']


# In[27]:


df.head()


# In[45]:


sns.barplot(x='target',y='Heart Beat',data=df)


# In[29]:


sns.relplot(x='age',y='Heart Beat',hue='target',data=df)


# In[30]:





# In[31]:





# # Relationship Between Expected Heartbeat and Observed Heartbeat

# In[33]:


sns.jointplot(data=df,x='thalach',y='Heart Beat',hue='target')


# # Conclusions
# 

# 1) The heart diseases is more for the age group 40 to 70 and their heart beat is more than normal limit
# 2) The thalach is more than 140 for the people who have heart diseases
# 3) There is a significant diffence between expected heart beat and observed heart beat from the people who have heart diseases

# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[21]:


import numpy as np
from datetime import date


# In[22]:


#uploading data
df=pd.read_csv('HRDataset.csv')


# In[23]:


df


# In[24]:


df.isnull().sum()


# In[25]:


df['DateofTermination']=df['DateofTermination'].replace(to_replace=np.nan,value=0)


# In[26]:


df.isnull().sum()


# In[27]:


managerdata=df.loc[:,['ManagerName','Department','ManagerID']]


# In[28]:


nullvalue=managerdata[managerdata['ManagerID'].isnull()]
nullvalue


# In[29]:


managerdata.loc[managerdata['ManagerName'] == 'Webster Butler']


# In[30]:


df['ManagerID']=df['ManagerID'].replace(to_replace=np.nan,value=0)


# In[31]:


df


# In[32]:


#Count of employees in each department
count_Emp=df.groupby('Department')['Department'].count()


# In[33]:


count_Emp


# In[54]:


#Average salary of employess in each depatment
Avg_salary=df.groupby('Department')['Salary'].mean().reset_index(name='Avg_Salary')
Avg_salary


# In[35]:


#Calculate the average of salary of employees based on gender
Avg_sal_age=df.groupby(['Department','Sex'],as_index=False).Salary.mean()
Avg_sal_age


# In[36]:


#Most popular RecruitmentSource of the company based on department.
RE=df.groupby(['Department','RecruitmentSource']).size().reset_index(name='count')
RE


# In[37]:


#Total Number of working days for terminated employee.
Mng_Name=input("Enter the Name: ")


# In[40]:


Start_Day=int(input("Enter the Starting Day: "))
Start_Month=int(input("Enter the Starting Month: "))
Start_Year=int(input("Enter the Starting Year: "))
Start_Date=date(Start_Year,Start_Month,Start_Day)


# In[43]:


Tm_Day=int(input("Enter The Terminating Day: "))
Tm_Month=int(input("Enter The Terminating Month: "))
Tm_Year=int(input("Enter The Terminating Year: "))
Tm_Date=date(Tm_Year,Tm_Month,Tm_Day)


# In[44]:


Business_day=pd.bdate_range(Start_Date,Tm_Date)
Business_day


# In[45]:


print("Employee Name: ",Mng_Name,"Working Day: ",len(Business_day))


# In[51]:


#Fetch Employee name and number of absences.
Emp_Attendance=df.loc[:,['Department','ManagerName','Employee_Name','Absences']]


# In[52]:


Emp_Attendance


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


ytube = pd.read_csv('C:\\Users\\arunc\\Desktop\\data cleaning\\top-5000-youtube-channels.csv')
ytube.head()


# In[4]:


ytube.isnull().sum()
#Hence no missing values found


# In[5]:


ytube.info()


# In[6]:


###Will change datatypes of Rank,Grade,Video Uploads,Subscribers to Numerical Datatype
ytube['Rank'] = ytube['Rank'].str[0:-2].str.replace(',','').astype('int')


# In[7]:


ytube.tail()


# In[8]:


mask1 = ytube[ytube['Subscribers'].str.contains('-')].index
# So we have drop cells with sign -- after which Subscribers column can be numerical


# In[9]:


ytube.drop(labels=mask1,axis=0,inplace=True)


# In[10]:


ytube.shape


# In[11]:


ytube['Subscribers'] = ytube['Subscribers'].astype('int')


# In[12]:


ytube['Rank'] = ytube['Rank'].astype('int')


# In[13]:


ytube.info()
#Hence Subscribers and Rank is now completely converted into Numerical Data.Let's convert Video Uploads and Grade now


# In[14]:


ytube['Grade'].unique()


# In[15]:


channel_map = {'A++ ':5,'A+ ':4,'A ':3,'A- ':2,'B+ ':1}


# In[16]:


ytube['Grade'] = ytube['Grade'].map(channel_map)


# In[17]:


ytube['Grade'].unique()


# In[18]:


ytube.head()


# In[19]:


mask2 = ytube[ytube['Video Uploads'].str.contains('-')].index


# In[20]:


ytube.drop(labels=mask2,axis=0,inplace=True)


# In[21]:


ytube['Video Uploads'] = ytube['Video Uploads'].astype('int')


# In[22]:


ytube.info()
#Hence task Completed !!


# In[23]:


ytube.head()


# In[24]:


df=ytube.sort_values('Video Uploads',ascending=False)
df.head()
#Hence we can find out Channels with maximum no of Video Uploads,Subscribers,Video views by various imbuilt functions


# In[25]:


df1 = ytube.groupby(['Grade']).agg({'Video Uploads':'max','Subscribers':'max','Video views':'max'})


# In[26]:


df1.head()


# In[27]:


df1.reset_index(inplace=True)


# In[28]:


sns.barplot(x='Grade',y='Video Uploads',data=df1)
#Relationship between Grades with Maximum no of Video Uploads


# In[ ]:





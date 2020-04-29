#!/usr/bin/env python
# coding: utf-8

# In[1]:


#The data  is scraped from "https://www.imdb.com/list/ls003962970/". The data contains the names of the actors, 
#image link, and also a link that gives the personality traits of the actors.

import requests
import csv
import re
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

response = requests.get("https://www.imdb.com/list/ls003962970/")  #Making a request


# In[2]:


response.status_code


# In[3]:


from bs4 import BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')
type(soup)


# In[4]:


content_lis = soup.find_all('div', attrs={'class': 'lister-item-content'}) #Filtering the required content


# In[5]:


print(content_lis)


# In[6]:


len(content_lis) #No. of actors


# In[7]:


table = soup.find_all('div', attrs={'class': 'lister-item-content'})
len(table)


# In[8]:


print(table)


# In[9]:


names=[] #Storing name sof actors


# In[10]:


for tag in soup.find_all(re.compile("h3")):
    print(tag.text)
    names.append(tag.text)
   
   


# In[11]:


print(names)


# In[13]:


links_with_text = []  #Storing links containing Personality Traits
for a in soup.find_all('a', href=re.compile("/name/nm") ): 
        links_with_text.append('https://www.imdb.com/name/nm0000821/' + a['href'])


# In[14]:


print(links_with_text)


# In[16]:


images = [] #Stores image links
for a in soup.find_all('img', src=re.compile('https://m.media-amazon.com/images/M/') ): 
        images.append(a['src'])


# In[17]:


print(images)


# In[26]:


Names = np.asarray(names) #Creating arrays
Images = np.asarray(images)
URL = np.asarray(links_with_text)


# In[27]:


df=pd.DataFrame(Names) #Creating a datafarme
df['Personality traits'] = pd.DataFrame(URL)
df['images']= pd.DataFrame(Images)


# In[ ]:


df_new = df.rename(columns={'0': 'Names'})


# In[28]:


df_new.head()


# In[30]:


df.to_csv('Indian_actors.csv')


# In[ ]:





# In[ ]:





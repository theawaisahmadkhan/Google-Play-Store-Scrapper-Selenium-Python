#!/usr/bin/env python
# coding: utf-8

# In[12]:

 
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# In[13]:


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://play.google.com/store/games')
time.sleep(8)


# In[14]:


# Collect all game links
links_games = []
elems = driver.find_elements(By.XPATH, "//a[@href]")
for elem in elems:
    if "details?id" in elem.get_attribute("href"):
        links_games.append(elem.get_attribute("href"))

links_games = list(dict.fromkeys(links_games)) 


# In[ ]:


links_games = list(dict.fromkeys(links_games))  # Remove duplicates
list_all_elements = []

for link in links_games:
    try:
        driver.get(link)
        print(link)
        time.sleep(5)

        
        name = driver.find_element(By.XPATH, '//h1[@itemprop ="name"]').text
        description = driver.find_element(By.XPATH, '//div[@class ="bARER"]').text
        reviews_downloads = driver.find_element(By.XPATH, '//div[@class= "w7Iutd"]').text

        list_all_elements.append([name, description, reviews_downloads])

    except Exception as e:
        print(f"An error occurred: {e}")

# Save the scraped data to a CSV file
df = pd.DataFrame(list_all_elements,columns=['Name', 'Description', 'Reviews_and_Downloads'])
df.to_csv('scraping_playstore.csv', header = True, index=False)


# In[ ]:





# In[ ]:





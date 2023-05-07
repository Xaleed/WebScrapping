#!/usr/bin/env python
# coding: utf-8

# In[48]:


from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
# %%
!pip install webdriver_manager
# In[56]:


options = Options()
options.add_argument("--headless")
#driver = webdriver.Firefox(options=options)

#driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
#driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)


# In[57]:


driver.get("https://parto.seo.ir/ViolationReport/AddOrEditViolationReport")


# In[ ]:


html(/body/div[1]/div[2]/div/div/nav/div/div[1]/div/div[2]/ul[2]/li/a/span[2])


# In[59]:


download= driver.find_element('xpath','/html/body/div[1]/div[2]/div/div/nav/div/div[1]/div/div[2]/ul[2]/li/a/span[2]');
download.click();


# In[61]:


downloadcsv= driver.find_element('id','addAccused');
downloadcsv.click();


# In[62]:


downloadc= driver.find_element('xpath','/html/body/div[1]/div[2]/div/div/div[1]/div/div[5]/div/div/div[2]/ul/li[2]/a');
downloadc.click();


# In[63]:


driver.find_element("id", "real-nationalId").send_keys("0386622051")


# In[ ]:


driver.find_element('xpath','/html/body/div[1]/div[2]/div/div/div[1]/div/div[5]/div/div/div[2]/div[1]/div[2]/div[4]/button').click()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





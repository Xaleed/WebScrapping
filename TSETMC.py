#!/usr/bin/env python
# coding: utf-8

# In[48]:


from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.select import Select

# In[56]:


options = Options()
options.add_argument("--headless")
#driver = webdriver.Firefox(options=options)

#driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
#driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)


# In[57]:
driver.get("http://www.tsetmc.com/Loader.aspx?ParTree=15")

# In[59]:


download= driver.find_element('id','search');
download.click();


# In[61]:


downloadcsv= driver.find_element('id','addAccused');
downloadcsv.click();




# In[63]:


driver.find_element("id", "SearchKey").send_keys("حتاید")
#0386622051

# In[62]:


driver.find_element('xpath','/html/body/div[5]/section/div/div/div/div[2]/table/tbody/tr[1]/td[1]/a').click();
#/html/body/div[5]/section/div/div/div/div[2]/table/tbody/tr[1]/td[1]/a/html/body/div[5]/section/div/div/div/div[2]/table/tbody/tr[1]/td[1]/a


# In[ ]:


K = driver.find_element('xpath','/html/body/div[4]/form/div[3]/div[2]/div[1]/div[3]/div[2]/div/div[5]/span')
# %%
K.click() 
# %%
driver.find_element('xpath','/html/body/div[5]/section/div/div/div/div[2]/table/tbody/tr[1]/td[1]/a').click()

#/html/body/div/div/div[2]/div[2]/div[2]/div[1]/div[2]/span/span[3]
# In[ ]:
x = driver.find_element('xpath','/html/body/div[1]/div[2]/div/div/div[1]/div/div[5]/div/div/div[2]/div[1]/div[2]/div[5]/div/div[2]/div[3]/div/label/select')
# In[ ]:
select = Select(x)
# %%
options = select.options
options[2].click()
#options = select.options


# %%

Row = driver.find_elements('xpath',"/html/body/div[1]/div[2]/div/div/div[1]/div/div[5]/div/div/div[2]/div[1]/div[2]/div[5]/div/div[1]/div[1]/div[2]/table/tbody/tr")
len(Row)

# In[ ]:
Col = driver.find_elements('xpath',"/html/body/div[1]/div[2]/div/div/div[1]/div/div[5]/div/div/div[2]/div[1]/div[2]/div[5]/div/div[1]/div[1]/div[2]/table/tbody/tr[2]/td")
len(Col)

# %%

for r in range(1, len(Row)+1):
  
    for p in range(1, len(Col)):
       
        # obtaining the text from each column of the table
        value = driver.find_element('xpath',"/html/body/div[1]/div[2]/div/div/div[1]/div/div[5]/div/div/div[2]/div[1]/div[2]/div[5]/div/div[1]/div[1]/div[2]/table/tbody/tr["+str(r)+"]/td["+str(p)+"]").text
        print(value, end='       ')
    print()


# %%
driver.find_element('xpath',"/html/body/div[1]/div[2]/div/div/div[1]/div/div[5]/div/div/div[2]/div[1]/div[2]/div[5]/div/div[1]/div[1]/div[2]/table/tbody/tr[1]/td[1]").text
# %%
len(Row)
# %%

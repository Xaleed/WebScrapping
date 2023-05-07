#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options


# In[2]:


options = Options()
options.add_argument("--headless")
#driver = webdriver.Firefox(options=options)

#driver = webdriver.Chrome(ChromeDriverManager().install())
#driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)


# In[13]:


username = "09192004727"
password = "Mahdi@32587"


# In[14]:


driver.get("https://account.emofid.com/Login?ReturnUrl=%2Fconnect%2Fauthorize%2Fcallback%3Fclient_id%3Dbourseview%26secret%3DmTmfpDDb%26scope%3Dopenid%2520account%2520offline_access%2520profile%26response_type%3Did_token%2520token%26redirect_uri%3Dhttps%253A%252F%252Fwww.bourseview.com%252Fpublic%252Fauth%252Fmofid%252Fcallback%26state%3D%257B%2522user_id%2522%253A%2520null,%2520%2522oauth_provider_key%2522%253A%2520null%257D%26nonce%3Dd6be7ff1d997442695ffc91c17e7722e%26response_mode%3Dform_post")


# In[ ]:





# In[11]:


driver.find_element("id", "Username").send_keys(username)
driver.find_element("id","Password").send_keys(password)
driver.find_element("id","submit_btn").click()


# In[5]:


def CreateUrl(a):
    b = "https://www.bourseview.com/home/#/stockmarket/"+a+"/production?tickerId="+a+"&scenario=actual&revise=&type=yearly&period=5&template=detail&field=valueOrigin&view=origin&trend=&currency=IRR&order=true&series=historical&asReported=false&exportDomestic=false&firstEstimate=false&isIndice=undefined&exchange=IRTSENO&consolidated=non-consolidated&endD=undefined"
    return(b)


# In[6]:


#driver.find_element("id", "input-0").send_keys(st)


# In[16]:


r = CreateUrl("IRO1FSAZ0001")
driver.get(r)


# In[17]:


downloadcsv= driver.find_element('xpath','/html/body/div[2]/div/div/div/div/div[3]/div[3]/div/div/div/div[3]/div[1]/div[2]/div/div/div[1]/span[2]/span');
downloadcsv.click();


# In[ ]:


(/*[@id="addAccused"])


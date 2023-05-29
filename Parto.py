#!/usr/bin/env python
# coding: utf-8

# In[459]:


#!/usr/bin/env python
# coding: utf-8

# In[48]:

import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
#import org.openqa.selenium.Keys

# %%


# In[323]:





# In[16]:



# In[56]:


options = Options()
options.add_argument("--headless")
#driver = webdriver.Firefox(options=options)

#driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
#driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)


# In[57]:


driver.get("https://parto.seo.ir/ViolationReport/AddOrEditViolationReport")


# In[498]:



d = pd.read_excel("C:\\Users\\masoumifard.kh\\Desktop\\Parto\\kh.xlsx");


# In[499]:


d


# In[500]:


d.columns


# In[502]:


d1 = d['كد جدید سهامدار مشكوك']
str(int(d1[0]))[1:11]


# In[548]:


P1 = []
P2 = []
P3 = []
P4 = []
P5 = []
P6 = []
P7 = []
P8 = []
P9 = []
P10 = []
P11 = []


# In[549]:


download= driver.find_element('xpath','/html/body/div[1]/div[2]/div/div/nav/div/div[1]/div/div[2]/ul[2]/li/a/span[2]');
download.click();


# In[ ]:





# In[ ]:





# In[550]:


a = d1[0]
int(a)


# In[ ]:





# In[551]:






# In[61]:





# In[62]:



# In[552]:



#downloadcsv.click();


# In[553]:


driver.refresh()


# In[554]:


downloadcsv= driver.find_element('id','addAccused');
downloadcsv.click()
downloadc= driver.find_element('xpath','/html/body/div[1]/div[2]/div/div/div[1]/div/div[5]/div/div/div[2]/ul/li[2]/a');
downloadc.click();


# In[555]:


Row = driver.find_elements('xpath',"/html/body/div[1]/div[2]/div/div/div[1]/div/div[5]/div/div/div[2]/div[1]/div[2]/div[5]/div/div[1]/div[1]/div[2]/table/tbody/tr")
x = driver.find_element('xpath','/html/body/div[1]/div[2]/div/div/div[1]/div/div[5]/div/div/div[2]/div[1]/div[2]/div[5]/div/div[2]/div[3]/div/label/select')
# In[ ]:
select = Select(x)
# %%
options = select.options
options[2].click()


# In[556]:


a = 39
t = driver.find_element("id", "real-nationalId")


# In[557]:


t.clear()
t.send_keys(int(d1[a]))


# In[558]:


o = driver.find_element('xpath','/html/body/div[1]/div[2]/div/div/div[1]/div/div[5]/div/div/div[2]/div[1]/div[2]/div[4]/button')


# In[559]:


ActionChains(driver).move_to_element(o).click().perform()


# In[560]:


t = driver.find_element("id", "real-nationalId")
o = driver.find_element('xpath','/html/body/div[1]/div[2]/div/div/div[1]/div/div[5]/div/div/div[2]/div[1]/div[2]/div[4]/button')


# In[561]:


a = 60
#/html/body/div[1]/div[2]/div/div/div[1]/div/div[5]/div/div/div[2]/div[1]/div[2]/div[4]/button


# In[582]:


for a in range(1,len(d1)): 
    t.clear()
    t.send_keys(str(int(d1[a]))[1:11])
    #driver.execute_script("arguments[0].click();", o)
    #o = driver.find_element('xpath','/html/body/div[1]/div[2]/div/div/div[1]/div/div[5]/div/div/div[2]/div[1]/div[2]/div[4]/button')
   # o.click()
    ActionChains(driver).move_to_element(o).click().perform()
    #o = driver.find_element('xpath','/html/body/div[1]/div[2]/div/div/div[1]/div/div[5]/div/div/div[2]/div[1]/div[2]/div[4]/button')
    Row = driver.find_elements('xpath',"/html/body/div[1]/div[2]/div/div/div[1]/div/div[5]/div/div/div[2]/div[1]/div[2]/div[5]/div/div[1]/div[1]/div[2]/table/tbody/tr")

    #WebElement.sendKeys(Keys.RETURN);
    Col = driver.find_elements('xpath',"/html/body/div[1]/div[2]/div/div/div[1]/div/div[5]/div/div/div[2]/div[1]/div[2]/div[5]/div/div[1]/div[1]/div[2]/table/tbody/tr[2]/td")
    try:
        for r in range(1,len(Row)+1):

            for p in range(1, len(Col)):

                # obtaining the text from each column of the table
                value = driver.find_element('xpath',"/html/body/div[1]/div[2]/div/div/div[1]/div/div[5]/div/div/div[2]/div[1]/div[2]/div[5]/div/div[1]/div[1]/div[2]/table/tbody/tr["+str(r)+"]/td["+str(p)+"]").text
                print(value, end='       ')
                if p == 1:
                    print(value)
                    print(p)
                    P1.append(value)
                if p == 2:
                    print(value)
                    print(p)
                    P2.append(value)
                if p == 3:
                    print(value)
                    print(p)
                    P3.append(value)
                if p == 4:
                    print(value)
                    print(p)
                    P4.append(value)
                if p == 5:
                    print(value)
                    print(p)
                    P5.append(value)
                if p == 6:
                    print(value)
                    print(p)
                    P6.append(value)
                if p == 7:
                    print(value)
                    print(p)
                    P7.append(value)
                if p == 8:
                    print(value)
                    print(p)
                    P8.append(value)
             # 3  if p == 9:
                  #  print(value)
                   # print(p)
                   # P9.append(value)
              #  if p == 10:
                 #   print(value)
                  #  print(p)
                 #   P10.append(value)
               # if p == 11:
                   # print(value)
                  #  print(p)
                   # P11.append(value)
            print(a)
    except:
    #some print statement 
        pass


# In[576]:


for p in range(1, 10):
    print(p)


# In[577]:


P1


# In[578]:


d = {'P1' : P1 , 'P2': P2,'P3' :P3 }
df=pd.DataFrame(d)
df


# In[308]:


for a in range(len(d1)): 
    t.clear()
    t.send_keys(int(d1[a]))
    #o.clear()
    #o = driver.find_element('xpath','/html/body/div[1]/div[2]/div/div/div[1]/div/div[5]/div/div/div[2]/div[1]/div[2]/div[4]/button')
    o.click()
    Col = driver.find_elements('xpath',"/html/body/div[1]/div[2]/div/div/div[1]/div/div[5]/div/div/div[2]/div[1]/div[2]/div[5]/div/div[1]/div[1]/div[2]/table/tbody/tr[2]/td")

    if len(Col) > 0:
        for r in range(1, len(Row)+1):

            for p in range(1, len(Col)):

                # obtaining the text from each column of the table
                value = driver.find_element('xpath',"/html/body/div[1]/div[2]/div/div/div[1]/div/div[5]/div/div/div[2]/div[1]/div[2]/div[5]/div/div[1]/div[1]/div[2]/table/tbody/tr["+str(r)+"]/td["+str(p)+"]").text
                print(value, end='       ')
                if p == 1:
                    P1.append(value)
                if p == 2:
                    P2.append(value)
                if p == 3:
                    P3.append(value)
                if p == 4:
                    P4.append(value)
                if p == 5:
                    P5.append(value)
                if p == 6:
                    P6.append(value)
                if p == 7:
                    P7.append(value)
                if p == 8:
                    P8.append(value)
                if p == 9:
                    P9.append(value)
                if p == 10:
                    P10.append(value)
                if p == 11:
                    P11.append(value)
            print()
        #driver.refresh()
        # %%
        #P6
        # %%
        #driver.find_element('xpath',"/html/body/div[1]/div[2]/div/div/div[1]/div/div[5]/div/div/div[2]/div[1]/div[2]/div[5]/div/div[1]/div[1]/div[2]/table/tbody/tr[1]/td[1]").text
        # %%
        #len(Row)
#driver.refresh()


# In[269]:


P1


# In[137]:




# In[63]:


#0386622051


# In[ ]:

a = 3
downloadcsv= driver.find_element('id','addAccused');
downloadcsv.click()
downloadc= driver.find_element('xpath','/html/body/div[1]/div[2]/div/div/div[1]/div/div[5]/div/div/div[2]/ul/li[2]/a');
downloadc.click();
driver.find_element("id", "real-nationalId").send_keys(int(d1[a]))
driver.find_element('xpath','/html/body/div[1]/div[2]/div/div/div[1]/div/div[5]/div/div/div[2]/div[1]/div[2]/div[4]/button').click()
Row = driver.find_elements('xpath',"/html/body/div[1]/div[2]/div/div/div[1]/div/div[5]/div/div/div[2]/div[1]/div[2]/div[5]/div/div[1]/div[1]/div[2]/table/tbody/tr")
len(Row)
#if len(Row) > 4:
# In[ ]:
#    x = driver.find_element('xpath','/html/body/div[1]/div[2]/div/div/div[1]/div/div[5]/div/div/div[2]/div[1]/div[2]/div[5]/div/div[2]/div[3]/div/label/select')
    # In[ ]:
#    select = Select(x)
 #   # %%
#    options = select.options
#    options[2].click()
    #options = select.options


    # %%



# In[ ]:




# %%
if len(Col) > 0:
    for r in range(1, len(Row)+1):

        for p in range(1, len(Col)):

            # obtaining the text from each column of the table
            value = driver.find_element('xpath',"/html/body/div[1]/div[2]/div/div/div[1]/div/div[5]/div/div/div[2]/div[1]/div[2]/div[5]/div/div[1]/div[1]/div[2]/table/tbody/tr["+str(r)+"]/td["+str(p)+"]").text
            print(value, end='       ')
            if p == 1:
                P1.append(value)
            if p == 2:
                P2.append(value)
            if p == 3:
                P3.append(value)
            if p == 4:
                P4.append(value)
            if p == 5:
                P5.append(value)
            if p == 6:
                P6.append(value)
            if p == 7:
                P7.append(value)
            if p == 8:
                P8.append(value)
            if p == 9:
                P9.append(value)
            if p == 10:
                P10.append(value)
            if p == 11:
                P11.append(value)
        print()
    driver.refresh()
    # %%
    P6
    # %%
    driver.find_element('xpath',"/html/body/div[1]/div[2]/div/div/div[1]/div/div[5]/div/div/div[2]/div[1]/div[2]/div[5]/div/div[1]/div[1]/div[2]/table/tbody/tr[1]/td[1]").text
    # %%
    len(Row)
driver.refresh()
# %%


# In[131]:


P1


# In[135]:


for a in range(len(d1)):




    # In[63]:


    #0386622051


    # In[ ]:


    downloadcsv= driver.find_element('id','addAccused');
    downloadcsv.click()
    downloadc= driver.find_element('xpath','/html/body/div[1]/div[2]/div/div/div[1]/div/div[5]/div/div/div[2]/ul/li[2]/a');
    downloadc.click();
    driver.find_element("id", "real-nationalId").send_keys(int(d1[a]))
    driver.find_element('xpath','/html/body/div[1]/div[2]/div/div/div[1]/div/div[5]/div/div/div[2]/div[1]/div[2]/div[4]/button').click()


    # In[ ]:
    if len(Col) > 0:
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
    print(len(Col))



    # %%
    if len(Col) > 0:
        for r in range(1, len(Row)+1):

            for p in range(1, len(Col)):

                # obtaining the text from each column of the table
                value = driver.find_element('xpath',"/html/body/div[1]/div[2]/div/div/div[1]/div/div[5]/div/div/div[2]/div[1]/div[2]/div[5]/div/div[1]/div[1]/div[2]/table/tbody/tr["+str(r)+"]/td["+str(p)+"]").text
                print(value, end='       ')
                if p == 1:
                    P1.append(value)
                if p == 2:
                    P2.append(value)
                if p == 3:
                    P3.append(value)
                if p == 4:
                    P4.append(value)
                if p == 5:
                    P5.append(value)
                if p == 6:
                    P6.append(value)
                if p == 7:
                    P7.append(value)
                if p == 8:
                    P8.append(value)
                if p == 9:
                    P9.append(value)
                if p == 10:
                    P10.append(value)
                if p == 11:
                    P11.append(value)
            print()
        driver.refresh()
        # %%
        P6
        # %%
        driver.find_element('xpath',"/html/body/div[1]/div[2]/div/div/div[1]/div/div[5]/div/div/div[2]/div[1]/div[2]/div[5]/div/div[1]/div[1]/div[2]/table/tbody/tr[1]/td[1]").text
        # %%
        len(Row)
    driver.refresh()
# %%


# In[120]:


P1


# In[ ]:






# In[63]:


#0386622051


# In[ ]:


downloadcsv= driver.find_element('id','addAccused');
downloadcsv.click()
downloadc= driver.find_element('xpath','/html/body/div[1]/div[2]/div/div/div[1]/div/div[5]/div/div/div[2]/ul/li[2]/a');
downloadc.click();
driver.find_element("id", "real-nationalId").send_keys(int(d1[0]))
driver.find_element('xpath','/html/body/div[1]/div[2]/div/div/div[1]/div/div[5]/div/div/div[2]/div[1]/div[2]/div[4]/button').click()


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
print(len(Col))



# %%
for r in range(1, len(Row)+1):
  
    for p in range(1, len(Col)):
       
        # obtaining the text from each column of the table
        value = driver.find_element('xpath',"/html/body/div[1]/div[2]/div/div/div[1]/div/div[5]/div/div/div[2]/div[1]/div[2]/div[5]/div/div[1]/div[1]/div[2]/table/tbody/tr["+str(r)+"]/td["+str(p)+"]").text
        print(value, end='       ')
        if p == 1:
            P1.append(value)
        if p == 2:
            P2.append(value)
        if p == 3:
            P3.append(value)
        if p == 4:
            P4.append(value)
        if p == 5:
            P5.append(value)
        if p == 6:
            P6.append(value)
        if p == 7:
            P7.append(value)
        if p == 8:
            P8.append(value)
        if p == 9:
            P9.append(value)
        if p == 10:
            P10.append(value)
        if p == 11:
            P11.append(value)
    print()
driver.refresh()
# %%
P6
# %%
driver.find_element('xpath',"/html/body/div[1]/div[2]/div/div/div[1]/div/div[5]/div/div/div[2]/div[1]/div[2]/div[5]/div/div[1]/div[1]/div[2]/table/tbody/tr[1]/td[1]").text
# %%
len(Row)
# %%


# In[63]:


driver.refresh()


# In[ ]:





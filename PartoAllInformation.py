# %%
import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
# %%

options = Options()
options.add_argument("--headless")
#driver = webdriver.Firefox(options=options)

#driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
#driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)
# %%
driver.get("https://parto.seo.ir/ViolationReport/AddOrEditViolationReport")
username = "Masoumifard.kh"
password = "Masoumifard.kh@1"
# %%
# برای این قسمت باید عدد داخل باکس در صفحه وب وارد شود
Captcha = 80503
# %%
driver.find_element("id", "UserName").send_keys(username)
driver.find_element("id","Password").send_keys(password)
driver.find_element("id","Captcha").send_keys(Captcha)
driver.find_element("xpath","/html/body/div/form/section/div/div/div[2]/button").click()
# %%
d = pd.read_excel("C:\\Users\\masoumifard.kh\\Desktop\\Parto\\kh.xlsx");
d1 = d['كد جدید سهامدار مشكوك'];
#%%
P1 = []
P1_1 = []
P2 = []
P2_1 = []
P3 = []
P3_1 = []
P4 = []
P4_1 = []
P5 = []
P5_1 = []
P6 = []
P6_1 = []
P7 = []
P7_1 = []
P8 = []
P8_1 = []
P9 = []
P9_1 = []
P10 = []
P10_1 = []
P11 = []
P11_1 = []
# %%
download= driver.find_element('xpath','/html/body/div[1]/div[2]/div/div/nav/div/div[1]/div/div[2]/ul[2]/li/a/span[2]');
download.click();
driver.refresh()
downloadcsv= driver.find_element('id','addAccused');
downloadcsv.click()
downloadc= driver.find_element('xpath','/html/body/div[1]/div[2]/div/div/div[1]/div/div[5]/div/div/div[2]/ul/li[2]/a');
downloadc.click();
# %%
Row = driver.find_elements('xpath',"/html/body/div[1]/div[2]/div/div/div[1]/div/div[5]/div/div/div[2]/div[1]/div[2]/div[5]/div/div[1]/div[1]/div[2]/table/tbody/tr")
x = driver.find_element('xpath','/html/body/div[1]/div[2]/div/div/div[1]/div/div[5]/div/div/div[2]/div[1]/div[2]/div[5]/div/div[2]/div[3]/div/label/select')
# In[ ]:
select = Select(x)
# %%
options = select.options
options[2].click()
# %%


for a in range(1,40): 
    #t.clear()
    #t.send_keys(str(int(d1[a]))[1:11])
    #driver.execute_script("arguments[0].click();", o)
    #o = driver.find_element('xpath','/html/body/div[1]/div[2]/div/div/div[1]/div/div[5]/div/div/div[2]/div[1]/div[2]/div[4]/button')
   # o.click()
    #ActionChains(driver).move_to_element(o).click().perform()
    #o = driver.find_element('xpath','/html/body/div[1]/div[2]/div/div/div[1]/div/div[5]/div/div/div[2]/div[1]/div[2]/div[4]/button')
    Row = driver.find_elements('xpath',"/html/body/div[1]/div[2]/div/div/div[1]/div/div[5]/div/div/div[2]/div[1]/div[2]/div[5]/div/div[1]/div[1]/div[2]/table/tbody/tr")

    #WebElement.sendKeys(Keys.RETURN);
    Col = driver.find_elements('xpath',"/html/body/div[1]/div[2]/div/div/div[1]/div/div[5]/div/div/div[2]/div[1]/div[2]/div[5]/div/div[1]/div[1]/div[2]/table/tbody/tr[2]/td")
    try:
        for r in range(1,len(Row)+1):
            print(len(Row))

            for p in range(1, 10):

                # obtaining the text from each column of the table
                value = driver.find_element('xpath',"/html/body/div[1]/div[2]/div/div/div[1]/div/div[5]/div/div/div[2]/div[1]/div[2]/div[5]/div/div[1]/div[1]/div[2]/table/tbody/tr["+str(r)+"]/td["+str(p)+"]").text
                #print(value, end='       ')
                if value != 'رکوردی با این مشخصات پیدا نشد':
                    if p == 1:
                        #print(value)
                        #print(p)
                        P1.append(value)
                        P1_1.append(str(a)+'_'+str(r))
                    if p == 2:
                        #print(value)
                        ##print(p)
                        P2.append(value)
                        P2_1.append(str(a)+'_'+str(r))
                    if p == 3:
                        #print(value)
                        #print(p)
                        P3.append(value)
                        P3_1.append(str(a)+'_'+str(r))
                    if p == 4:
                        #print(value)
                        #print(p)
                        P4.append(value)
                        P4_1.append(str(a)+'_'+str(r))
                    if p == 5:
                        #print(value)
                        #print(p)
                        P5.append(value)
                        P5_1.append(str(a)+'_'+str(r))
                    if p == 6:
                        #print(value)
                        #print(p)
                        P6.append(value)
                        P6_1.append(str(a)+'_'+str(r))
                    if p == 7:
                        #print(value)
                        #print(p)
                        P7.append(value)
                        P7_1.append(str(a)+'_'+str(r))
                    if p == 8:
                        #print(value)
                        #print(p)
                        P8.append(value)
                        P8_1.append(str(a)+'_'+str(r))
                    if p == 9:
                        #print(value)
                        #print(p)
                        P9.append(value)
                        P9_1.append(str(a)+'_'+str(r))
                    if p == 10:
                        #print(value)
                        #print(p)
                        P10.append(value)
                        P10_1.append(str(a)+'_'+str(r))
                    if p == 11:
                        #print(value)
                        #print(p)
                        P11.append(value)
                        P11_1.append(str(a)+'_'+str(r))
            print(a)
    except:
    #some print statement 
        pass
    o1 = driver.find_element('xpath','//*[@id="table-real-peaple-serach-result_next"]')
    o1.click()

# %%
#############################################
dd1 = {'N' : P1_1 , 'P1': P1}
df1=pd.DataFrame(dd1)

d2 = {'N' : P2_1 , 'P2': P2}
df2=pd.DataFrame(d2)

d3 = {'N' : P3_1 , 'P3': P3}
df3=pd.DataFrame(d3)
d4 = {'N' : P4_1 , 'P4': P4}
df4=pd.DataFrame(d4)
d5 = {'N' : P5_1 , 'P5': P5}
df5=pd.DataFrame(d5)
d6 = {'N' : P6_1 , 'P6': P6}
df6=pd.DataFrame(d6)
d7 = {'N' : P7_1 , 'P7': P7}
df7=pd.DataFrame(d7)
d8 = {'N' : P8_1 , 'P8': P8}
df8=pd.DataFrame(d8)
d9 = {'N' : P9_1 , 'P9': P9}
df9=pd.DataFrame(d9)
D1 = pd.merge(df1, df2,how = 'left',on="N")
D2 = pd.merge(df3, df4,how = 'left',on="N")
D3 = pd.merge(df5, df6,how = 'left',on="N")
D4 = pd.merge(df7, df8,how = 'left',on="N")
D11 = pd.merge(D1, D2,how = 'left',on="N")
D21 = pd.merge(D3, D4,how = 'left',on="N")
D111 = pd.merge(D11, D21,how = 'left',on="N")
F = pd.merge(D111, df9,how = 'left',on="N")
#F.to_excel('C:\\Users\\masoumifard.kh\\Desktop\\Parto\\Result3.xlsx')
F
# %%
a = 39
t = driver.find_element("id", "real-nationalId")
t.clear()
t.send_keys(int(d1[a]))
# %%
o = driver.find_element('xpath','/html/body/div[1]/div[2]/div/div/div[1]/div/div[5]/div/div/div[2]/div[1]/div[2]/div[4]/button')


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
            #print(len(Row))

            for p in range(1, 11):

                # obtaining the text from each column of the table
                value = driver.find_element('xpath',"/html/body/div[1]/div[2]/div/div/div[1]/div/div[5]/div/div/div[2]/div[1]/div[2]/div[5]/div/div[1]/div[1]/div[2]/table/tbody/tr["+str(r)+"]/td["+str(p)+"]").text
                #print(value, end='       ')
                if value != 'رکوردی با این مشخصات پیدا نشد':
                    if p == 1:
                        #print(value)
                        #print(p)
                        P1.append(value)
                        P1_1.append(str(a)+'_'+str(r))
                    if p == 2:
                        #print(value)
                        ##print(p)
                        P2.append(value)
                        P2_1.append(str(a)+'_'+str(r))
                    if p == 3:
                        #print(value)
                        #print(p)
                        P3.append(value)
                        P3_1.append(str(a)+'_'+str(r))
                    if p == 4:
                        #print(value)
                        #print(p)
                        P4.append(value)
                        P4_1.append(str(a)+'_'+str(r))
                    if p == 5:
                        #print(value)
                        #print(p)
                        P5.append(value)
                        P5_1.append(str(a)+'_'+str(r))
                    if p == 6:
                        #print(value)
                        #print(p)
                        P6.append(value)
                        P6_1.append(str(a)+'_'+str(r))
                    if p == 7:
                        #print(value)
                        #print(p)
                        P7.append(value)
                        P7_1.append(str(a)+'_'+str(r))
                    if p == 8:
                        #print(value)
                        #print(p)
                        P8.append(value)
                        P8_1.append(str(a)+'_'+str(r))
                    if p == 9:
                        #print(value)
                        #print(p)
                        P9.append(value)
                        P9_1.append(str(a)+'_'+str(r))
                    if p == 10:
                        #print(value)
                        #print(p)
                        P10.append(value)
                        P10_1.append(str(a)+'_'+str(r))
                    if p == 11:
                        #print(value)
                        #print(p)
                        P11.append(value)
                        P11_1.append(str(a)+'_'+str(r))
            #print(a)
    except:
    #some print statement 
        pass

# %%
[len(P1),len(P2),len(P3),len(P4),len(P5),len(P6),len(P7),len(P8),len(P9)]
# %%
dd1 = {'N' : P1_1 , 'P1': P1}
df1=pd.DataFrame(dd1)

d2 = {'N' : P2_1 , 'P2': P2}
df2=pd.DataFrame(d2)

d3 = {'N' : P3_1 , 'P3': P3}
df3=pd.DataFrame(d3)
d4 = {'N' : P4_1 , 'P4': P4}
df4=pd.DataFrame(d4)
d5 = {'N' : P5_1 , 'P5': P5}
df5=pd.DataFrame(d5)
d6 = {'N' : P6_1 , 'P6': P6}
df6=pd.DataFrame(d6)
d7 = {'N' : P7_1 , 'P7': P7}
df7=pd.DataFrame(d7)
d8 = {'N' : P8_1 , 'P8': P8}
df8=pd.DataFrame(d8)
d9 = {'N' : P9_1 , 'P9': P9}
df9=pd.DataFrame(d9)
D1 = pd.merge(df1, df2,how = 'left',on="N")
D2 = pd.merge(df3, df4,how = 'left',on="N")
D3 = pd.merge(df5, df6,how = 'left',on="N")
D4 = pd.merge(df7, df8,how = 'left',on="N")
D11 = pd.merge(D1, D2,how = 'left',on="N")
D21 = pd.merge(D3, D4,how = 'left',on="N")
D111 = pd.merge(D11, D21,how = 'left',on="N")
F = pd.merge(D111, df9,how = 'left',on="N")
F.to_excel('C:\\Users\\masoumifard.kh\\Desktop\\Parto\\Result3.xlsx')


# %%
for a in range(1,len(d1)): 
    a = 21
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

    for r in range(1,len(Row)+1):
        #print(len(Row))

        for p in range(1, 11):
            #print(len(Col))

            # obtaining the text from each column of the table
            try:
                value = driver.find_element('xpath',"/html/body/div[1]/div[2]/div/div/div[1]/div/div[5]/div/div/div[2]/div[1]/div[2]/div[5]/div/div[1]/div[1]/div[2]/table/tbody/tr["+str(r)+"]/td["+str(p)+"]").text
                #print(value, end='       ')
                if value != 'رکوردی با این مشخصات پیدا نشد':
                    if p == 1:
                        print(value)
                       # print(p)
                        P1.append(value)
                    if p == 2:
                        print(value)
                        #print(p)
                        P2.append(value)
                    if p == 3:
                        print(value)
                        #print(p)
                        P3.append(value)
                    if p == 4:
                        print(value)
                        #print(p)
                        P4.append(value)
                    if p == 5:
                        print(value)
                        #print(p)
                        P5.append(value)
                    if p == 6:
                        print(value)
                        #print(p)
                        P6.append(value)
                    if p == 7:
                        print(value)
                        #print(p)
                        P7.append(value)
                    if p == 8:
                        print(value)
                        #print(p)
                        P8.append(value)
                    if p == 9:
                        print(value)
                       # print(p)
                        P9.append(value)
                    if p == 10:
                        print(value)
                      #  print(p)
                        P10.append(value)
                    if p == 11:
                       # print(value)
                      #  print(p)
                        P11.append(value)
            except:
                pass

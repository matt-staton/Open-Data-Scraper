from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
import random
import time
import re
import string
import urlparse
from bs4 import BeautifulSoup
import pandas as pd
from pandas import DataFrame, Series
path_to_chromedriver = '//home//isb//Downloads//chromedriver' ##C:\Anaconda\selenium\webdriver
path = "//home//isb//Documents//lat_long_sub_district//"
driver = webdriver.Chrome(executable_path = path_to_chromedriver)
url = r'http://india.csis.u-tokyo.ac.jp/default/single'
driver.get(url) 
driver.wait = WebDriverWait(driver, 2)
##//*[@id="state_list"]/option[16]
driver.find_element_by_xpath('//*[@id="state_list"]/option[15]').click() #chooses state - J&K, Himachal
#//*[@id="query_name"] //*[@id="query_name"]//*[@id="state_list"]/option[15]
#//*[@id="query_form"]/text()

names = pd.read_csv(path+"rdir.csv")

for i in range(7772,len(names)-1): #len(names.names_sub_district)-1 #Hajinar
    sub_district =names.name2001[i]
    dtc2001=int(names.dtc2001[i])
    dtc2001=str(dtc2001)
    #print len(dtc2001)
    if len(dtc2001)==1:
        dtc="0"+dtc2001
    else:
        dtc=dtc2001
        
    subdt2001=int(names.subdt2001[i])
    subdt2001=str(subdt2001)   
    if len(subdt2001)==1:
        subdt="000"+subdt2001
    elif len(subdt2001)==2:
        subdt="00"+subdt2001
    elif len(subdt2001)==3:
        subdt="0"+subdt2001
    else:
        subdt=subdt2001
    
    plcn2001=int(names.plcn2001[i])
    plcn2001=str(plcn2001)
    if len(plcn2001)==3:
        plc="00000"+plcn2001
    elif len(plcn2001)==4:
        plc="0000"+plcn2001
    elif len(plcn2001)==5:
        plc="000"+plcn2001
    elif len(plcn2001)==6:
        plc="00"+plcn2001
    elif len(plcn2001)==7:
        plc="0"+plcn2001
    else:
        plc=plcn2001
        
    census_code_file = str(int(names.stc2001[i])) + dtc+subdt+plc
    #print census_code
    #//*[@id="locationList"]/table/tbody/tr[1]/td[7]
    driver.find_element_by_xpath('//*[@id="query_name"]').send_keys(sub_district)
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="retrieve"]').click() #//*[@id="retrieve"]
    time.sleep(3)
    soup = BeautifulSoup(driver.page_source,"html.parser")
    tag_body = soup.body
    tag_tr = tag_body.find_all("tr")
    tag_tr_1 = tag_tr[2]
    tag_td = tag_tr_1.find_all("td")
    for i in range(1,len(tag_tr)-1):
        ##//*[@id="locationList"]/table/tbody/tr[1]/td[7]
        census_code_html=driver.find_element_by_xpath('//*[@id="locationList"]/table/tbody/tr['+str(i)+']/td[7]').text
        #print census_code_html
        if int(census_code_html) == int(census_code_file): 
            data_all=pd.DataFrame()
            for j in range(0, len(tag_td)):
                data = tag_td[j].get_text(",",strip=True)
                data_list = data.split('_')
                df=pd.DataFrame(data_list)
                data_all=data_all.append(df)
                #print data_all
                
            data_all=data_all.T
            #print data_all
            data_all.to_csv(path+"lat_long_trial.csv", header = False, index = False, mode = 'a', encoding = 'utf-8')
    driver.find_element_by_xpath('//*[@id="query_name"]').clear()
        #break    
    

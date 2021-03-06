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
path_to_chromedriver = '../../chromedriver' ##C:\Anaconda\selenium\webdriver

driver = webdriver.Chrome(executable_path = path_to_chromedriver)
url = r'http://agcensus.dacnet.nic.in/StateSizeClass.aspx'
driver.get(url) 
driver.wait = WebDriverWait(driver, 2)


#print(sizeclass_Val)
varfilename = "agcensus_column_names.csv"
#input_path = r'./' ##C:\Users\malaniaayushi\Desktop
#agcensus_vars = pd.read_csv(input_path + varfilename)
#columns =list(agcensus_vars.sources_of_irrigation)
#col_string = ','.join(columns)



driver.find_element_by_xpath('//*[@id="_ctl0_ContentPlaceHolder1_DropDownList5"]/option[1]').click()
time.sleep(3) # wait for browser


driver.find_element_by_xpath('//*[@id="_ctl0_ContentPlaceHolder1_DropDownList4"]/option[1]').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="_ctl0_ContentPlaceHolder1_Dropdownlist2"]//option[4]').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="_ctl0_ContentPlaceHolder1_DropDownList1"]/option[2]').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="_ctl0_ContentPlaceHolder1_DropDownList3"]/option[4]').click()
time.sleep(2)
driver.find_element_by_id("_ctl0_ContentPlaceHolder1_Submit").click()
time.sleep(4)
    
soup=BeautifulSoup(driver.page_source,"html.parser")
tag_body = soup.body
tag_table =tag_body.find_all("table")
tag_data = tag_table[3]
tag_tr = tag_data.find_all("tr")
data_all = pd.DataFrame()
samplist=[]
for i in range(3,len(tag_tr)): 
    data = tag_tr[i].get_text(",", strip = True)
    data = data.replace(" ","")
    data_string = data.encode('utf-8')
    data_list = data_string.split()
    df = pd.DataFrame(data_list)
    data_all = data_all.append(df)
        
#print data_all

data_all.to_csv('C:\Users\malaniaayushi\Desktop\sample_2.csv', header = False, index = False, sep='\t') 
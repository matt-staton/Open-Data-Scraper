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

tabUrlBody = "http://agcensus.dacnet.nic.in/sizestatedisplay" # url use later to navigate to other tables

sizeclass_Select = Select(driver.find_element_by_id("_ctl0_ContentPlaceHolder1_DropDownList5")) # retrieve all sizeclasses

sizeclass_val = {}
for val in sizeclass_Select.options:
    sizeclass_val[val.get_attribute('value')] = val.text # populate all sizeclasses


socialgroup_select = Select(driver.find_element_by_id("_ctl0_ContentPlaceHolder1_DropDownList4")) # social groups
socialgroup_val = {}
for val in socialgroup_select.options:
    socialgroup_val[val.get_attribute('value')] = val.text # populate social groups

url_append = ['3','2a','4','5a','6a','7'] # table numbers to be appended to tabUrlBody


for sizeclass in sizeclass_val.keys(): # loop through each sizeclass
    driver.find_element_by_xpath('//*[@id="_ctl0_ContentPlaceHolder1_DropDownList5"]/option[@value=' + sizeclass + ']').click()
    time.sleep(3) # wait for browser

    for socialgroup in socialgroup_val.keys(): # through each socialgroup
        driver.find_element_by_xpath('//*[@id="_ctl0_ContentPlaceHolder1_DropDownList4"]/option[@value=' + socialgroup + ']').click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="_ctl0_ContentPlaceHolder1_Dropdownlist2"]//option[4]').click() # select AP
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="_ctl0_ContentPlaceHolder1_DropDownList1"]/option[2]').click() # select 2010-11
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="_ctl0_ContentPlaceHolder1_DropDownList3"]/option[3]').click() # select landuse
        time.sleep(2)
        

        for table in url_append: # navigate through each table and write
            if table == '3':
                driver.find_element_by_id("_ctl0_ContentPlaceHolder1_Submit").click() # click once only for landuse
                time.sleep(4)
                continue
            driver.get(tabUrlBody + table + ".aspx")
            time.sleep(3)
            soup=BeautifulSoup(driver.page_source,"html.parser")
            tag_body = soup.body
            tag_table =tag_body.find_all("table")
            tag_data = tag_table[3]
            tag_tr = tag_data.find_all("tr")
            data_all = pd.DataFrame()
            samplist=[]
            for i in range(3,len(tag_tr)): 
                data = tag_tr[i].get_text(",", strip = True)
                data_string = data.encode('utf-8')
                data_list = data_string.split()
                df = pd.DataFrame(data_list)
                data_all = data_all.append(df)
            # #print data_all
            
            data_all.to_csv('./sample'+table+'.csv', header = False, index = False, sep='\t', mode = 'a', encoding = 'utf-8')
            time.sleep(3)
            

        driver.execute_script("window.history.go(-6)")# navigate back to mainpage without losing selections
        time.sleep(10)
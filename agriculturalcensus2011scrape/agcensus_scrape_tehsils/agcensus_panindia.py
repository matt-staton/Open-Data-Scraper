# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

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

driver = webdriver.Chrome(executable_path = path_to_chromedriver)
url = r'http://agcensus.dacnet.nic.in/DistSizeClass.aspx'
driver.get(url) 
driver.wait = WebDriverWait(driver, 2)

tabUrlBody = "http://agcensus.dacnet.nic.in/dtsizedisplay" # url use later to navigate to other tables

driver.find_element_by_xpath('//*[@id="_ctl0_ContentPlaceHolder1_DropDownList5"]/option[1]').click() # select landuse
time.sleep(2) #keeping size class constant # option 1->below 0.5
driver.find_element_by_xpath('//*[@id="_ctl0_ContentPlaceHolder1_Dropdownlist2"]//option[4]').click() # select 2010-11
time.sleep(2) # always constant 

### populate all states ###
state_select = Select(driver.find_element_by_xpath('//*[@id="_ctl0_ContentPlaceHolder1_DropDownList1"]'))
state_val = {}
for val in state_select.options:
    state_val[val.get_attribute('value')] = val.text

#####--------populate all social groups--------#####
socialgroup_select = Select(driver.find_element_by_id("_ctl0_ContentPlaceHolder1_DropDownList4")) 
socialgroup_val = {}
for val in socialgroup_select.options:
    socialgroup_val[val.get_attribute('value')] = val.text # populate social groups
    
url_append = ['3','2a','4','5a','6a','7' ] # table numbers to be appended to tabUrlBody
#2a tenancy, 3 land use, 4 irrigation status, 5a sources of irrigation 6a gross croppd area,#7 dispersal of operated

for state in state_val.keys(): # loop through each state
    driver.find_element_by_xpath('//*[@id="_ctl0_ContentPlaceHolder1_DropDownList1"]/option[@value=' + state + ']').click()
    time.sleep(2) # wait for browser
    #select all district for a particular state#
    district_select = Select(driver.find_element_by_id("_ctl0_ContentPlaceHolder1_DropDownList6")) # district
    district_val = {}
    for val in district_select.options:
        district_val[val.get_attribute('value')] = val.text # populate districts

    for district in district_val.keys(): # through each district
        driver.find_element_by_xpath('//*[@id="_ctl0_ContentPlaceHolder1_DropDownList6"]/option[@value=' + district +']').click()
        time.sleep(2)
        
        for socialgroup in socialgroup_val.keys(): # through each socialgroup
            driver.find_element_by_xpath('//*[@id="_ctl0_ContentPlaceHolder1_DropDownList4"]/option[@value=' + socialgroup + ']').click()
            time.sleep(2)
            
            fixed_val = state_val[state] + ',' + district_val[district] + ',' + socialgroup_val[socialgroup] + ',' + 'Below 0.5' +','  # add sizegroup, social class, and state column values

            for table in url_append: # navigate through each table and write
                if table == '3':
                    driver.find_element_by_id("_ctl0_ContentPlaceHolder1_Submit").click() # click once only for landuse
                    time.sleep(3)
                    
                driver.get(tabUrlBody + table + ".aspx") # navigate to table page
                time.sleep(3)
                ##### ------ scrape data ------ #####
                soup=BeautifulSoup(driver.page_source,"html.parser")
                tag_body = soup.body
                if soup.td.string =="No Records found":
                    continue
                tag_table =tag_body.find_all("table")
                tag_data = tag_table[3]
                tag_tr = tag_data.find_all("tr")
                data_all = pd.DataFrame()
                #samplist=[]
                for i in range(3,len(tag_tr)-1): #exclude 'all districts'
                    data = fixed_val + tag_tr[i].get_text(",", strip = True)
                    data_list = data.split('_') # dummy string to ensure that default splitting over ' ' does not happen
                    #print data_list
                    df = pd.DataFrame(data_list)
                    data_all = data_all.append(df)
                
                data_all.to_csv('//home//isb//Documents//agcensus_scrape//table_'+table+'.csv', header = False, index = False, sep='\t', mode = 'a', encoding = 'utf-8')
                time.sleep(3)
                

            driver.execute_script("window.history.go(-6)")# navigate back to mainpage without losing selections
            time.sleep(2)

# <codecell>

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

driver = webdriver.Chrome(executable_path = path_to_chromedriver)
url = r'http://agcensus.dacnet.nic.in/DistSizeClass.aspx'

# <codecell>



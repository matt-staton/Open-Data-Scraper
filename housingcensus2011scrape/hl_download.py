
import pandas as pd
from pandas import DataFrame, Series
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
import os
import shutil

path_to_chromedriver = '//home//isb//Downloads//chromedriver' ##C:\Anaconda\selenium\webdriver
driver = webdriver.Chrome(executable_path = path_to_chromedriver)
#table_names_hh = ("01","02A","02B","02C","03","04","05","06","07","08","09","10","11","12","13")
table_names_hl = ("01", "02","03A", "03B", "03C","04","05")
url_total = "http://www.censusindia.gov.in/2011census/Hlo-series/Hl-data/DDW-HL"
readfile_path = "//home//isb//Downloads//DDW-HH"
output_path = "//home//isb//Documents//nikita//scrapping_data//Open-Data-Scraper//housingcensus2011scrape//DDW-HL"
x=1

for i in table_names_hl: #table names 
    # url_categories = url + i + ".html"
    # print url_categories
    

    if len(str(x))==1:
        x1 = "0"+str(x)
    else:
        x1 = str(x)
    url_total1 = url_total + x1 + i
    #print url_total1
    data_all = pd.DataFrame()
    for j in range(0,36):
        if len(str(j))==1:
            state_code = "0" +str(j)+"00.xls"
        else:
            state_code = str(j) + "00.xls"
        url_final = url_total1 + "-" +state_code
        #print url_final
        driver.get(url_final) 
        #print url_final
        #driver.wait = WebDriverWait(driver, 10)
        #data = pd.read_excel(readfile_path + x1 + i +"-" +state_code)
        #data_all = data_all.append(data)   
    #data_all.to_csv(output_path+str(i)+".csv")
    x= x+1


    #http://www.censusindia.gov.in/2011census/Hlo-series/HH01.html    
    #http://www.censusindia.gov.in/2011census/Hlo-series/Hl-data/DDW-HH0101-0000.xls
    #http://www.censusindia.gov.in/2011census/Hlo-series/Hl-data/DDW-HH0201C-0000.xls
    #http://www.censusindia.gov.in/2011census/Hlo-series/Hl-data/DDW-HH0301T-0000.xls
    
    #http://www.censusindia.gov.in/2011census/Hlo-series/Hl-data/DDW-HH0101-1800.xls
    #http://www.censusindia.gov.in/2011census/Hlo-series/Hl-data/DDW-HH0201C-1800.xls
    #http://www.censusindia.gov.in/2011census/Hlo-series/Hl-data/DDW-HH0301T-1800.xls
    
    #http://www.censusindia.gov.in/2011census/Hlo-series/HH2A.html
    #http://www.censusindia.gov.in/2011census/Hlo-series/Hl-data/DDW-HH0402A-0000.xls
    #http://www.censusindia.gov.in/2011census/Hlo-series/Hl-data/DDW-HH0502AC-0000.xls
    #http://www.censusindia.gov.in/2011census/Hlo-series/Hl-data/DDW-HH0602AT-0000.xls
    
    #http://www.censusindia.gov.in/2011census/Hlo-series/HH2B.html
    #http://www.censusindia.gov.in/2011census/Hlo-series/Hl-data/DDW-HH0702B-0000.xls
    #http://www.censusindia.gov.in/2011census/Hlo-series/Hl-data/DDW-HH0802BC-0000.xls

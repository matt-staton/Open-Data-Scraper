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

path_to_chromedriver = 'C:\Anaconda\selenium\webdriver\chromedriver' ##C:\Anaconda\selenium\webdriver

driver = webdriver.Chrome(executable_path = path_to_chromedriver)
url = r'http://www.censusindia.gov.in/2011census/dchb/DCHB_Village_Release_'#3500.xlsx'
readfile_path = "C:\Users\malaniaayushi\Downloads\DCHB_Village_Release_"
output_path = "C:\Users\malaniaayushi\Desktop\data_all.csv"

data_all = pd.DataFrame()

for i in range(1,36):
    if len(str(i))==1:
        state_code = "0" + str(i) +"00.xlsx"
         
    else:
        state_code = str(i) +"00.xlsx"
    url_state = url + state_code
    print url_state
    driver.get(url_state) 
    driver.wait = WebDriverWait(driver, 100)
    data = pd.read_excel(readfile_path + state_code)
    data_all = data_all.append(data)
data_all.to_csv(output_path)


from bs4 import BeautifulSoup
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

soup = BeautifulSoup(html)
path_to_chromedriver = 'C:\Anaconda\selenium\webdriver\chromedriver' ##C:\Anaconda\selenium\webdriver

driver = webdriver.Chrome(executable_path = path_to_chromedriver)
url = r'http://www.censusindia.gov.in/2011census/dchb/DCHB.html'
driver.get(url) 
driver.wait = WebDriverWait(driver, 2)

soup=BeautifulSoup(driver.page_source,"html.parser")

#driver.find_element_by_partial_link_text('DCHB_Village').click()
driver.find_element_by_link_text('DCHB_Village_Release_3500.xlsx').click()

time.sleep(2)


#tbody_result=soup.find_all("tbody")
#tag_tr = tbody_result[4].find_all("tr")
#result_td = tag_tr[7].find_all("td")
#driver_td = result_td[3]
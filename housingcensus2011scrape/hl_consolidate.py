
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

readfile_path = "//home//isb//Downloads//DDW-HL"
#url_total = "http://www.censusindia.gov.in/2011census/Hlo-series/Hl-data/DDW-HH"
output_path = "//home//isb//Documents//nikita//scrapping_data//Open-Data-Scraper//housingcensus2011scrape//DDW-HL"
table_names_hl = ("01", "02","03A", "03B", "03C","04","05")


x=1
for i in table_names_hl: #table names 
    # url_categories = url + i + ".html"
    # print url_categories
    

    if len(str(x))==1:
        x1 = "0"+str(x)
    else:
        x1 = str(x)
    readfile_path1 = readfile_path + x1 + i
    #output_path1 = output_path +x1+i
    
    table_folder = "//home//isb//Documents//nikita//scrapping_data//Open-Data-Scraper//housingcensus2011scrape//HL_table_" + i
    os.makedirs(table_folder)
    #print url_total1
    output_path1 = table_folder + "//DDW-HH" + x1 + i
    data_all = pd.DataFrame()
    for j in range(0,36):
        if len(str(j))==1:
            state_code = "0" +str(j)+"00.xls"
        else:
            state_code = str(j) + "00.xls"
        #url_final = url_total1 + "-" +state_code
        old_loc = readfile_path1 + "-" + state_code
        new_loc = output_path1 + "-" + state_code
        if os.path.exists(old_loc) == False:
            print "HH_table_" + x1 + i +"T" + "-" + state_code
        else:
            shutil.move(old_loc, new_loc)
    x=x+1

###################################################33

import gzip
import pandas as pd
from pandas import DataFrame, Series
import shutil
import xlrd
import os
path ="//home//isb//Documents//nikita//housing_census_2011//housingcensus2011scrape//HL_table_"
#folder_name = ("01C","02AC","02BC",..)
#folder_name =("01","02A","02B","02C","03","04","05","06","07","08","09","10","11","12","13")
folder_name = ("01","02","03A","03B","03C","04","05")
#goes to folder containing files that need to be consolidated
x=1
for i in folder_name:
    if len(str(x))==1:
        x1="0"+str(x)
    else:
        x1=str(x)
    table_name = 'HL'+x1+i
    folder_path = path + i +"//DDW-HH"+x1+i+"-"
    # 1st folder_path = //home//...//hh_SC_alltables_allstates//HH-table-01T//DDW-HH0101-
    data_all = pd.DataFrame()
    for j in range(0,36):
        if len(str(j))==1:
            state_code = "0" +str(j)+"00.xls"
        else:
            state_code = str(j) + "00.xls"
        file_path = folder_path +state_code
        # filename = DDW-HH0101-0100.xls
        if os.path.exists(file_path):
            data = pd.read_excel(file_path)
            frst_col = str(data.columns[0]) #getting name of first column
            idx = data[data[frst_col]==table_name].index.tolist() #getting indexes of rows which need to be read
            data = data.loc[idx] #getting corresponding to those rows indexes
            data_all = data_all.append(data)
    data_all.to_csv(folder_path + "all.csv", index=False,encoding = 'utf-8')
    #compresses the consolidated files
    with open(folder_path+"all.csv", 'rb') as f_in, gzip.open(folder_path+"all.csv.gz", 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)
    x=x+1

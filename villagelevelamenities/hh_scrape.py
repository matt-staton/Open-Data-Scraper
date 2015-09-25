path_to_chromedriver = 'C:\Anaconda\selenium\webdriver\chromedriver' ##C:\Anaconda\selenium\webdriver

driver = webdriver.Chrome(executable_path = path_to_chromedriver)
#url = r'http://www.censusindia.gov.in/2011census/Hlo-series/HH'#3500.xlsx'
output_path = "C:\Users\malaniaayushi\Desktop\data_housing.csv"
data_all = pd.DataFrame()
#table_names_hh = {"01","02A", "02B", "02C","03","04","05","06","07","08","09","10","11","12","13"}
table_names_hh = {"01"}
table_names_h = {"1", "2","3A", "3B", "3C","4","5"}

for i in table_names_hh: #table names 
    # url_categories = url + i + ".html"
	# print url_categories
    url_total = "http://www.censusindia.gov.in/2011census/Hlo-series/Hl-data/DDW-HH"
    x=1
    if len(str(x))==1:
        x1 = "0"+str(x)
    else:
        x1 = str(x)
    url_total1 = url_total + x1 + i
    print url_total1
    
    for j in range(0,36):
        if len(str(j))==1:
            state_code = "0" +str(j)+"00.xls"
        else:
            state_code = str(j) + "00.xls"
        url_final = url_total1 + "-" +state_code
        print url_final
    x= x+3
		
		
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
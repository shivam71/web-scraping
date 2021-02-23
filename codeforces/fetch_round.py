import sys
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
PATH ="C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
link     = "https://codeforces.com/contest/"+sys.argv[1]
contest_number = sys.argv[1]
#try:
    #os.mkdir(contest_number)
#except:
    #print("you have already downloaded problems for this contest")
    #quit
#os.chdir("./"+contest_number)
driver.get(link)
table = driver.find_element_by_class_name("problems")
tbody = table.find_element_by_tag_name("tbody")
tr = tbody.find_elements_by_tag_name("tr")
for i in range(1,len(tr)):
    td = tr[i].find_element_by_tag_name("td")
    if td != None:
        
        print(td.text)
        link = td.find_element_by_link_text(td.text)
        print(link)

    
#rows = table.find_elements_by_tag_name("td")
#print(len(rows))
#for row in rows:
    #part = row.find_element_by_tag_name("a")
    #print(part.text)

    
    


time.sleep(10)
driver.quit()



#try:
    #os.mkdir(contest_number)
#except:
    #print("you have already downloaded problems for this contest")
    #quit
#os.chdir("./"+contest_number)
#for 
# make directories inside this folder
#os.mkdir()
# argv list of the command line arguments that are passed 


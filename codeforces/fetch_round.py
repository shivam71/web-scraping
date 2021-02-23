import sys
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
        part = td.txt#A , B ......
        print(td.text)
        os.mkdir(td.txt)
        link = td.find_element_by_link_text(td.text)

        link.click()
        try:
         element = WebDriverWait(driver, 10).until(
         EC.presence_of_element_located((By.CLASS_NAME, "problem-statement"))
         )
         os.chdir("./"+td.txt)
         element.screenshot_as_png("problem.png")
         # MORE THAN ONE OUTPUT INPUT SO TAKE CARE
         
         outputs = driver.find_elements_by_class_name("output")
         inputs =  driver.find_elements_by_class_name("input")
         for output in outputs:
             print(output.txt)
         for Input in inputs:
             print(Input.txt)
         os.chdir("..")# check is ../
         # now we have to go back to previous page and do the same for thr other parts 
        except:
         driver.quit()
        # go back to pervious page
        # link click then screen shot and input output files 

    
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


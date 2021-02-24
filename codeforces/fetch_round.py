import sys
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
options = Options()
options.headless = True
PATH ="C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH,options=options)

link     = "https://codeforces.com/contest/"+sys.argv[1]
contest_number = sys.argv[1]
try:
    os.mkdir(contest_number)
except:
    print("you have already downloaded problems for this contest")
    quit
os.chdir("./"+contest_number)
driver.get(link)
table = driver.find_element_by_class_name("problems")
tbody = table.find_element_by_tag_name("tbody")
tr = tbody.find_elements_by_tag_name("tr")
for i in range(1,len(tr)):
        td = tr[i].find_element_by_tag_name("td")
        part = td.text#A , B ......
        print(td.text)
        os.mkdir(part)
        os.chdir("./"+td.text)
        link = td.find_element_by_link_text(td.text)

        link.click()
        
        element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "problem-statement"))
        )
        S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
        driver.set_window_size(S('Width'),S('Height')) # May need manual adjustment
        element.screenshot("problem.png")
         # MORE THAN ONE OUTPUT INPUT SO TAKE CARE
         
        outputs = driver.find_elements_by_class_name("output")
        inputs =  driver.find_elements_by_class_name("input")
        counter = 1
        for output in outputs:
            results = output.find_element_by_tag_name("pre")
            file_h= open("output"+str(counter)+".txt","at")
            file_h.write(results.text)
            print(results.text)
            counter+=1
            file_h.close()
        counter = 1
        for Input in inputs:
             tests = Input.find_element_by_tag_name("pre")
             file_h= open("input"+str(counter)+".txt","at")
             file_h.write(tests.text)
             print(tests.text)
             counter+=1
             file_h.close()

        os.chdir("..")# check is ../
        driver.back()
        table = driver.find_element_by_class_name("problems")
        tbody = table.find_element_by_tag_name("tbody")
        tr = tbody.find_elements_by_tag_name("tr")
        
      
         # now we have to go back to previous page and do the same for thr other parts 
        
         
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


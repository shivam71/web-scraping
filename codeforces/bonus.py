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
PATH ="../chromedriver.exe"
driver = webdriver.Chrome(PATH,options=options)
print("Using chromedriver in headless option")
link_home = "https://codeforces.com/contests"
driver.get(link_home)
contest_table = driver.find_element_by_class_name("contests-table")
data_table = driver.find_element_by_class_name("datatable")
table = contest_table.find_element_by_tag_name("table")
contests_links = table.find_elements_by_link_text("Enter »")
next_page = driver.find_element_by_link_text("→")


list_hrefs = [contests_links[i].get_attribute("href")  for i in range(len(contests_links))]

last_x= int(sys.argv[1])

k = 0
j = last_x
while(j !=0):
    
 if k > len(list_hrefs):# if page change required 
     k = 0 
     driver.get(link_home)
     next_page = driver.find_element_by_link_text("→")
     next_page.click()
     contest_table = driver.find_element_by_class_name("contests-table")
     data_table = driver.find_element_by_class_name("datatable")
     table = contest_table.find_element_by_tag_name("table")
     contests_links = table.find_elements_by_link_text("Enter »")
     next_page = driver.find_element_by_link_text("→")
     list_hrefs = [contests_links[f].get_attribute("href")  for f in range(len(contests_links))]

     

 driver.get(list_hrefs[k])

 contest_number=driver.current_url.split("/")[4]

 try:
            os.mkdir(contest_number)
 except:
            print("you have already downloaded problems for this contest")
            quit
 os.chdir("./"+contest_number)
 table = driver.find_element_by_class_name("problems")
 tbody = table.find_element_by_tag_name("tbody")
 tr = tbody.find_elements_by_tag_name("tr")
 for i in range(1,len(tr)):
        td = tr[i].find_element_by_tag_name("td")
        part = td.text
        
        
        os.mkdir(part)
        os.chdir("./"+td.text)
        link = td.find_element_by_link_text(td.text)

        link.click()
        
        element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "problem-statement"))
        )
        S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
        driver.set_window_size(S('Width'),S('Height')) 
        element.screenshot("problem.png")
         
         
        outputs = driver.find_elements_by_class_name("output")
        inputs =  driver.find_elements_by_class_name("input")
        counter = 1
        for output in outputs:
            results = output.find_element_by_tag_name("pre")
            file_h= open("output"+str(counter)+".txt","at")
            file_h.write(results.text)
            
            counter+=1
            file_h.close()
        counter = 1
        for Input in inputs:
             tests = Input.find_element_by_tag_name("pre")
             file_h= open("input"+str(counter)+".txt","at")
             file_h.write(tests.text)
            
             counter+=1
             file_h.close()

        os.chdir("..")
        driver.back()
        table = driver.find_element_by_class_name("problems")
        tbody = table.find_element_by_tag_name("tbody")
        tr = tbody.find_elements_by_tag_name("tr")
 os.chdir("..")  
 k+=1
 j-=1
time.sleep(10)
print("completed")
driver.quit()
 

        





































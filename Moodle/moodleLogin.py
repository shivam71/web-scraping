from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
PATH ="../chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://moodle.iitd.ac.in/login/index.php")
us = driver.find_element_by_id("username")
ps = driver.find_element_by_id("password")


text = driver.find_element_by_id("login").text
capcha_text = text.split("\n")[3]
var = capcha_text.split(" ")
if capcha_text.find(",") == -1:# means add or subtract
       n1 = int(var[2])
       n2 = int(var[4])
       
       if var[3] == "-":
            capcha_v=(n1-n2)
            
       else:
           capcha_v =(n1+n2)
           

else:
    if var[2] == "first":
        
        capcha_v=int(var[4])
        

    else:
        
        capcha_v=int(var[6])




capcha_box = driver.find_element_by_id("valuepkg3")
capcha_box.send_keys(capcha_v)
username = input("USERNAME:")
password = input("PASSWORD")
us.send_keys(username)
ps.send_keys(password)



login_button = driver.find_element_by_id("loginbtn")
login_button.send_keys(Keys.RETURN)





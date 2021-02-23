from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
PATH ="C:\Program Files (x86)\chromedriver.exe"
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
       print(n1,n2)
       if var[3] == "-":
            capcha_v=(n1-n2)
            
       else:
           capcha_v =(n1+n2)
           

else:
    if var[2] == "first":
        print(var[4])
        capcha_v=int(var[4])
        

    else:
        print(var[6])
        capcha_v=int(var[6])



print(capcha_v)
username = input("USERNAME:")
password = input("PASSWORD")
us.send_keys(username)
ps.send_keys(password)

capcha_box = driver.find_element_by_id("valuepkg3")
capcha_box.send_keys(capcha_v)

login_button = driver.find_element_by_id("loginbtn")
login_button.send_keys(Keys.RETURN)


time.sleep(10)
driver.quit()

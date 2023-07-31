import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj= Service("C:\\Users\\user\\Drivers\\chromedriver.exe")

driver= webdriver.Chrome(service =service_obj)
driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.maximize_window()

#1.scroll down page by pixel
# driver.execute_script("window.scrollBy(0,3000)","")
# value=driver.execute_script("return window.pageYOffset;")
# print(value)#3000

#2.scroll down page by visible_text
# flag=driver.find_element(By.XPATH,"//td[normalize-space()='India']")
# driver.execute_script("arguments[0].scrollIntoView();",flag)
# value=driver.execute_script("return window.pageYOffset;")
# print(value)#5003.2001953125

#3.scroll down page till End
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
value=driver.execute_script("return window.pageYOffset;")
print(value)#5998.39990234375
time.sleep(3)
#4.scroll up for starting
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
time.sleep(3)



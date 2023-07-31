import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

service_obj= Service("C:\\Users\\user\\Drivers\\chromedriver.exe")

driver= webdriver.Chrome(service =service_obj)
driver.get(" https://text-compare.com/")
# driver.maximize_window()

input1=driver.find_element(By.XPATH,"//textarea[@id='inputText1']")
input2=driver.find_element(By.XPATH,"//textarea[@id='inputText2']")
input1.send_keys('Welcome ra mawa')
#Ctrl A
act= ActionChains(driver)
# act.key_down(keys.CONTROL)
# act.send_keys("a")
# act.key_up(keys.CONTROL)
# act.perform()
act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
#Ctrl C
# act.key_down(keys.CONTROL)
# act.send_keys("a")
# act.key_up(keys.CONTROL)
# act.perform()
act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()
#Ctrl TAB
act.send_keys(Keys.TAB).perform()
#Ctrl P
# act.key_down(keys.CONTROL)
# act.send_keys("a")
# act.key_up(keys.CONTROL)
# act.perform()
act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()

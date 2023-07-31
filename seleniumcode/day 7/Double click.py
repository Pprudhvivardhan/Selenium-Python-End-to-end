import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj= Service("C:\\Users\\user\\Drivers\\chromedriver.exe")

driver= webdriver.Chrome(service =service_obj)
driver.get(" https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_ev_ondblclick")
# driver.implicitly_wait(10)

driver.switch_to.frame("iframeResult")
button=driver.find_element(By.XPATH,"//button[@ondblclick='myFunction()']")
act = ActionChains(driver)
act.double_click(button).perform()#Performs double click
time.sleep(3)
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj= Service("C:\\Users\\user\\Drivers\\chromedriver.exe")

driver= webdriver.Chrome(service =service_obj)
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.implicitly_wait(10)

act=ActionChains(driver)
rome=driver.find_element(By.ID,"box6")
italy=driver.find_element(By.ID,"box106")
act.drag_and_drop(rome,italy).perform()

time.sleep(2)
washinton=driver.find_element(By.ID,"box3")
Usa=driver.find_element(By.ID,"box103")
act.drag_and_drop(washinton,Usa).perform()
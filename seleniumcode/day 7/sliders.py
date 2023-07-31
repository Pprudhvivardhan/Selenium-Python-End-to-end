import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj= Service("C:\\Users\\user\\Drivers\\chromedriver.exe")

driver= webdriver.Chrome(service =service_obj)
driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")
driver.maximize_window()

min=driver.find_element(By.XPATH," (//span[@class='ui-slider-handle ui-corner-all ui-state-default'])[1]")
max=driver.find_element(By.XPATH," (//span[@class='ui-slider-handle ui-corner-all ui-state-default'])[2]")
print("before drag and drop")
print(min.location)#{'x': 59, 'y': 251}
print(max.location)#{'x': 613, 'y': 251}

act=ActionChains(driver)
act.drag_and_drop_by_offset(min,100,0).perform()
act.drag_and_drop_by_offset(max,-40,0).perform()
time.sleep(3)

print("After drag and drop")
print(min.location)#{'x': 159, 'y': 251}
print(max.location)#{'x': 574, 'y': 251}


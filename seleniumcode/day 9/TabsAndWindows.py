from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os
service_obj= Service("C:\\Users\\user\\Drivers\\chromedriver.exe")

driver= webdriver.Chrome(service =service_obj)
# driver.get(" https://demo.nopcommerce.com/")
# driver.maximize_window()
# reglink = Keys.CONTROL + Keys.RETURN
# driver.find_element(By.LINK_TEXT,"Register").send_keys(reglink)

#open new tab and switches to new tab
# driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
# driver.switch_to.new_window("tab")
# driver.get("https://demo.nopcommerce.com/")

#open new window and switches to new window
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.switch_to.new_window("window")
driver.get("https://demo.nopcommerce.com/")
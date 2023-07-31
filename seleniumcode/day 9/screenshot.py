from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os
service_obj= Service("C:\\Users\\user\\Drivers\\chromedriver.exe")

driver= webdriver.Chrome(service =service_obj)
driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.maximize_window()
# driver.save_screenshot("C:\\Users\\user\\PycharmProjects\\ selenium\\day 9\\home.png")
# driver.save_screenshot(os.getcwd()+"\\home.png")
# driver.get_screenshot_as_file(os.getcwd()+"\\home.png")
driver.get_screenshot_as_base64()
driver.quit()
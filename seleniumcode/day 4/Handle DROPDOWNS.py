import time

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select

service_object = Service('C:\\Users\\user\\PycharmProjects\\ selenium\\day 1 selenium\\chromedriver.exe')

driver =webdriver.Chrome(service=service_object)
driver.maximize_window()
driver.get("https://www.opencart.com/index.php?route=account/register")

drop_element=Select(driver.find_element(By.XPATH,"//select[@id='input-country']"))

# 1.select option from dropdown
# drop_element.select_by_visible_text('India')
# time.sleep(2)
# drop_element.select_by_index(10)
# time.sleep(2)
# drop_element.select_by_value('3')
# time.sleep(2)
# 2.select all options from dropdown
alloptions=drop_element.options
print('selecting all options:', len(alloptions))
# for i in alloptions:
#     print(i.text)
# 3. select option with logic
for i in alloptions:
    if i.text=='India':
        i.click()
        break






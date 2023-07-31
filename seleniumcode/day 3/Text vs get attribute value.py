import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service_object = Service('C:\\Users\\user\\PycharmProjects\\ selenium\\day 1 selenium\\chromedriver.exe')

driver =webdriver.Chrome(service=service_object)
driver.get('https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F')
emailbox=driver.find_element(By.XPATH,"//input[@value='admin@yourstore.com']")
time.sleep((2))
emailbox.clear()
emailbox.send_keys('abcdef@gmail.com')
print('result of test:',emailbox.text) # printed nothing
print('result of get_att:',emailbox.get_attribute('value')) #abcdef@gmail.com
#Button
button = driver.find_element(By.XPATH,"//button[@type='submit']")
print('result of button:',button.text) #
print('result of button get_att:',button.get_attribute('value'))

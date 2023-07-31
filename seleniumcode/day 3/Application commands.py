from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service_object = Service('C:\\Users\\user\\PycharmProjects\\ selenium\\day 1 selenium\\chromedriver.exe')

driver =webdriver.Chrome(service=service_object)
driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
print(driver.title)#OrangeHRM
print(driver.current_url) #https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
print(driver.page_source)
driver.close()
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service_object = Service('C:\\Users\\user\\PycharmProjects\\ selenium\\day 1 selenium\\chromedriver.exe')

driver =webdriver.Chrome(service=service_object)
driver.get('https://www.snapdeal.com/')
driver.get('https://www.amazon.in/')
driver.back() # snapdeal
driver.forward() #amazon
driver.refresh() #reload
driver.quit()
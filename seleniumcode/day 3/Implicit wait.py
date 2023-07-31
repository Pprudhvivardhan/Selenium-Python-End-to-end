import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service_object = Service('C:\\Users\\user\\PycharmProjects\\ selenium\\day 1 selenium\\chromedriver.exe')

driver =webdriver.Chrome(service=service_object)
driver.implicitly_wait(10)
driver.get('https://www.google.com/')
driver.maximize_window()
search=driver.find_element(By.NAME,"q")
search.send_keys('selenium')
search.submit()
#time.sleep(5)
driver.find_element(By.XPATH,"//h3[text()='Selenium']").click()
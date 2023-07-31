import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service_object = Service('C:\\Users\\user\\PycharmProjects\\ selenium\\day 1 selenium\\chromedriver.exe')

driver =webdriver.Chrome(service=service_object)
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")

driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Prompt']").click()
time.sleep(2)
alretwindow=driver.switch_to.alert
print(alretwindow.text)
time.sleep(2)
alretwindow.send_keys('welcome')
time.sleep(2)
# alretwindow.accept() # ok
time.sleep(2)
alretwindow.dismiss() # cancel
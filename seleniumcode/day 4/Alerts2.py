import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service_object = Service('C:\\Users\\user\\PycharmProjects\\ selenium\\day 1 selenium\\chromedriver.exe')

driver =webdriver.Chrome(service=service_object)
driver.maximize_window()
driver.get("https://mail.rediff.com/cgi-bin/login.cgi")
driver.find_element(By.XPATH,"//input[@title='Sign in']").click()
time.sleep(2)
driver.switch_to.alert.accept()
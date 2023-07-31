from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_object = Service('C:\\Users\\user\\PycharmProjects\\ selenium\\day 1 selenium\\chromedriver.exe')

driver = webdriver.Chrome(service=service_object)

driver.get('https://www.facebook.com/login/')

#TAG & ID
driver.find_element(By.CSS_SELECTOR,'input#email').send_keys('abc')
#TAG & CLASSNAME
driver.find_element(By.CSS_SELECTOR,'input.inputtext').send_keys('abcdef')
#TAG & ATTRIBUTE
driver.find_element(By.CSS_SELECTOR,'input[placeholder="Email address or phone number"]').send_keys('abcdffjskdvnksjvd')
#TAG & CLASSNAME & ATTRIBUTE
driver.find_element(By.CSS_SELECTOR,'input.inputtext[autocomplete="current-password"]').send_keys('abc')

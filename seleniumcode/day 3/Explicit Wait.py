from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
service_object = Service('C:\\Users\\user\\PycharmProjects\\ selenium\\day 1 selenium\\chromedriver.exe')

driver =webdriver.Chrome(service=service_object)

mywait =WebDriverWait(driver,10,poll_frequency=2,ignored_exceptions=Exception)


driver.get('https://www.google.com/')
driver.maximize_window()
search=driver.find_element(By.NAME,"q")
search.send_keys('selenium')
search.submit()

searchlink=mywait.until(EC.presence_of_element_located((By.XPATH,"//h3[text()='Selenium']")))
searchlink.click()
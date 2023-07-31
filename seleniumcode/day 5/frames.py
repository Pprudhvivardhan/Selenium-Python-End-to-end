import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service_object = Service('C:\\Users\\user\\PycharmProjects\\ selenium\\day 1 selenium\\chromedriver.exe')

driver =webdriver.Chrome(service=service_object)
driver.maximize_window()
driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?org/openqa/selenium/package-summary.html")

driver.switch_to.frame("packageListFrame")
driver.find_element(By.XPATH,"//a[normalize-space()='org.openqa.selenium']").click()

driver.switch_to.default_content() # switch to main content
driver.switch_to.frame("packageFrame")
driver.find_element(By.XPATH,"//span[normalize-space()='WebDriver']").click()

driver.switch_to.default_content() # switch to main content
driver.switch_to.frame("classFrame")
driver.find_element(By.XPATH,"//div[@class='topNav']//a[normalize-space()='Help']").click()
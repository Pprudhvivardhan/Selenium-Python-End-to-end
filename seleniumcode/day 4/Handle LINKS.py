import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service_object = Service('C:\\Users\\user\\PycharmProjects\\ selenium\\day 1 selenium\\chromedriver.exe')

driver =webdriver.Chrome(service=service_object)
driver.maximize_window()
driver.get("https://demo.nopcommerce.com/")

#CLICK THE LINK
# driver.find_element(By.LINK_TEXT,"Digital downloads").click()
driver.find_element(By.PARTIAL_LINK_TEXT,"Digital").click()

# find links on page
# links=driver.find_elements(By.TAG_NAME,'a') #95 #tagname
# print(len(links))
links=driver.find_elements(By.XPATH,'//a') # 95 #xpath
print(len(links))
for i in links:
    print(i.text)
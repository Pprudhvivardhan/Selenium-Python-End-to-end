import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service_object = Service('C:\\Users\\user\\PycharmProjects\\ selenium\\day 1 selenium\\chromedriver.exe')

driver =webdriver.Chrome(service=service_object)
driver.maximize_window()
driver.get("http://www.deadlinkcity.com/")

allLinks=driver.find_elements(By.TAG_NAME,'a')
count=0
for i in allLinks:
    url=i.get_attribute('href')
    try:
        response=requests.head(url)
    except:
        None
    if response.status_code>=400:
        print('broken links',url)
        count+=1
    else:
        print(url,'valid link')

print ('BROKEN LINKS',count)

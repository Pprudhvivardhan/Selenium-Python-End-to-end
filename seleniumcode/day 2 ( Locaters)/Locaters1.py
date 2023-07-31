from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_object = Service('C:\\Users\\user\\PycharmProjects\\ selenium\\day 1 selenium\\chromedriver.exe')

driver = webdriver.Chrome(service=service_object)

driver.get('https://demo.nopcommerce.com/')
driver.maximize_window()
#ID
#driver.find_element(By.ID,'small-searchterms').send_keys('Asus N551JK-XO076H Laptop')
#NAME
#driver.find_element(By.NAME,'q').send_keys('Asus N551JK-XO076H Laptop')
#LINK TEST
#driver.find_element(By.LINK_TEXT,'Register').click()
#PARTIAL LINK TEST
#driver.find_element(By.PARTIAL_LINK_TEXT,'Reg').click()
#TAGNAME
links=driver.find_elements(By.TAG_NAME ,'a')
print(len(links))

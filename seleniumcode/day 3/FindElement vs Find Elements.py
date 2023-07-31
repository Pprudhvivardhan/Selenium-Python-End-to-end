from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service_object = Service('C:\\Users\\user\\PycharmProjects\\ selenium\\day 1 selenium\\chromedriver.exe')

driver =webdriver.Chrome(service=service_object)
driver.get('https://demo.nopcommerce.com/')
##FIND ELEMENT
# 1.  locates single element

# element=driver.find_element(By.XPATH,"//input[@placeholder='Search store']")
# element.send_keys("Apple MacBook Pro 13-inch")

## 2. locating multiple web elements

# element=driver.find_element(By.XPATH,"//div[@class='footer']//a")
# print(element.text) # printed first link from footer :sitemap

# 3. element not found , it throws error

# element=driver.find_element(By.LINK_TEXT,"Log  ")
# element.click() # throws expection : NO ELEMENT FOUND EXPECTION

##FIND ELEMENTS
#1. Locates single web elements
# elements=driver.find_elements(By.XPATH,"//input[@placeholder='Search store']")
# print(len(elements)) #1- find elements gives web elements in list
# elements[0].send_keys("Apple MacBook Pro 13-inch")
#2. Locates multiple web elements
# elements=driver.find_elements(By.XPATH,"//div[@class='footer']//a")
# print(len(elements)) #23- find elements gives web elements in list
# # print((elements[1].text))
# for i in elements:
    #print(i.text)

# 3. elements not found ,it gives list of zero[0]

element=driver.find_elements(By.LINK_TEXT,"Log  ")
print(len(element))





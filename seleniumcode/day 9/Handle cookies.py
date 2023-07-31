from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service

service_obj= Service("C:\\Users\\user\\Drivers\\chromedriver.exe")

driver= webdriver.Chrome(service =service_obj)
driver.get(" https://demo.nopcommerce.com/")
driver.maximize_window()

#opens cookies
cookies=driver.get_cookies()
print(len(cookies))#3
#
# #prints details of cookies
# for i in cookies:
#     #print(i)
#     # {'domain': 'demo.nopcommerce.com',
#     # 'expiry': 1705738816, 'httpOnly': False,S......'}
#     print(i.get('name'),":",i.get("value"))
#     #.Nop.Customer : 1443d4fe-0074-4e6a-a253-2881c1916ec0

#Add new cookies to the cookies
driver.add_cookie({"name":"Mycookies", "value":"12345"})
cookies=driver.get_cookies()
print("after adding new cookie:",len(cookies))#4
#Deleting cookies
driver.delete_cookie("Mycookies")
cookies=driver.get_cookies()
print("after adding delete cookie:",len(cookies))#3

#All cookies deleted
driver.delete_all_cookies()
cookies=driver.get_cookies()
print("after delete all cookie:",len(cookies))#0



from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service_object = Service('C:\\Users\\user\\PycharmProjects\\ selenium\\day 1 selenium\\chromedriver.exe')

driver =webdriver.Chrome(service=service_object)
driver.get('https://money.rediff.com/gainers')
#SELF
#text_msg=driver.find_element(By.XPATH,'//a[contains(text(),"India Tourism De")]/self::a ').text
#print(text_msg) #India Tourism De
# PARENT
# text_msg=driver.find_element(By.XPATH,'//a[contains(text(),"India Tourism De")]/parent::td').text
# print(text_msg) # India Tourism De
# CHILD
# child=driver.find_elements(By.XPATH,'//a[contains(text(),"India Tourism De")]/ancestor::tr/child::td')
# print(len(child)) #5
#ANCESTOR
# text_msg=driver.find_element(By.XPATH,'//a[contains(text(),"India Tourism De")]/ancestor::tr').text
# print(text_msg) #India Tourism De B 355.40 356.15 + 0.21
#DESCENDET
# descendants=driver.find_elements(By.XPATH,'//a[contains(text(),"India Tourism De")]/ancestor::tr/descendant::*')
# print(len(descendants)) # 7
#FOLLOWING
# following=driver.find_elements(By.XPATH,'//a[contains(text(),"India Tourism De")]/ancestor::tr/following::*')
# print(len(following)) # 5055
#FOLLOWING-SIBLING
followingsibling=driver.find_elements(By.XPATH,'//a[contains(text(),"India Tourism De")]/ancestor::tr/following-sibling::*')
print(len(followingsibling)) # 618
#PRECEDINGS
precedings=driver.find_elements(By.XPATH,'//a[contains(text(),"India Tourism De")]/ancestor::tr/preceding::*')
print(len(precedings))
#PRECEDING-SIBLING
precedingsibling=driver.find_elements(By.XPATH,'//a[contains(text(),"India Tourism De")]/ancestor::tr/preceding-sibling::*')
print(len(precedingsibling))#1541
driver.close()
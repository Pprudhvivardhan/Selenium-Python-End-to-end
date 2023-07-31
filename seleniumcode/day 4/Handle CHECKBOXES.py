import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service_object = Service('C:\\Users\\user\\PycharmProjects\\ selenium\\day 1 selenium\\chromedriver.exe')

driver =webdriver.Chrome(service=service_object)
driver.maximize_window()
driver.get('https://itera-qa.azurewebsites.net/home/automation')
##1.select the specific check box
# driver.find_element(By.XPATH,"//div[4]//label[1]//input[1]").click()
#2.checking the Multiple checkbox
checkbox=driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'day')]")
print(len(checkbox))

#Approach-1
# for i in range(len(checkbox)):
#      checkbox[i].click()

#.Approach-2
for i in checkbox:
    i.click()

#3.checking the Multiple checkbox with choice

# for i in checkbox:
#     weekdays=i.get_attribute('id')
#     if weekdays=='sunday' or weekdays=='friday':
#      i.click()

#4. select last two
# for i in range(len(checkbox)-2,(len(checkbox))):
#     checkbox[i].click()
#5. select first two
# for i in range(len(checkbox)):
#     if i < 2:
#         checkbox[i].click()

time.sleep(5)
#6. clear all checkbox
for i in checkbox:
    if i.is_selected():
        i.click()

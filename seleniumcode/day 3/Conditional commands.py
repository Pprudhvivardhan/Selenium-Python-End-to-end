from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service_object = Service('C:\\Users\\user\\PycharmProjects\\ selenium\\day 1 selenium\\chromedriver.exe')

driver =webdriver.Chrome(service=service_object)
driver.get('https://demo.nopcommerce.com/register?returnUrl=%2F')
#IS_DISPLAY & IS_ENABLED
search=driver.find_element(By.XPATH,"//input[@placeholder='Search store']")
print('dispaly status :',search.is_displayed()) #True
print('enabled status :',search.is_enabled()) #True
#IS_SELECTED
male_radio=driver.find_element(By.XPATH,"//input[@value='M']")
female_radio=driver.find_element(By.XPATH,"//input[@value='F']")
print('default setting')
print('male radio:',male_radio.is_selected())
print('female radio:',female_radio.is_selected())

male_radio.click()
print('after clicking the male ')
print('male radio:',male_radio.is_selected())
print('female radio:',female_radio.is_selected())

female_radio.click()
print('after clicking the female ')
print('female radio:',male_radio.is_selected())
print('female radio:',female_radio.is_selected())

driver.close()

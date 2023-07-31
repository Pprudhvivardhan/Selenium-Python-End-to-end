from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service_object = Service('C:\\Users\\user\\PycharmProjects\\ selenium\\day 1 selenium\\chromedriver.exe')

driver =webdriver.Chrome(service=service_object)

driver.get('https://demo.nopcommerce.com/')

#ABSOLUTE XPATH
#driver.find_element(By.XPATH,'/html[1]/body[1]/div[6]/div[1]/div[2]/div[2]/form[1]/input[1]').send_keys('T-shirt')
#driver.find_element(By.XPATH,'/html[1]/body[1]/div[6]/div[1]/div[2]/div[2]/form[1]/button[1]').click()

#RELATIVE XPATH
#driver.find_element(By.XPATH,'//input[@id="small-searchterms"]').send_keys('T-shirt')
#driver.find_element(By.XPATH,'//button[@type="submit"]').click()

# OR & AND
#driver.find_element(By.XPATH,'//input[@ id="small-searchterms" or @ type="text" ]').send_keys('T-shirt')
#driver.find_element(By.XPATH,'//button[@ type="submit" and @ class="button-1 search-box-button" ]').click()
# CONTAINS & STARTS-WITH
#driver.find_element(By.XPATH,'//input[contains(@class,ui-autocomplete)]').send_keys('T-shirt')
#driver.find_element(By.XPATH,'//button[starts-with(type,sub)]').click()

driver.find_element(By.XPATH,'//div[text()="Categories"]').click()

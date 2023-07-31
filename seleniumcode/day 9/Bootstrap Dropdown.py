from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

service_obj= Service("C:\\Users\\user\\Drivers\\chromedriver.exe")

driver= webdriver.Chrome(service =service_obj)
driver.get(" https://www.dummyticket.com/")
driver.implicitly_wait(10)
driver.maximize_window()



selectticket=driver.find_element(By.XPATH," (//a[contains(@class,'btn-w-full fg-text-dark ffb-button1-4-1')])[2]")

driver.execute_script("arguments[0].scrollIntoView();",selectticket)
selectticket.click()


driver.find_element(By.XPATH,"//span[@id='select2-billing_country-container']").click()


countrieslist=driver.find_elements(By.XPATH," //ul[@id='select2-billing_country-results']/li")
print(len(countrieslist))

for i in countrieslist:
    if i.text=="India":
        i.click()
        break

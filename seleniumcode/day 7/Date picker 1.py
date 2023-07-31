import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
service_obj= Service("C:\\Users\\user\\Drivers\\chromedriver.exe")

driver= webdriver.Chrome(service =service_obj)
driver.get("https://jqueryui.com/datepicker/")

driver.switch_to.frame(0) # switch to the frame
# driver.find_element(By.XPATH,"//input[@id='datepicker']").send_keys("07/03/1997") #mm/dd/yy
# time.sleep(3)

year="2022"
date="23"
month="March"


driver.find_element(By.XPATH, "//input[@id='datepicker']").click()

while True:
    mn=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text
    yr=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-year']").text

    if mn==month and yr==year:
        break;
    else:
        driver.find_element(By.XPATH,"//span[@class='ui-icon ui-icon-circle-triangle-w']").click()

time.sleep(3)

dates=driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")

for i in dates:
    if i.text==date:
        i.click()
        break
time.sleep(3)
driver.close()
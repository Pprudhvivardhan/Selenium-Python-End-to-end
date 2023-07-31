import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

service_obj= Service("C:\\Users\\user\\Drivers\\chromedriver.exe")


driver = webdriver.Chrome(service =service_obj)
driver.implicitly_wait(20)
driver.get(" https://www.dummyticket.com/")
driver.maximize_window()

# open buy ticket
driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/section[3]/div[1]/div[1]/div[3]/div[1]/div[2]/section[1]/div[2]/span[1]/a[1]").click()

#select date of birth
driver.find_element(By.XPATH,"//input[@id='dob']").click()

month=Select(driver.find_element(By.XPATH,"//select[@aria-label='Select month']"))
month.select_by_visible_text('Jan') # selects the month

year=Select(driver.find_element(By.XPATH," //select[@aria-label='Select year']"))
year.select_by_visible_text("2021")

dates =driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")

for i in dates:
    if i.text=="20":
        i.click()
        break
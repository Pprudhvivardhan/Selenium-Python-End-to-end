from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
service_obj= Service("C:\\Users\\user\\Drivers\\chromedriver.exe")

driver= webdriver.Chrome(service =service_obj)
driver.get("https://jqueryui.com/datepicker/")

demo=driver.find_element(By.XPATH," //a[normalize-space()='Demos']")
lopala=driver.find_elements(By.XPATH," //div[@id='content']//a[normalize-space()='Draggable']")

act=ActionChains(driver)
act.move_to_element(demo).click().perform()

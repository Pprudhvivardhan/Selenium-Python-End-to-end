from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
service_obj= Service("C:\\Users\\user\\Drivers\\chromedriver.exe")

driver= webdriver.Chrome(service =service_obj)
driver.get(" https://swisnl.github.io/jQuery-contextMenu/demo.html")

button=driver.find_element(By.XPATH," //span[@class='context-menu-one btn btn-neutral']")

act = ActionChains(driver)
act.context_click(button).perform() #Performs right click
driver.find_element(By.XPATH,"//span[normalize-space()='Copy']").click()

driver.switch_to.alert.accept()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service_object = Service('C:\\Users\\user\\PycharmProjects\\ selenium\\day 1 selenium\\chromedriver.exe')

ops=webdriver.ChromeOptions()
ops.add_argument("--disable-notifications")
driver =webdriver.Chrome(service=service_object,options=ops)
driver.maximize_window()
driver.get("https://www.where-am-i.co/")

driver.find_element(By.XPATH,"//a[@class='cc_btn cc_btn_accept_all']").click()
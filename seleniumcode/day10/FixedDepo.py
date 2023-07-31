import time

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
import openpyxl
from day10 import excelulity

# service_object=Service("C:\\Users\\user\\PycharmProjects\\selenium\\day 1 selenium\\chromedriver.exe")
service_object = Service('C:\\Users\\user\\PycharmProjects\\ selenium\\day 1 selenium\\chromedriver.exe')
driver= webdriver.Chrome(service=service_object)
driver.implicitly_wait(10)
driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html?classic=true")
driver.maximize_window()

file="C:\\Users\\user\\Downloads\\selen.example.xlsx"
rows=excelulity.getRowCount(file,"Sheet1")

for r in range(2,rows+1):
    pric=excelulity.readData(file, "Sheet1",r,1)
    rateofinterest=excelulity.readData(file, "Sheet1",r,2)
    per1 = excelulity.readData(file, "Sheet1", r, 3)
    per2 = excelulity.readData(file, "Sheet1", r, 4)
    fre = excelulity.readData(file, "Sheet1", r, 5)
    exp_value = excelulity.readData(file, "Sheet1", r, 6)
     #passing data to the application
    driver.find_element(By.XPATH,"//input[@id='principal']").send_keys(pric)
    driver.find_element(By.XPATH, "//input[@id='interest']").send_keys(rateofinterest)
    driver.find_element(By.XPATH,"//input[@id='tenure']").send_keys(per1)

    periodorp = Select(driver.find_element(By.XPATH, "//select[@id='tenurePeriod']"))
    periodorp.select_by_visible_text(per2)

    frequencydro = Select(driver.find_element(By.XPATH, "//select[@id='frequency']"))
    frequencydro.select_by_visible_text(fre)
    #Button
    driver.find_element(By.XPATH,"//*[@id='fdMatVal']/div[2]/a[1]/img").click()
    #result
    result=driver.find_element(By.XPATH,"\\span[id='resp_matval']\ strong").text()
    #Validation
    if float(exp_value)==float(result):
        print("Test Passed")
        excelulity.writeData(file,"Sheet1",r,8,"Passed")
        excelulity.fillGreenColor(file, "Sheet1", r, 8)
    else:
        print("Test Failed")
        excelulity.writeData(file, "Sheet1", r, 8, "Failed")
        excelulity.fillRedColor(file, "Sheet1", r, 8)

    driver.find_element(By.XPATH,"(//img[@class='PL5'])[1]").click()
    time.sleep(2)
driver.close()



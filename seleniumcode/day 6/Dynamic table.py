from Tools.scripts.serve import app
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service_object = Service('C:\\Users\\user\\PycharmProjects\\ selenium\\day 1 selenium\\chromedriver.exe')

driver =webdriver.Chrome(service=service_object)
driver.maximize_window()
driver.get(" https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

#Admin->user management-->users

driver.find_element(By.XPATH, "//*[@id='senu_adein_viewAdminModule 1/b").click()
driver.find_element(By.XPATH, "//[@id='menu_admin_UserManagement 1").click()
driver.find_element(By.XPATH,"//[@id='menu_admin_viewSystemUsers").click()

#total rows n a table

rows =len(driver.find_elements(By.XPATH, "//table[@id='resultTable']//tbody/tr"))
print("total number of rows in a table:", rows)
count=0
for row in range(1, rows+1):
    status=driver.find_element(By.XPATH, "//table[@ids 'resultTable']/tbody/tr["+str(row)+"]/td[5]").text
if status=="Enabled":
    count=count+1

print("Total Number of users: ", rows)
print("Number of enabled users: ", count)
print("Number of disabled users: ", (rows-count))
driver.close()



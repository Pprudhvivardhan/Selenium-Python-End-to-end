from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service_object = Service('C:\\Users\\user\\PycharmProjects\\ selenium\\day 1 selenium\\chromedriver.exe')

driver =webdriver.Chrome(service=service_object)
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")

#1. count no.of rows in the table
rows=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr"))
columns=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr[1]/th"))
print(rows,columns) #7 #4
# driver.close()

#2.Read specific row and column data
data=driver.find_element(By.XPATH,"//table[@name='BookTable']//tr[5]/td[1]").text
#print(data) #Master In Selenium

# #3.read all the data from table
# for row in range(2,rows+1):
#     for col in range(1,columns+1):
#         data = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr["+str(row)+"]/td["+str(col)+"]").text
#         print(data,end="    ")
#     print()

#4.read the data according to condition (list books who's name s mukesh)
for row in range(2,rows+1):
    authorname=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(row)+"]/td[2]").text
    if authorname=="Mukesh":
        bookname = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(row)+"]/td[1]").text
        price = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(row)+"]/td[4]").text

        print(bookname,"    "  ,authorname,"    " , price)





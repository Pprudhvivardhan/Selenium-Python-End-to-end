from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service_object = Service('C:\\Users\\user\\PycharmProjects\\ selenium\\day 1 selenium\\chromedriver.exe')

driver =webdriver.Chrome(service=service_object)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

#Single window

# windowid =driver.current_window_handle
# print(windowid)#CDwindow-81ECCBB02E9BB54F88B4D520C7CACEA2 .....CDwindow-DA094D65FF7B7A40412C05AD8ACEAD9B

#Multiple windows
#Approcah 1
driver.find_element(By.XPATH,"//button[@id='openwindow']").click()
windowIDs=driver.window_handles
# parentwindow=windowIDs[0]   #CDwindow-7C4C493AB6B35E1FA62DB89EF000ECE6
# childwindow=windowIDs[1]    #CDwindow-E16324CD7046CBB784CAFCA91C60DA3A
# #print(parentwindow,childwindow)
# driver.switch_to.window(childwindow)
# print('childwindows title;',driver.title)
#
# driver.switch_to.window(parentwindow)
# print('parentwindows title;',driver.title) #'Practice Page'

#Approcah 2
# for i in windowIDs:
#     driver.switch_to.window(i)
#     print(driver.title)

#Approcah 3
for i in windowIDs:
    driver.switch_to.window(i)
    if driver.title=='Practice Page': # close particular windows
        driver.close()




driver.quit()

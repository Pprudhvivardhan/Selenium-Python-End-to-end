
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os
location=os.getcwd()

def chrome_setup():
    from selenium.webdriver.chrome.service import Service
    service_obj= Service("C:\\Users\\user\\Drivers\\chromedriver.exe")
    #download in desired location
    prefrences={'download.default_directory':location,"plugins.always_open_pdf_externally":True}
    ops=webdriver.ChromeOptions()
    ops.add_experimental_option('prefs',prefrences)
    driver= webdriver.Chrome(service =service_obj,options=ops)
    return driver

def Edge_setup():
    from selenium.webdriver.edge.service import Service
    service_obj: Service= Service("C:\\Users\\user\\Drivers\\msedgedriver.exe")
    #download in desired location
    prefrences={'download.default_directory':location}
    ops=webdriver.EdgeOptions()
    ops.add_experimental_option('prefs',prefrences)
    driver= webdriver.Edge(service =service_obj,options=ops)
    return driver

def firefox_setup():
    from selenium.webdriver.firefox.service import Service
    serv_obj = Service ("C:\Drivers\geckodriver-v0.29.1-win64\geckodriver.exe")
    # settings
    ops = webdriver.FirefoxOptions()
    ops.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf") #Mime tag
    ops.set_preference("pdfjs.disabled",True)# For pdf
    ops.set_preference("browser.download.manager.showWhenStarting", False)
    ops.set_preference("browser.download.folderList", 2)  # 0-desktop 1-downloads folder 2- Desired loc
    ops.set_preference("browser.download.dir", location)
    driver = webdriver.Firefox(service=serv_obj,options = ops)
    return driver


#Automation Code:
#driver=chrome_setup()
driver=Edge_setup()
driver.get(" https://filesamples.com/formats/docx")
driver.maximize_window()
driver.find_element(By.XPATH,"//div[@id='output']//div[2]//a[1]").click()
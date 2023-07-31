from selenium import webdriver

def headless_chrome():
    from selenium.webdriver.chrome.service import Service
    service_object=Service("C:\\Users\\user\\Drivers\\chromedriver.exe")
    ops=webdriver.ChromeOptions()
    ops.headless=True
    driver=webdriver.Chrome(service=service_object,options=ops)
    return driver
def headless_edge():
    from selenium.webdriver.edge.service import Service
    service_object=Service("C:\\Users\\user\\Drivers\\msedgedriver.exe")
    ops=webdriver.EdgeOptions()
    ops.headless=True
    driver=webdriver.Edge(service=service_object,options=ops)
    return driver
def headless_firefox():
    from selenium.webdriver.firefox.service import Service
    service_object=Service("C:\\Users\\user\\Drivers\\geckodriver.exe")
    ops=webdriver.FirefoxOptions()
    ops.headless=True
    driver=webdriver.Firefox(service=service_object,options=ops)
    return driver

# driver=headless_chrome()
# driver=headless_edge()
driver=headless_firefox()
driver.get(" https://demo.nopcommerce.com/")
print(driver.title)
print(driver.current_url)
driver.close()
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
#chrome_option.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-error")
chrome_options.add_argument("--start-maximized")
service_object = Service("C:\\Users\\jguala\\Downloads\\chromedriver.exe")
driver = webdriver.Chrome(service=service_object, options=chrome_options)

driver.get("https:google.com")

time.sleep(2)

driver.close()

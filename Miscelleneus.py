import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_object = Service("C:/Users/jguala/Downloads/chromedriver.exe")
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificates-errors")

driver = webdriver.Chrome(service=service_object,options=chrome_options)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.implicitly_wait(4)
#scroll to the bottom
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)") #or driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
time.sleep(2)
driver.get_screenshot_as_file("ashok.png")
driver.close()

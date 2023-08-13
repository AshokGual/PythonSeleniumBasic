from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_object = Service("C:/Users/jguala/Downloads/chromedriver.exe")
driver = webdriver.Chrome(service=service_object)
driver.implicitly_wait(5)
driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT,"Click Here").click()
windowsOpened = driver.window_handles
print(windowsOpened)
driver.switch_to.window(windowsOpened[1])
print(driver.find_element(By.TAG_NAME,"h3").text)
driver.switch_to.window(windowsOpened[0])

assert "Opening a new window" == driver.find_element(By.TAG_NAME,"h3").text
driver.quit()
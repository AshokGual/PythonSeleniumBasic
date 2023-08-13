from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_object = Service("C:/Users/jguala/Downloads/chromedriver.exe")
driver = webdriver.Chrome(service=service_object)
driver.get("https://the-internet.herokuapp.com/iframe")
driver.switch_to.frame("mce_0_ifr")
driver.find_element(By.CSS_SELECTOR,"#tinymce").clear()
driver.find_element(By.CSS_SELECTOR,"#tinymce").send_keys("I am able to automate iframe")
driver.switch_to.default_content()
print(driver.find_element(By.CSS_SELECTOR,"h3").text)
driver.close()


import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_object = Service("C:\\Users\\jguala\\Downloads\\chromedriver.exe")
driver = webdriver.Chrome(service=service_object)
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
action = ActionChains(driver)
#action.context_click(driver.find_element(By.CSS_SELECTOR,"#mousehover")).perform()

#action.move_to_element(driver.find_element(By.CSS_SELECTOR,"#mousehover")).perform()
#action.context_click(driver.find_element(By.LINK_TEXT,"Top")).perform()
#driver.find_element(By.LINK_TEXT,"Top").click()
action.scroll_to_element(driver.find_element(By.CSS_SELECTOR,"#mousehover")).perform()
time.sleep(3)
driver.quit()
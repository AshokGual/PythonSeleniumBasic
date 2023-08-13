import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_object = Service("C:/Users/jguala/Downloads/chromedriver.exe")
driver = webdriver.Chrome(service=service_object)
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.maximize_window()
driver.implicitly_wait(5)
driver.find_element(By.CSS_SELECTOR,"#autosuggest").send_keys("ind")
time.sleep(2)
countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")
print(len(countries))
for country in countries:
    if country.text == "India":
        country.click()
        break
print(driver.find_element(By.CSS_SELECTOR,"#autosuggest").get_attribute("value"))
assert driver.find_element(By.CSS_SELECTOR,"#autosuggest").get_attribute("value") == "India"
driver.quit()

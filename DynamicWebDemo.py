import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_object = Service("C:\\Users\\jguala\\Downloads\\chromedriver.exe")
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=service_object, options=chrome_options)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.implicitly_wait(4)
#a[href*='shop']    , //a[contains(@href, 'shop')]
driver.find_element(By.CSS_SELECTOR, "a[href*='shop'] ").click()
productsList = driver.find_elements(By.CSS_SELECTOR,".card.h-100")
print(len(productsList))

for item in productsList:
    if item.find_element(By.XPATH,"div/h4/a").text == "Nokia Edge":
        item.find_element(By.XPATH,"div/button").click()
        break

driver.find_element(By.CSS_SELECTOR,".nav-link.btn.btn-primary").click()
driver.find_element(By.CSS_SELECTOR,".btn.btn-success").click()
wait = WebDriverWait(driver,10)

driver.find_element(By.CSS_SELECTOR,"#country").send_keys("ind")
wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//a[text()='India']")))
driver.find_element(By.XPATH,"//a[text()='India']").click()
driver.find_element(By.CSS_SELECTOR,"label[for='checkbox2']").click()
driver.find_element(By.CSS_SELECTOR,"input[value='Purchase']").click()
print(driver.find_element(By.XPATH,"//div[@class='alert alert-success alert-dismissible']").text)
time.sleep(5)
assert "Success! Thank you!" in driver.find_element(By.XPATH,"//div[@class='alert alert-success alert-dismissible']").text
driver.close()

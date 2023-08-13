import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

"""
implicit wait globally applied in a session.
Implicit wait waits for element is available to perform any action till the given time.
implicit wait apply to all the code in a session, for findelements implicit wait doesnot work 
because it checks for only return type and here return type is list(empty list) so it will proceed ahead
if we wait for 2sec then the actual list value is returning. This is the only exceptional case 
"""
service_object = Service("C:/Users/jguala/Downloads/chromedriver.exe")
driver = webdriver.Chrome(service=service_object)
driver.implicitly_wait(2)
# record start time
start = time.time()

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR, "input[type='search']").send_keys("ber")
time.sleep(2)
products_list = []
products = driver.find_elements(By.XPATH,"//div[@class='products']/div[@class='product']")
#carts = driver.find_elements(By.XPATH, "//button[text()='ADD TO CART']")
print(len(products))
assert products != 0
for cart in products:
    products_list.append(cart.find_element(By.XPATH, "h4").text)  #xpath extension
    cart.find_element(By.XPATH, "div/button").click()
print("product lists are", products_list)

driver.find_element(By.XPATH, "//img[@alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")

driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
# explicit wait
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))

promotext = driver.find_element(By.CSS_SELECTOR,".promoInfo").text
print(promotext)


# //tbody/tr[3]/td[5]
row = len(products)
total_price = 0
for r in range(1, row + 1):
    price = driver.find_element(By.XPATH, f"//tbody/tr[{r}]/td[5]").text
    total_price = total_price + int(price)

print("total price is :", total_price)
actual_totalPrice = driver.find_element(By.CSS_SELECTOR, ".totAmt").text
assert int(actual_totalPrice) == total_price
actual_dicount_price = driver.find_element(By.CSS_SELECTOR, ".discountAmt").text
discount_price = (total_price * 10) / 100

totalpriceDiscount = total_price - discount_price

print(totalpriceDiscount)
assert float(actual_dicount_price) == totalpriceDiscount

driver.find_element(By.XPATH, "//button[text()='Place Order']").click()
print("all the code executed successfully")
# record end time
end = time.time()
print("The time of execution of above program is :",
      (end - start), "s")

driver.quit()





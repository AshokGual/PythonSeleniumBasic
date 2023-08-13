from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_object = Service("C:/Users/jguala/Downloads/chromedriver.exe")
chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")

driver = webdriver.Chrome(service=service_object, options=chrome_options)
driver.implicitly_wait(5)
BrowserSortedVaggieList = []
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.XPATH,"//a[text()='Top Deals']").click()
windows = driver.window_handles
driver.switch_to.window(windows[-1])
#verify vaggie list is in ascending order
#Steps: click on column header
#collect vaggie list
#sort vaggie list in ascending order
# compare sorted vaggie list with vaggie list
driver.find_element(By.XPATH,"//span[text()='Veg/fruit name']").click()
# tableLength = driver.find_elements(By.XPATH,"//tbody/tr")
# print(len(tableLength))
# BrowserSortedVaggieList = []
# for vaggie in range(1, len(tableLength)+1):
#     VaggieList.append(driver.find_element(By.XPATH, f"//tbody/tr[{vaggie}]/td[1]").text)  or

vaggieWebelements = driver.find_elements(By.XPATH,"//tr/td[1]")
for ele in vaggieWebelements:
    BrowserSortedVaggieList.append(ele.text)

print(BrowserSortedVaggieList)

SortVaggieList = sorted(BrowserSortedVaggieList)
print(SortVaggieList)
assert BrowserSortedVaggieList == SortVaggieList , "Vaggielist are not sorted in table"
print("Vaggielist are sorted in table")

driver.quit()

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("/Users/Akash.Dasgupta/Documents/chromedriver")

driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.get('https://rahulshettyacademy.com/seleniumPractise/#/offers')

# Sort the tables - Sort the products


# Algorithm
# Click on column header
# Collect all vegetable names to veggie list -> Browser Sorted List
# Apply sort to veggie list by python methods and  store to -> New Veggie List
# Check Browser List is equal to New list or not

driver.find_element(By.CSS_SELECTOR, "th:nth-child(1)").click() # Click to sort

veg_list = []
veggies = driver.find_elements(By.XPATH, "//tr/td[1]")
for veg in veggies:
    veg_list.append(veg.text)

check_list = veg_list.copy() # Copy of list so that we can check it later / We can also use slice
# -> but copy is faster than slice
print(check_list)
print(veg_list)

veg_list.sort()
assert veg_list == check_list

time.sleep(5)
driver.close()
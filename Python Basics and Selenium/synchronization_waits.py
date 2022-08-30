import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service('/Users/Akash.Dasgupta/Documents/chromedriver')
driver = webdriver.Chrome(service=service_obj)

driver.get('https://rahulshettyacademy.com/seleniumPractise/#/')
driver.implicitly_wait(5)
#Entering to search box
driver.find_element(By.CSS_SELECTOR, '.search-keyword').send_keys('ber')
time.sleep(2) # -> Wait to load server - Implicit wait will not work here as if loading of server fail, empty list is generated
# which is also valid
# On passing ber add all the veggies displayed, count and iterate



#----------------------------------Assignment 2------------------------------
expected = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
actual = []
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")

print(len(results))
# To put assertion on lengths
assert len(results) > 0

#--------------------Chaining-----------------------
# We already had pre written xpath in out veggies, just we have to click the button
# Write the remaining piece with parent web element
for result in results:
    actual.append(result.find_element(By.XPATH, 'h4').text) #Assignment 2 Grabbing the name of veggies
    result.find_element(By.XPATH, "div/button").click() # Do not add a / while chaining

assert expected == actual # Checking

driver.find_element(By.XPATH, '//img[@class=" "]').click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

# Send 'rahulshettyacademy' as a promocode and apply
driver.find_element(By.CSS_SELECTOR, '.promoCode').send_keys('rahulshettyacademy')
driver.find_element(By.CSS_SELECTOR, '.promoBtn').click()


# Explicit wait ------------> Applied wait to only a particular web element
# Applying a long time wait by implicit will apply to whole script, which is a bad practice knowingly about that appln has bug
# Explicit wait overrides the implicit wait

wait = WebDriverWait(driver, 10) # Invoking WebDriverWait class
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, '.promoInfo'))) # waiting until
#Below code is failing as it takes some time to load its not instant, also tim.sleep is a bad practice
# So we use implicit wait mechansim
print(driver.find_element(By.CSS_SELECTOR, '.promoInfo').text)



# --------------------------Validating all the items added to cart is the proper total
prices = driver.find_elements(By.CSS_SELECTOR, 'td:nth-child(5) .amount ')
total = 0
for price in prices:
    total = total + int(price.text)

print(total)
tot = int(driver.find_element(By.CSS_SELECTOR, '.totAmt').text)
assert tot == total

discounted_amount = float(driver.find_element(By.CSS_SELECTOR, '.discountAmt').text)

assert discounted_amount < total




time.sleep(5)
driver.close()

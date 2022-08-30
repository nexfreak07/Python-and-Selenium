from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service('/Users/Akash.Dasgupta/Documents/chromedriver')
driver = webdriver.Chrome(service=service_obj)
driver.get('https://rahulshettyacademy.com/angularpractice/')


driver.find_element(By.NAME, "name").send_keys('Akash Dasgupta')
driver.find_element(By.NAME, "email").send_keys('akashakxy@gmail.com')
driver.find_element(By.ID, "exampleInputPassword1").send_keys('AEZAKMI')
driver.find_element(By.ID, "exampleCheck1").click()


# Static Dropdown
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_visible_text('Female') # Select by Text
dropdown.select_by_index(0) # Select by Index



# Syntax for Xpath
# //tagname[@attribute='value'] - > //input[@type='submit']
# CSS Selector Syntax - input[type='submit'] -> No // and @
driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click() # CSS Selector by ID
driver.find_element(By.XPATH, "//input[@type='text']").send_keys("Akash Dasgupta")
driver.find_element(By.XPATH, "//input[@type='submit']").click()


# spaces between classes denotes different class names
# text is an attribute to grab the message at that class name
message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)

assert "Success" in message
driver.close()
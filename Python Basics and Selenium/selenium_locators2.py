from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("/Users/Akash.Dasgupta/Documents/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.get('https://rahulshettyacademy.com/client')

# Link Text - if it has <a> tag it means it has a link, an element in webpage linked to another element
# eg - Forgot password
driver.find_element(By.LINK_TEXT, "Forgot password?").click()
driver.find_element(By.XPATH, "//input[@type='email']").send_keys('demo@gmail.com')
# find element by CSS Prent to child traversal parent child1:nth-child1(block no) child2
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(2) input").send_keys("Hello@1234")

# find element by parent to child traversal - Syntax - //parent/child1[block no]/child2.....
driver.find_element(By.XPATH, "//form/div[3]/input").send_keys("Hello@1234")
# Click the submit button
driver.find_element(By.XPATH, "//button[text()='Save New Password']").click()
# Parent to child traverse in the HTML File
# //form/div[3]/input -> form is parent, div is child, so many divs so 3rd div to be selected, then select input
driver.close()
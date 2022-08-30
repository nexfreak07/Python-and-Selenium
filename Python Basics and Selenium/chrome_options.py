from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service('/Users/Akash.Dasgupta/Documents/chromedriver')
# Invoking Chrome Options class
chrome_options = webdriver.ChromeOptions()

# Setting Chrome Options as to start in maximize mode by default
chrome_options.add_argument('--start-maximized')
chrome_options.add_argument('headless') # To start in headless manner
chrome_options.add_argument('--ignore-certificate-error') # Ignore the error and press and advance and proceed

driver = webdriver.Chrome(service=service_obj, options=chrome_options)
driver.get('https://rahulshettyacademy.com/angularpractice/')
print(driver.title)
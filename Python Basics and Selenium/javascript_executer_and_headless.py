# Selenium does not provide anything to scroll down, but using java script we can scroll down
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("/Users/Akash.Dasgupta/Documents/chromedriver")
# Creating Chrome Options for Headless Mode - Faster and Browser will bot open

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('headless') # Setting options so that browser does not opens up
# Press Advance and lands to the webpage automatically
chrome_options.add_argument('--ignore-certificate-errors') # Setting ignore so that it ignores certificates


# Adding chrome options to the driver so No browser Opens up
driver = webdriver.Chrome(service=service_obj, options=chrome_options)
driver.implicitly_wait(5)
driver.get('https://rahulshettyacademy.com/AutomationPractice/')
driver.execute_script("window.scrollBy(0, document.body.scrollHeight);") # Executing Js Code from Console
driver.get_screenshot_as_file("screen.png") # Taking screenshot - Usually used when test fails



time.sleep(2)
driver.close()
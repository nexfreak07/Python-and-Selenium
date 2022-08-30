# Frames are basically another page which is embedded into thre parent html page
# How to know about Frame is present or not
# 1. Ask Developer 2. Automation Fails, cannot find element --------- check for <iframe> tag in html

# As there is a frame over here so we are unable to access the Frame, hence a error is thrown (No such element error)

import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service_obj = Service("/Users/Akash.Dasgupta/Documents/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(3)
driver.get('https://the-internet.herokuapp.com/iframe')

# As there is a frame over here so we are unable to access the Frame, hence a error is thrown (No such element error)
# Hence we need to switch to Frame and then handle everything --------driver.switch_to.frame(Frame ID)

frame = driver.switch_to.frame("mce_0_ifr")
driver.find_element(By.ID, "tinymce").clear() # Clearing the existing text
driver.find_element(By.ID, "tinymce").send_keys("Akash here, Good Automation Tester")

driver.switch_to.default_content() # Switching back to driver when it was created

print(driver.find_element(By.TAG_NAME, 'h3').text)


time.sleep(2)
driver.close()
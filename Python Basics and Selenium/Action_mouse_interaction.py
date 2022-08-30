import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("/Users/Akash.Dasgupta/Documents/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.get('https://rahulshettyacademy.com/AutomationPractice/')

# Hovering of Mouse and Mouse actions are performed by Action class
# Invoke the action object
actions = ActionChains(driver)

# actions.click_and_hold() - long press
# actions.context_click() - Right click
# actions.double_click() - Double click
# actions.drag_and_drop(source, target) - DND

actions.move_to_element(driver.find_element(By.ID, "mousehover")).perform()
actions.context_click(driver.find_element(By.LINK_TEXT, "Top")).perform()
actions.context_click(driver.find_element(By.LINK_TEXT, "Reload")).click().perform()


time.sleep(2)
driver.close()
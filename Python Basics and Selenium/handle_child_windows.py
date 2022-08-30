import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service_obj = Service("/Users/Akash.Dasgupta/Documents/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(2)
driver.get('https://the-internet.herokuapp.com/windows')

action = ActionChains(driver)
action.move_to_element(driver.find_element(By.LINK_TEXT, "Click Here")).click().perform()
# Switched to New Window - The scope is still under parent window

windowOpened = driver.window_handles # Grabs all windows opened and stores in a list format

# Indexing of windows will be from 0 as parent and follows to nth child
driver.switch_to.window(windowOpened[1]) # Switching to the desired window
print(driver.find_element(By.TAG_NAME, 'h3').text)
driver.close() # Closing child window
driver.switch_to.window(windowOpened[0]) # Switching to the parent window
assert  'Opening a new window' == (driver.find_element(By.TAG_NAME, 'h3').text)


time.sleep(2)
driver.close()
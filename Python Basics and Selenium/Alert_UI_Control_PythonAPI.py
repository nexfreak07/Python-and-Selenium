import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service('/Users/Akash.Dasgupta/Documents/chromedriver')
driver = webdriver.Chrome(service=service_obj)

driver.get('https://www.rahulshettyacademy.com/AutomationPractice/')
# Iteration over checkboxes to click by iteration

# Handling Checkbox

checkboxes = driver.find_elements(By.XPATH, '//input[@type="checkbox"]')
print(len(checkboxes))

for checkbox in checkboxes:
    if checkbox.get_attribute('value') == 'option2':
        checkbox.click()
        assert checkbox.is_selected() # check if proper checkbox is selected or not
        break

print(driver.find_element(By.XPATH, '//input[@type="checkbox"]').get_attribute('value'))
# Handling Radiobutton

radio_button = driver.find_elements(By.XPATH, '//input[@type="radio"]')
print(len(radio_button))

for button in radio_button:
    if button.get_attribute('value') == 'radio3':
        button.click()
        assert button.is_enabled()
        break

# is_displayed() - The input box is displayed or not

# the box is now displaye and we are checking
assert driver.find_element(By.ID, 'displayed-text').is_displayed()
# clicking to hide
driver.find_element(By.CSS_SELECTOR, '#hide-textbox').click()
# Now the assert will throw error, so assert not means - not displayed
assert not driver.find_element(By.ID, 'displayed-text').is_displayed()

# -----------------------------------------------ALERTS------------------------------------------------------------

# Java-Script Executor - Handling Alert pop-ups
driver.find_element(By.XPATH, "//fieldset/input[@id='name']").send_keys('Akash')
driver.find_element(By.CSS_SELECTOR, '#alertbtn').click()
# Switching to alert mode, it will have knowledge of alert, no browser leve knowledge
alert = driver.switch_to.alert
# Now we will check about our name is in the alert or not, so will grab the text
alert_text = alert.text
print(f'Alert is {alert_text}')
assert 'Akash' in alert_text
# Now we have to accept or click ok to alert.
alert.accept()

#alert dismiss
driver.find_element(By.XPATH, "//fieldset/input[@id='name']").send_keys('Akash')
driver.find_element(By.CSS_SELECTOR, '#confirmbtn').click()
alert = driver.switch_to.alert
alert.dismiss()


time.sleep(5)
driver.close()
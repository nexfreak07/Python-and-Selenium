import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("/Users/Akash.Dasgupta/Documents/chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

driver.find_element(By.ID, 'autosuggest').send_keys('ind')
# by doing above the popup dropdown appears, and it takes atleast 2 sec to display so we put sleep
time.sleep(2)

# Now in pop up we have multiple elements so we have to iterate it.
# we used parent to children CSS selector parent[child1='value'] child2
countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")
print(len(countries))
# Iterating in countries

for country in countries:
    if country.text == 'India':
        country.click()
        break # Once Clicked so we skip remaining the rest by break

# This will not give you any o/p, because it got dynamically updated
# To get by .text the page should already present when it is loaded for the 1st time
print(driver.find_element(By.ID, 'autosuggest').text)

# so to get the text which is dynamically we dont do .text instead we do .get_attribute()

print(driver.find_element(By.ID, 'autosuggest').get_attribute('value')) #get_attribute('value') - is a javascript, a attribute value is present in the backend

# Assertion to check the attribute is correct or not
assert (driver.find_element(By.ID, 'autosuggest').get_attribute('value')) == 'India'


driver.close()
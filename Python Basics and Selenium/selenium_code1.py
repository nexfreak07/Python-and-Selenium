from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#The Service() class knows about the chrome driver, we give the path, then that invokes the Chrome browser
service_obj = Service("/Users/Akash.Dasgupta/Documents/chromedriver.exe")

#invoking chrome browser
#chrome cannot be invoked directly we need chrome driver for that
driver = webdriver.Chrome(service=service_obj)
# How to maximize the window - Maximizing is always done before hitting the URL
driver.maximize_window()

driver.get('https://rahulshettyacademy.com') # get to the url

print(driver.title) # title is the property, and it does not requre () - It helps to get the title of webpage
# to make sure that you are in the correct url
print(driver.current_url)

driver.get('https://rahulshettyacademy.com/seleniumPractise/#/')
driver.minimize_window() # Minimize the window

driver.back() # Go to the previous page (Rahul Shetty URL)
print('After back URL'+driver.current_url)

driver.refresh() # Refresh the current page

driver.forward() # go to forward (Green Kart) URL
print('After forward url'+driver.current_url)
# driver.close() # close the webdriver

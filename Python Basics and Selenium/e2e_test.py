import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service('/Users/Akash.Dasgupta/Documents/chromedriver')

driver = webdriver.Chrome(service=service_obj)
driver.get('https://rahulshettyacademy.com/angularpractice')
driver.implicitly_wait(4)
# customized css from Regular expression -> a[href*='Shop'] and Xpath -> //a[contains(href,'Shop')]
driver.find_element(By.LINK_TEXT, 'Shop').click()
phones = driver.find_elements(By.XPATH, "//div[@class='card h-100']")

for phone in phones:
    phone_name = phone.find_element(By.XPATH, 'div/h4/a').text
    if phone_name == 'Blackberry':
        phone.find_element(By.XPATH, 'div/button').click()


driver.find_element(By.CSS_SELECTOR, "a[class*='nav-link btn btn-primary']").click()
driver.find_element(By.CSS_SELECTOR, "td button.btn.btn-success").click()

driver.find_element(By.CSS_SELECTOR,"#country").send_keys("Ind")
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element(By.LINK_TEXT, "India").click()

driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()  # Question????????????

# <div class="alert alert-success alert-dismissible" xpath="1">
#         The Above Element has three class name ---> alert, alert-success and alert-dismissible
# Among those any one can be used

driver.find_element(By.XPATH, "//input[@type='submit']").click()

success_text = driver.find_element(By.CLASS_NAME, 'alert-success').text
print(success_text)
assert 'Success! Thank you! Your order will be delivered in next few weeks :-).' in success_text  # Question?????????????????


time.sleep(3)
driver.close()

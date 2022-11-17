url = "https://www.makemytrip.com/"
radio_button = "li[data-cy='roundTrip']"
from_city_button = "//div/div/label[@for='fromCity']"
from_city = "//input[@placeholder='From']"

wait_src = "//div/ul/li[@role='option']"
pune_airport = "//div[@class='calc60']/child::p[text()='Pune Airport']"
to_city_button = "//div/label[@for='toCity']"
to_city = "//div/div[@role='combobox']/input[@type='text']"
wait_dept = "//div[text()='CCU']/ancestor::li[@role='option']"
kolkata_airport = "//div[text()='CCU']/ancestor::li[@role='option']"
dept_button = "//div[@role='heading']"
dept_date = '//p[text()="23"]/ancestor::div[@aria-label="Sun Oct 23 2022"]'
arr_date = "//p[text()='31']/ancestor::div[@aria-label='Mon Oct 31 2022']"
travel_button = "div[data-cy='flightTraveller']"
adults = 'li[data-cy="adults-1"]'
apply = ".btnApply"
search = ".widgetSearchBtn"
wait_airlines = "//p[text()='Airlines']"

gofirst_carrier = "//span[@title='Go First']/preceding-sibling::span[@class='customCheckbox']"
applied_filters = "//ul[@class='appliedFilter']/li"
sort_price_dept = "//b[text()='Pune → Kolkata']/ancestor::div[@class='paneView']/descendant::span[text()='Price']"
sort_price_arr = "//b[text()='Kolkata → Pune']/ancestor::div[@class='paneView']/descendant::span[text()='Price']"


air_cards = "//div[@class='listingCard ']"

search_card = "//*[@class='listingCard ']"
airline_name = 'descendant::span[@class="boldFont blackText"]'
source = "descendant::div[@class='flexOne timeInfoLeft']/p[@class='blackText']"
destination = "descendant::div[@class='flexOne timeInfoRight']/p[@class='blackText']"
dept_time = 'descendant::div[@class="flexOne timeInfoLeft"]/descendant::p[@class="appendBottom2 flightTimeInfo"]/span'
arr_time = 'descendant::div[@class="flexOne timeInfoRight"]/descendant::p[@class="appendBottom2 flightTimeInfo"]/span'
total_time = "descendant::div[@class='stop-info flexOne']/p"
stops = "descendant::p[@class='flightsLayoverInfo']"
fare = "descendant::p[@class='blackText fontSize16 blackFont']"
kol_to_pune = "//div[@class='listingCard ']/descendant::p[text()='₹ 12,070']"
pune_to_kol = "//label[@id='flightCard-35']/descendant::p[text()='₹ 10,390']"
fare = "descendant::div[@class='makeFlex priceInfo gap-x-10 ']/div"
book_now = ".splitFooterButton"
cont = ".lato-black"

# Switched Page

secure_trip = "//b[text()='Yes, Secure my trip. ']/ancestor::label/span[@class='customRadioBtn']"
wait_booking = "//div[@id='JOURNEY_SECTION']"

add_adult = "//button[text()='+ ADD NEW ADULT']"
adult1_fname = "input[placeholder*='First &']"
adult1_lname = "input[placeholder*='Last Name']"
adult1_gender = "//span[text()='MALE']"
adult_disability_dropdown = "//div[text()='Wheelchair']"

adult_pax = "span[class='paxname']"
check = ".adultList .customCheckbox"

mobile = "//input[@placeholder='Mobile No']"
email = "//input[@placeholder='Email']"
continue1 = "//button[text()='Continue']"
click_email = ".emailId"
confirm_button = "//button[text()='CONFIRM']"

# Next Page
seat_confirm = "//button[text()='Yes, Please']"
continue2 = "//button[text()='Continue']"
continue_anyway = "//button[text()='CONTINUE ANYWAY']"

# Proceed To pay
pay = "//button[text()='Proceed to pay']"

# Result page locators - After POM
more_airlines = "//p[text()='Airlines']/parent::div[@class='filtersOuter']/descendant::p[@class='appendBottom15']"
airlines_name = "//p[text()='Airlines']/parent::div[@class='filtersOuter']/div/label/div"

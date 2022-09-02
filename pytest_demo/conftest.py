import pytest

# Normal fixture which is basically a setup and teardown
@pytest.fixture()
def setup():
    print('I will be executing first')
    # code after the yield will execute last
    yield
    print('I will be executing last')

# To load the data using fixture, which automatically loads data
@pytest.fixture()
def dataLoad():
    print('user profile data is created')
    return ['Rahul', 'Shetty', 'rahulshettyacademy@gmail.com']


# To run tests in crossbrowser, multiple dataset will be run on same tests
# 1st Test will take Chrome
# 2nd will be Firefox
# 3rd will be IE
@pytest.fixture(params=[('chrome','Akash','DG'),('firfox','Aundh'), 'IE'])
def cross_browser(request):
    return request.param
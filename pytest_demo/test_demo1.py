# Any pytest file should start with test_ keyword file
# All code should be written in function



# all test function name should again start with test_ function name

# To run pytest we either need test runner or cmd....we cannot run it as usual ->
# it will run but nothing will be printed

# To run in CMD
# cd Path
# py.test -k CreditCard -v -s
# -k for method name execution (Regular Expression)
# -v for Verbose
# -s print console logs in o/p
# -m (mark tag) mark as smoke pytest.mark.smoke
# pytest.mark.skip -> To Skip

# fixtures are used as setup and tear down methods for test cases
# conftest file to generalize the fixture and make available to all testcases
import pytest
# @pytest.mark.smoke
# @pytest.mark.skip


# data-driven and parameterization can be done with return statements in list format
# when you define scope to class only, it will run once before class is initiate
def test_demo1(setup):
    message = "Hello"
    assert  message is "Hello", "Test Failed as String do not match "
    print(message)



def test_secondCreditCard():
    print('Hello Greeting Second Creit card')



# When testfixture Demo is executed, it will check that if any fixture is defined or not
# if yes then, the setup as it is fixture will be exetuted first and then test_fixtureDemo will execute
# It is all like prequest stuff


def test_fixtureDemo(setup):
    print('I will execute steps in fixture Demo method')



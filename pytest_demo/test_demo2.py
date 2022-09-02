def test_CreditCard(setup):
    a = 3
    b = 5
    print(a+b)
    assert a+b == 8

# Cross Browser will run multiple with  data on same tests script


def test_crossBrowser(cross_browser):
    print(cross_browser)
    print(cross_browser[1])


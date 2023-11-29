# pip install pytest-html

def test_Login(browser):
    browser.get("https://www.redbus.in/")
    assert 4 == 5

# pytest -v --html=report.html => run report HTML
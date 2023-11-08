# https://www.tutorialspoint.com/pytest/pytest_conftest_py.htm
# https://pytest-html.readthedocs.io/en/latest/user_guide.html
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import pytest_html

driver = None
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, "extras", [])
    if report.when == "call" or report.when == "setup":
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
               html = '<div><img src="%s" alt="screenshot" style="width:304px; height:228px;"' \
                     'onclick="window.open(this.src)" align="right"/></div>' % file_name
               extras.append(pytest_html.extras.html(html))
        report.extras = extras

def _capture_screenshot(name):
   driver.get_screenshot_as_file(name)

def pytest_html_report_title(report):
   report.title = "Automation Report"

@pytest.fixture(scope="session", autouse=True)
def browser():
   # global driver
   # if driver is None:
      option = webdriver.ChromeOptions()
      option.add_argument("start-maximized")
      driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=option)
      # return driver
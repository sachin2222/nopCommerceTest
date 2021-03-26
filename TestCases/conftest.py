import pytest
from selenium import webdriver
from Testdata.LoginUserData import LoginUserData

driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--incognito")
        driver = webdriver.Chrome(
            executable_path="../Drivers/chromedriver.exe",
            options=chrome_options)

    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path="../Drivers/geckodriver.exe")
        driver.maximize_window()

    driver.get("https://admin-demo.nopcommerce.com/")
    driver.implicitly_wait(20)
    request.cls.driver = driver
    yield


@pytest.fixture(scope="class")
def login():
    driver.find_element_by_id("Email").clear()
    driver.find_element_by_id("Email").send_keys("admin@yourstore.com")
    driver.find_element_by_id("Password").clear()
    driver.find_element_by_id("Password").send_keys("admin")
    driver.find_element_by_css_selector("button[type='submit']").click()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    file_path = "../Reports/"
    driver.get_screenshot_as_file(file_path + name)

import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--incognito")
        driver = webdriver.Chrome(executable_path='C:\sachin\chromeWebdriver89\chromedriver_win32\chromedriver.exe',
                                  options=chrome_options)
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path="C:\sachin\geckodriver-v0.28.0-win64\geckodriver.exe")

    driver.implicitly_wait(10)
    driver.get("https://www.myntra.com/")
    request.cls.driver = driver
    yield
    driver.quit()

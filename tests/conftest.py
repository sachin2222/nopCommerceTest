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
        driver = webdriver.Chrome(
            executable_path="../Drivers/chromedriver.exe",
            options=chrome_options)

    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path="../Drivers/geckodriver.exe")
        driver.maximize_window()

    driver.implicitly_wait(10)
    driver.get("https://www.myntra.com/")
    request.cls.driver = driver
    yield


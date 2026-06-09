import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def pytest_addoption(parser):
    parser.addoption(
        "--grid-url",
        action="store",
        default=os.getenv("SELENIUM_GRID_URL", "http://localhost:4444/wd/hub"),
        help="URL Selenium Grid Hub, например http://localhost:4444/wd/hub",
    )
    parser.addoption(
        "--browser",
        action="store",
        default=os.getenv("BROWSERS", "chrome"),
        help="Браузер или список браузеров через запятую: chrome,firefox",
    )


def pytest_generate_tests(metafunc):
    if "browser_name" in metafunc.fixturenames:
        raw_value = metafunc.config.getoption("--browser")
        browsers = [item.strip().lower() for item in raw_value.split(",") if item.strip()]
        metafunc.parametrize("browser_name", browsers, ids=browsers)


def _build_options(browser_name: str):
    if browser_name == "chrome":
        options = ChromeOptions()
        options.add_argument("--window-size=1366,768")
        return options
    if browser_name == "firefox":
        options = FirefoxOptions()
        return options
    raise ValueError(f"Unsupported browser: {browser_name}")


@pytest.fixture
def driver(request, browser_name):
    grid_url = request.config.getoption("--grid-url")
    options = _build_options(browser_name)
    driver = webdriver.Remote(command_executor=grid_url, options=options)
    driver.set_page_load_timeout(30)
    driver.implicitly_wait(0)
    driver.maximize_window()
    yield driver
    driver.quit()

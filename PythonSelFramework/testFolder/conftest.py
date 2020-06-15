import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browserName", action="store", default="chrome")


@pytest.fixture(scope="class")
def setUp(request):
    selectedBrowser = request.config.getoption("--browserName")
    if selectedBrowser.lower() == "chrome":
        # Invoke chrome browser
        driver = webdriver.Chrome(executable_path="F:\Practice\Pythonpractice\PythonSelFramework\servers\chromedriverV83.exe")
    elif selectedBrowser.lower() == "firefox":
        # Invoke Firefox browser
        driver = webdriver.Chrome(executable_path="F:\Practice\Pythonpractice\PythonSelFramework\servers\geckodriver.exe")
    elif selectedBrowser.upper() == "IE":
        # Invoke Internet Explorer browser
        driver = webdriver.Chrome(executable_path="F:\Practice\Pythonpractice\PythonSelFramework\servers\IEDriverServer.exe")
    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    request.cls.driver = driver
    yield
    driver.close()

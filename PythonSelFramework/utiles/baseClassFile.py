import pytest
import logging
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("setUp")
class BaseClass:

    def verifyLinkPresence(self, linkText, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, linkText)))

    def EnterText(self, locator, textToEnter):
        locator.clear()
        locator.send_keys(textToEnter)

    def selectByVibleText(self, locator, textToSelect):
        sel = Select(locator)
        sel.select_by_visible_text(textToSelect)

    def clickOn(self, locator):
        locator.click()

    def getTextOfElement(self, locator):
        return locator.text

    def getLogger(self):
        # loggerName = inspect.stack()[1][3]
        # logger = logging.getLogger(loggerName)
        logger = logging.getLogger(__name__)
        fileHandler = logging.FileHandler("logfile.log")
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)
        return logger

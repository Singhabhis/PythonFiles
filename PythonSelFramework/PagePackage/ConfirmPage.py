from selenium.webdriver.common.by import By


class ConfirmPageClass:

    #constructor
    def __init__(self, driver):
        self.driver = driver

    # Locator attribute
    successMsg = (By.CLASS_NAME, "alert-success")

    # Locators
    def successMsgElement(self):
        return self.driver.find_element(*ConfirmPageClass.successMsg)

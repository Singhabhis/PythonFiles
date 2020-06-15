from selenium.webdriver.common.by import By


class CheckoutClass:

    def __init__(self, driver):
        self.driver = driver

    checkout = (By.XPATH, "//button[@class='btn btn-success']")
    country = (By.ID, "country")
    countryName = (By.LINK_TEXT, "India")
    agreeTerm = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    purchase = (By.CSS_SELECTOR, "[type='submit']")

    def checkoutButton(self):
        return self.driver.find_element(*CheckoutClass.checkout)

    def countryTextBox(self):
        return self.driver.find_element(*CheckoutClass.country)

    def countryNameLink(self):
        return self.driver.find_element(*CheckoutClass.countryName)

    def agreeTermChkBox(self):
        return self.driver.find_element(*CheckoutClass.agreeTerm)

    def purchaseButton(self):
        return self.driver.find_element(*CheckoutClass.purchase)
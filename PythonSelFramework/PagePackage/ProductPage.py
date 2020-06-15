from selenium.webdriver.common.by import By


class ProductClass:

    # constructor
    def __init__(self, driver):
        self.driver = driver

    # locator attribute
    products = (By.XPATH, "//div[@class='card h-100']")
    cart = (By.CSS_SELECTOR, "a[class*='btn-primary']")

    # Locators
    def productsList(self):
        return self.driver.find_elements(*ProductClass.products)

    def cartIcon(self):
        return self.driver.find_element(*ProductClass.cart)

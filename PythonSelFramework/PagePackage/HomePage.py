from selenium.webdriver.common.by import By


class HomePage:

    # Constructor -- driver is assigned
    def __init__(self, driver):
        self.driver = driver

    # locator attribute
    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.XPATH, "//label[text()='Name']/following-sibling::input")
    email = (By.XPATH, "//input[@name='email']")
    password = (By.ID, "exampleInputPassword1")
    iceCream = (By.ID, "exampleCheck1")
    gender = (By.ID, "exampleFormControlSelect1")
    employed = (By.ID, "inlineRadio2")
    dob = (By.NAME, "bday")
    submit = (By.XPATH, "//input[@type='submit']")
    alertmsg = (By.XPATH, "//div[contains(@class,'alert-success')]")

    # locator
    def shopElement(self):
        return self.driver.find_element(*HomePage.shop)

    def nameTextBox(self):
        return self.driver.find_element(*HomePage.name)

    def emailTextBox(self):
        return self.driver.find_element(*HomePage.email)

    def passwordTextBox(self):
        return self.driver.find_element(*HomePage.password)

    def iceCreamCheckBox(self):
        return self.driver.find_element(*HomePage.iceCream)

    def genderDropDown(self):
        return self.driver.find_element(*HomePage.gender)

    def employedRadioButton(self):
        return self.driver.find_element(*HomePage.employed)

    def DOBTextBox(self):
        return self.driver.find_element(*HomePage.dob)

    def submitButton(self):
        return self.driver.find_element(*HomePage.submit)

    def alertMsgText(self):
        return self.driver.find_element(*HomePage.alertmsg)

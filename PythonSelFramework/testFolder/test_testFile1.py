from utiles.baseClassFile import BaseClass
from PagePackage.HomePage import HomePage
from PagePackage.ProductPage import ProductClass
from PagePackage.CheckoutPage import CheckoutClass
from PagePackage.ConfirmPage import ConfirmPageClass


class TestClass(BaseClass):

    def test_testCase1(self):
        log = self.getLogger()
        hp = HomePage(self.driver)
        hp.shopElement().click()
        log.info("Shop link clicked")
        pro = ProductClass(self.driver)
        products = pro.productsList()
        log.info("getting product list information")
        for product in products:
            productName = product.find_element_by_xpath("div/h4/a").text
            if productName == "Blackberry":
                #Add item into cart
                product.find_element_by_xpath("div/button").click()
                log.info("Added blackberry in cart")

        pro.cartIcon().click()
        log.info("Clicked on cart ICon")
        chkout = CheckoutClass(self.driver)
        chkout.checkoutButton().click()
        log.info("Clicked on checkout button")
        chkout.countryTextBox().send_keys("ind")
        log.info("Entered the value in country field.")
        self.verifyLinkPresence("India", timeout=7)
        chkout.countryNameLink().click()
        log.info("Country Name link clicked")
        chkout.agreeTermChkBox().click()
        log.info("checkbox Clicked")
        chkout.purchaseButton().click()
        log.info("Purchase button Clicked")
        cnfm = ConfirmPageClass(self.driver)
        successText = cnfm.successMsgElement().text
        assert "Success! Thank you!" in successText
        log.info("success present in the alert msg")
        self.driver.get_screenshot_as_file("screen.png")
        log.info("screen shot saved")

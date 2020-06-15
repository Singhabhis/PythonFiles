import pytest
from utiles.baseClassFile import BaseClass
from PagePackage.HomePage import HomePage
from TestData.HomePageData import HomePageData


class TestHomePage(BaseClass):

    def test_submitForm(self, getData):
        log = self.getLogger()
        hp = HomePage(self.driver)
        self.EnterText(hp.nameTextBox(), getData["firstName"])
        log.info("First name successfully entered")
        self.EnterText(hp.emailTextBox(), getData["lastName"])
        log.info("last name successfully entered")
        self.EnterText(hp.passwordTextBox(), getData["pwd"])
        log.info("Password entered successfully")
        self.clickOn(hp.iceCreamCheckBox())
        log.info("Checked box clicked")
        self.clickOn(hp.employedRadioButton())
        log.info("Employed selected")
        self.selectByVibleText(hp.genderDropDown(), getData["gender"])
        log.info("Gender selected")
        self.EnterText(hp.DOBTextBox(), getData["DOB"])
        log.info("Provided Data of birth")
        self.clickOn(hp.submitButton())
        log.info("Submit button Clicked")
        alertMsg = self.getTextOfElement(hp.alertMsgText())
        assert("Success" in alertMsg)
        log.info("Successfully validated")

    @pytest.fixture(params=HomePageData.getTestData("TC_1"))
    def getData(self, request):
        return request.param

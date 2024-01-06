from telnetlib import EC
from time import sleep
from pageObjects.loginPage import LoginPage
from utilities.baseClass import BaseClass

class TestHomePage(BaseClass):

    def test_homePage(self):
        loginpage = LoginPage(self.driver)
        homepage = loginpage.login("9024204345", "12345")

        # Click on the Filter button
        dropdown_toggle = homepage.click_filter()
        dropdown_toggle.click()

        # Wait for the filter options dropdown to be present
        dropdown_options = homepage.get_filter_options()
        print(len(dropdown_options))
        sleep(3)

        if len(dropdown_options) > 1:
            dropdown_options[1].click()
            print("Clicked on index 1")
        else:
            print("Dropdown doesn't have enough options.")

        sleep(3)

        homepage.get_source_data_exist()

        print(homepage.get_no_data_source())

        assert homepage.get_no_data_source() == "No data matches your selected criteria"

        homepage.click_upload_lead().click()
        sleep(2)
        homepage.click_close_upload_lead().click()
        sleep(2)
        homepage.click_create_campaign().click()
        homepage.click_campaign_back().click()
        print("title: "+homepage.get_title())

        assert homepage.get_title() == "Unsaved Changes"

        homepage.click_user_report().click()
        print("Clicked on user report")
        self.driver.back()
        homepage.click_login_report().click()
        print("Clicked on login report")
        self.driver.back()
        sleep(2)
        homepage.click_manager_user().click()
        sleep(2)
        print("Setting page title: "+homepage.get_setting_title())
        sleep(2)
        homepage.click_sidebar_dashboard().click()

        side_menu_bar = homepage.click_sidebar_button()
        sleep(2)
        print(len(side_menu_bar))
        assert len(side_menu_bar) == 9

    def test_pinned_campaigns(self):
        """Test the behavior related to pinned campaigns on the home page."""
        loginpage = LoginPage(self.driver)
        homepage = loginpage.login("446646", "12345")

        # Verify the presence of pinned campaigns
        assert homepage.get_pinned_campaign() == "Pinned Campaigns"

        # Click on the campaign report
        homepage.click_campaign_report().click()

        # Go back to the home page
        self.driver.back()

        # Perform other actions related to pinned campaigns
        homepage.click_plus_icon().click()
        sleep(2)
        homepage.click_close_popup().click()

















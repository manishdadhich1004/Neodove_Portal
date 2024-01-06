from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    title = (By.TAG_NAME, "h3")
    manage_user = (By.CSS_SELECTOR, "a[href='/settings/users']")
    dashboard_filter = (By.CSS_SELECTOR, "button[mattooltip='Filter']")
    filter_options = (By.CSS_SELECTOR, "button[role='menuitem']")
    no_source_data = (By.CSS_SELECTOR, "div[class='text-center']")
    upload_leads = (By.ID, "dashboard-upload-lead")
    close_upload_lead = (By.XPATH, "//span[text()='Close']")
    create_campaign = (By.CSS_SELECTOR, "a[href='/campaign/custom/create']")
    campaign_back = (By.CSS_SELECTOR, "i[mattooltip='Go back']")
    user_report = (By.CSS_SELECTOR, "a[href='/reports/user-report']")
    login_report = (By.CSS_SELECTOR, "a[href='/reports/login-report']")
    sidebar_dashboard = (By.ID, "nd-dashboard")
    setting_title = (By.XPATH, "//h3[text()='Settings']")
    sidebar_options = (By.CSS_SELECTOR, "span[class='mat-ripple mat-list-item-ripple']")
    pinned_campaign = (By.XPATH, "//div[text()='Pinned Campaigns']")
    campaign_report = (By.LINK_TEXT, "reports/campaign-report")
    plus_icon = (By.CSS_SELECTOR, "div[class='plus-icon']")
    pin_popup_close = (By.CSS_SELECTOR, "div[class='close-icon']")
    view_content = (By.CSS_SELECTOR, "span[class='div[class='nd-content']")
    view_all_campaign = (By.LINK_TEXT, "/campaign/all")
    source_data_exist = (By.CSS_SELECTOR, "div[class='chart-wrapper']")

    def get_title(self):
        return self.driver.find_element(*HomePage.title).text

    def click_manager_user(self):
        return self.driver.find_element(*HomePage.manage_user)

    def click_filter(self):
        return self.driver.find_element(*HomePage.dashboard_filter)

    def get_filter_options(self):
        return self.driver.find_elements(*HomePage.filter_options)

    def get_no_data_source(self):
        return self.driver.find_element(*HomePage.no_source_data).text

    def get_source_data_exist(self):
        return self.driver.find_element(*HomePage.source_data_exist).text

    def click_upload_lead(self):
        """Click on upload lead button"""
        return self.driver.find_element(*HomePage.upload_leads)

    def click_close_upload_lead(self):
        """Click on upload lead close button"""
        return self.driver.find_element(*HomePage.close_upload_lead)

    def click_create_campaign(self):
        """Click on create campaign button"""
        return self.driver.find_element(*HomePage.create_campaign)

    def click_campaign_back(self):
        """Click on campaign back button"""
        return self.driver.find_element(*HomePage.campaign_back)

    def click_user_report(self):
        """Click on user report button"""
        return self.driver.find_element(*HomePage.user_report)

    def click_login_report(self):
        """Click on login report button"""
        return self.driver.find_element(*HomePage.login_report)

    def get_setting_title(self):
        """Get setting page title"""
        return self.driver.find_element(*HomePage.setting_title).text

    def click_sidebar_dashboard(self):
        return self.driver.find_element(*HomePage.sidebar_dashboard)

    def click_sidebar_button(self):
        """Click on a button within the sidebar options"""
        return self.driver.find_elements(*HomePage.sidebar_options)

    def get_pinned_campaign(self):
        """Click on a button within the sidebar options"""
        return self.driver.find_elements(*HomePage.pinned_campaign).text

    def click_campaign_report(self):
        """Click on a button within the sidebar options"""
        return self.driver.find_elements(*HomePage.campaign_report)

    def click_plus_icon(self):
        """Click on a button within the sidebar options"""
        return self.driver.find_elements(*HomePage.plus_icon)

    def click_close_popup(self):
        """Click on a button within the sidebar options"""
        return self.driver.find_elements(*HomePage.pin_popup_close)

    def get_view_content(self):
        """Click on a button within the sidebar options"""
        return self.driver.find_elements(*HomePage.view_content)

    def click_view_all_campaign(self):
        """Click on a button within the sidebar options"""
        return self.driver.find_elements(*HomePage.view_all_campaign)
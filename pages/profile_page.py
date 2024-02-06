import allure
from pages.base_page import BasePage
from locators import ProfilePageLocators


class ProfilePage(BasePage):
    @allure.step('Wait profile page to load')
    def waiting_for_profile_page(self):
        self.wait_for_element(ProfilePageLocators.SAVE_BUTTON)

    @allure.step('Wait profile page to load')
    def waiting_for_history_page(self):
        self.wait_for_element(ProfilePageLocators.ORDER_ID)

    @allure.step('Click logout button')
    def click_logout_button(self):
        self.click_element(ProfilePageLocators.LOGOUT_BUTTON)

    @allure.step('Click history button')
    def click_history_button(self):
        self.click_element(ProfilePageLocators.HISTORY_BUTTON)

    @allure.step('Get order id from history')
    def get_order_id(self):
        return self.get_element_text(ProfilePageLocators.ORDER_ID)

import allure
from pages.base_page import BasePage
from locators import ForgotPasswordLocators


class ForgotPasswordPage(BasePage):
    @allure.step('Set the email to the field')
    def email_input(self, email):
        self.set_value(ForgotPasswordLocators.EMAIL_FIELD, email)

    @allure.step('Submit data for password recovery')
    def submit_for_password_recovery(self):
        self.click_element(ForgotPasswordLocators.PASSWORD_RECOVERY_BUTTON)
        
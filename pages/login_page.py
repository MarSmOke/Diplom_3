import allure
from pages.base_page import BasePage
from locators import LoginPageLocators


class LoginPage(BasePage):
    @allure.step('Go to the password recovery page')
    def click_recovery_password_link(self):
        self.click_element(LoginPageLocators.PASSWORD_RECOVERY_LINK)

    @allure.step('Wait login page to load')
    def waiting_for_login_page(self):
        self.wait_for_element(LoginPageLocators.PASSWORD_RECOVERY_LINK)

    @allure.step('Set the user email')
    def set_email(self, email):
        self.set_value(LoginPageLocators.EMAIL_FIELD, email)

    @allure.step('Set the user password')
    def set_password(self, password):
        self.set_value(LoginPageLocators.PASSWORD_FIELD, password)

    @allure.step('Click login button')
    def click_login_button(self):
        self.click_element(LoginPageLocators.LOGIN_BUTTON)



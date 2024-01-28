import allure
from pages.base_page import BasePage
from locators import ResetPasswordPageLocators


class ResetPasswordPage(BasePage):
    @allure.step('Click on the eye icon in the password field')
    def click_eye_icon(self):
        self.click_element(ResetPasswordPageLocators.EYE_ICON)

    @allure.step('Wait for page to load')
    def wait_reset_password(self):
        self.wait_for_element(ResetPasswordPageLocators.EYE_ICON)

    @allure.step('Wait for password field is active')
    def wait_password_field_active(self):
        return self.wait_for_element(ResetPasswordPageLocators.ACTIVE_EMAIL_FIELD)


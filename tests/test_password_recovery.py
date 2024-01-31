import allure

from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.reset_password_page import ResetPasswordPage

import data

class TestPasswordRecovery:
    @allure.title('Transition from the login page to the password recovery page')
    def test_go_to_recovery_page(self, driver):
        main_page = MainPage(driver)
        main_page.click_login_button()
        login_page = LoginPage(driver)
        login_page.waiting_for_login_page()
        login_page.click_recovery_password_link()
        assert login_page.get_current_page() == 'https://stellarburgers.nomoreparties.site/forgot-password'

    @allure.title('Password recovery with the email')
    def test_password_recovery(self, driver):
        main_page = MainPage(driver)
        main_page.click_login_button()
        login_page = LoginPage(driver)
        login_page.waiting_for_login_page()
        login_page.click_recovery_password_link()
        forgot_password_page = ForgotPasswordPage(driver)
        forgot_password_page.email_input(data.test_email)
        forgot_password_page.submit_for_password_recovery()
        reset_page = ResetPasswordPage(driver)
        reset_page.wait_reset_password()
        assert reset_page.get_current_page() == 'https://stellarburgers.nomoreparties.site/reset-password'

    @allure.title('Password field is selected by click on the eye icon')
    def test_click_on_eye_icon(self, driver):
        main_page = MainPage(driver)
        main_page.click_login_button()
        login_page = LoginPage(driver)
        login_page.waiting_for_login_page()
        login_page.click_recovery_password_link()
        forgot_password_page = ForgotPasswordPage(driver)
        forgot_password_page.email_input(data.test_email)
        forgot_password_page.submit_for_password_recovery()
        reset_page = ResetPasswordPage(driver)
        reset_page.wait_reset_password()
        reset_page.click_eye_icon()
        assert reset_page.wait_password_field_active()


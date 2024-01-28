import allure

from pages.main_page import MainPage
from pages.profile_page import ProfilePage
from pages.login_page import LoginPage


class TestUserSpace:
    @allure.title('Go to user profile')
    def test_go_to_user_profile(self, driver, user_login):
        main_page = MainPage(driver)
        main_page.click_profile_button()
        profile_page = ProfilePage(driver)
        profile_page.waiting_for_profile_page()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'

    @allure.title('Go to user order history')
    def test_go_to_user_history(self, driver, user_login):
        main_page = MainPage(driver)
        main_page.click_profile_button()
        profile_page = ProfilePage(driver)
        profile_page.waiting_for_profile_page()
        profile_page.click_history_button()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/order-history'

    @allure.title('User is logging out')
    def test_user_logout(self, driver, user_login):
        main_page = MainPage(driver)
        main_page.click_profile_button()
        profile_page = ProfilePage(driver)
        profile_page.waiting_for_profile_page()
        profile_page.click_logout_button()
        login_page = LoginPage(driver)
        login_page.waiting_for_login_page()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

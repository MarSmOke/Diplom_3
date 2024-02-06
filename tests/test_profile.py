import allure

from pages.main_page import MainPage
from pages.profile_page import ProfilePage
from pages.login_page import LoginPage

import data


class TestUserSpace:
    @allure.title('Go to user profile')
    def test_go_to_user_profile(self, driver, user_login):
        main_page = MainPage(driver)
        main_page.click_profile_button()
        profile_page = ProfilePage(driver)
        profile_page.waiting_for_profile_page()
        assert profile_page.get_current_page() == data.profile_url

    @allure.title('Go to user order history')
    def test_go_to_user_history(self, driver, user_login):
        main_page = MainPage(driver)
        main_page.click_profile_button()
        profile_page = ProfilePage(driver)
        profile_page.waiting_for_profile_page()
        profile_page.click_history_button()
        assert profile_page.get_current_page() == data.order_history_url

    @allure.title('User is logging out')
    def test_user_logout(self, driver, user_login):
        main_page = MainPage(driver)
        main_page.click_profile_button()
        profile_page = ProfilePage(driver)
        profile_page.waiting_for_profile_page()
        profile_page.click_logout_button()
        login_page = LoginPage(driver)
        login_page.waiting_for_login_page()
        assert login_page.get_current_page() == data.login_url

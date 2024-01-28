import allure

from pages.main_page import MainPage
from pages.feed_page import FeedPage


class TestConstructor:
    @allure.title('Go to feed')
    def test_go_to_feed(self, driver):
        main_page = MainPage(driver)
        main_page.click_feed_button()
        feed_page = FeedPage(driver)
        feed_page.waiting_for_feed_page()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/feed'

    @allure.title('Go to constructor')
    def test_go_to_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.click_constructor_button()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    @allure.title('Check ingredient details')
    def test_ingredient_details(self, driver):
        main_page = MainPage(driver)
        main_page.click_ingredient()
        assert main_page.get_ingredient_details_window()

    @allure.title('Close ingredient details')
    def test_close_ingredient_details(self, driver):
        main_page = MainPage(driver)
        main_page.click_ingredient()
        main_page.click_close_button()
        assert main_page.ingredient_details_is_closed()

    @allure.title('Ingredient count increases')
    def test_add_ingredient(self, driver):
        main_page = MainPage(driver)
        main_page.drag_and_drop_bun()
        assert main_page.get_buns_count().text == '2'

    @allure.title('Authorized user can make an order')
    def test_open_order_window(self, driver, user_login):
        main_page = MainPage(driver)
        main_page.waiting_for_main_page()
        main_page.click_order_button()
        assert main_page.get_order_window()


import allure

from pages.main_page import MainPage
from pages.feed_page import FeedPage
from pages.profile_page import ProfilePage


class TestUserFeed:
    @allure.title('Check order details')
    def test_order_details(self, driver):
        main_page = MainPage(driver)
        main_page.click_feed_button()
        feed_page = FeedPage(driver)
        feed_page.waiting_for_feed_page()
        feed_page.order_click()
        assert feed_page.get_order_details_window()

    @allure.title('Check order from history')
    def test_order_from_history(self, driver, user_login, make_order):
        main_page = MainPage(driver)
        main_page.click_profile_button()
        profile_page = ProfilePage(driver)
        profile_page.waiting_for_profile_page()
        profile_page.click_history_button()
        profile_page.waiting_for_history_page()
        order_id = profile_page.get_order_id()
        main_page.click_feed_button()
        feed_page = FeedPage(driver)
        feed_page.waiting_for_feed_page()
        order_feed_id = feed_page.get_order_id()
        assert f'{order_id}' in f'{order_feed_id}'

    @allure.title('Check order in progress')
    def test_order_in_progress(self, driver, user_login, make_order):
        main_page = MainPage(driver)
        main_page.click_profile_button()
        profile_page = ProfilePage(driver)
        profile_page.waiting_for_profile_page()
        profile_page.click_history_button()
        profile_page.waiting_for_history_page()
        order_id = profile_page.get_order_id()
        main_page.click_feed_button()
        feed_page = FeedPage(driver)
        feed_page.waiting_for_feed_page()
        feed_page.waiting_for_order_in_progress()
        order_in_progress = feed_page.get_order_in_progress()
        assert f'{order_id[1:]}' in f'{order_in_progress}'

    @allure.title('Check overall number of orders')
    def test_overall_order_increase(self, driver, user_login):
        main_page = MainPage(driver)
        main_page.click_feed_button()
        feed_page = FeedPage(driver)
        feed_page.waiting_for_feed_page()
        orders_count = feed_page.get_overall_orders()
        main_page.go_to_main_page()
        main_page.waiting_for_main_page()
        main_page.drag_and_drop_bun()
        main_page.drag_and_drop_sauce()
        main_page.click_order_button()
        main_page.waiting_for_order_window()
        main_page.click_close_order_button()
        main_page.click_feed_button()
        feed_page.waiting_for_feed_page()
        new_orders_count = feed_page.get_overall_orders()
        assert int(new_orders_count) == int(orders_count) + 1

    @allure.title('Check today number of orders')
    def test_today_order_increase(self, driver, user_login):
        main_page = MainPage(driver)
        main_page.click_feed_button()
        feed_page = FeedPage(driver)
        feed_page.waiting_for_feed_page()
        orders_count = feed_page.get_today_orders()
        main_page.go_to_main_page()
        main_page.waiting_for_main_page()
        main_page.drag_and_drop_bun()
        main_page.drag_and_drop_sauce()
        main_page.click_order_button()
        main_page.waiting_for_order_window()
        main_page.click_close_order_button()
        main_page.click_feed_button()
        feed_page.waiting_for_feed_page()
        new_orders_count = feed_page.get_today_orders()
        assert int(new_orders_count) == int(orders_count) + 1

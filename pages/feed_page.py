import allure
from pages.base_page import BasePage
from locators import FeedPageLocators
from locators import MainPageLocators


class FeedPage(BasePage):
    @allure.step('Wait profile page to load')
    def waiting_for_feed_page(self):
        self.wait_for_element(FeedPageLocators.HEADER)

    @allure.step('Click for order details')
    def order_click(self):
        self.click_element(FeedPageLocators.ORDER)

    @allure.step('Get order details window')
    def get_order_details_window(self):
        return self.wait_for_element(FeedPageLocators.ORDER_DETAILS_WINDOW)

    @allure.step('Get order id')
    def get_order_id(self):
        return self.get_element_text(FeedPageLocators.ORDER_FEED_ID)

    @allure.step('Get orders in progress')
    def get_order_in_progress(self):
        return self.get_element_text(FeedPageLocators.ORDERS_IN_PROGRESS)

    @allure.step('Waiting for order in progress')
    def waiting_for_order_in_progress(self):
        return self.wait_for_element(FeedPageLocators.ORDERS_IN_PROGRESS)

    @allure.step('Get overall orders count')
    def get_overall_orders(self):
        return self.get_element_text(FeedPageLocators.OVERALL_ORDERS)

    @allure.step('Get today orders count')
    def get_today_orders(self):
        return self.get_element_text(FeedPageLocators.TODAY_ORDERS)



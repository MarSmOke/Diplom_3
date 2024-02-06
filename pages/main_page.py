import allure
from pages.base_page import BasePage
from locators import MainPageLocators


class MainPage(BasePage):

    @allure.step('Click login button')
    def click_login_button(self):
        self.click_element(MainPageLocators.LOG_IN)

    @allure.step('Click LK button')
    def click_profile_button(self):
        self.click_element(MainPageLocators.PROFILE)

    @allure.step('Click feed button')
    def click_feed_button(self):
        self.click_element(MainPageLocators.FEED)

    @allure.step('Click constructor button')
    def click_constructor_button(self):
        self.click_element(MainPageLocators.CONSTRUCTOR)

    @allure.step('Click ingredient')
    def click_ingredient(self):
        self.click_element(MainPageLocators.INGREDIENT)

    @allure.step('Click close button')
    def click_close_button(self):
        self.click_element(MainPageLocators.INGREDIENT_DETAILS_CLOSE)

    @allure.step('Get ingredient details window')
    def get_ingredient_details_window(self):
        return self.wait_for_element(MainPageLocators.INGREDIENT_DETAILS_HEADER)

    @allure.step('Get ingredient details window')
    def get_order_window(self):
        return self.wait_for_element(MainPageLocators.ORDER_ID)

    @allure.step('Get buns count')
    def get_buns_count(self):
        return self.get_element(MainPageLocators.BUN_COUNTER)

    @allure.step('Click make order button')
    def click_order_button(self):
        self.click_element(MainPageLocators.MAKE_ORDER)

    @allure.step('Click make order button')
    def click_close_order_button(self):
        self.click_element(MainPageLocators.CLOSE_ORDER)

    @allure.step('Wait for main page to load')
    def waiting_for_main_page(self):
        return self.wait_for_element(MainPageLocators.MAKE_ORDER)

    @allure.step('Wait for order window to open')
    def waiting_for_order_window(self):
        return self.wait_for_element(MainPageLocators.CLOSE_ORDER)

    @allure.step('Ingredient details is closed')
    def ingredient_details_is_closed(self):
        return self.element_is_not_displayed(MainPageLocators.INGREDIENT_DETAILS_HEADER)

    @allure.step('Add bun to the burger')
    def drag_and_drop_bun(self):
        self.drag_and_drop(MainPageLocators.BUN, MainPageLocators.BURGER)

    @allure.step('Add sauce to the burger')
    def drag_and_drop_sauce(self):
        self.drag_and_drop(MainPageLocators.SAUCE, MainPageLocators.BURGER)

    @allure.step('Scroll to filling')
    def scroll_to_filling(self):
        self.scroll_to_element(MainPageLocators.FILLING)

    @allure.step('Add filling to the burger')
    def drag_and_drop_filling(self):
        self.drag_and_drop(MainPageLocators.FILLING, MainPageLocators.BURGER)

    @allure.step('Go to the main page')
    def go_to_main_page(self):
        self.click_element(MainPageLocators.CONSTRUCTOR)

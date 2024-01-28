from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver import ActionChains


class BasePage:
    def __init__(self, setup_driver):
        self.driver = setup_driver

    def get_element(self, locator):
        return self.driver.find_element(*locator)

    def get_element_text(self, locator):
        return self.driver.find_element(*locator).text

    def wait_for_element(self, locator):
        return WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(locator))

    def click_element(self, locator):
        return self.driver.find_element(*locator).click()

    def set_value(self, locator, value):
        return self.driver.find_element(*locator).send_keys(value)

    def element_is_not_displayed(self, locator):
        return WebDriverWait(self.driver, 3).until(expected_conditions.invisibility_of_element_located(locator))

    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        return self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def drag_and_drop(self, locator_1, locator_2):
        source = self.driver.find_element(*locator_1)
        target = self.driver.find_element(*locator_2)
        return ActionChains(self.driver).drag_and_drop(source, target).perform()

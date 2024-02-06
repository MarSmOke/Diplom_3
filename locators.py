from selenium.webdriver.common.by import By


class MainPageLocators:
    LOG_IN = By.XPATH, '//button[text()="Войти в аккаунт"]'
    PROFILE = By.XPATH, '//p[text()="Личный Кабинет"]'
    FEED = By.XPATH, '//p[text()="Лента Заказов"]'
    CONSTRUCTOR = By.XPATH, '//p[text()="Конструктор"]'
    MAKE_ORDER = By.XPATH, '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg"]'
    INGREDIENT = By.XPATH, '//*[contains(@href,"/ingredient/")]'
    INGREDIENT_DETAILS_HEADER = By.XPATH, '//h2[text()="Детали ингредиента"]'
    INGREDIENT_DETAILS_CLOSE = By.XPATH, '//button[contains(@class, "Modal_modal__close_modified__3V5XS")]'
    CONSTRUCTOR_HEADER = By.XPATH, '/h1[@class="text text_type_main-large mb-5 mt-10"]/'
    BURGER = By.XPATH, '//span[@class="BurgerConstructor_basket__listContainer__3P_AM"]'
    BUN = By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa6c"]'
    BUN_COUNTER = By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa6c"]//p[@class="counter_counter__num__3nue1"]'
    SAUCE = By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa73"]'
    FILLING = By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa70"]'
    ORDER_ID = By.XPATH, '//p[@class="undefined text text_type_main-medium mb-15"]'
    CLOSE_ORDER = By.XPATH, '//button[@type="button"]'


class ForgotPasswordLocators:
    PASSWORD_RECOVERY_BUTTON = By.XPATH, '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]'
    EMAIL_FIELD = By.XPATH, '//input[@class="text input__textfield text_type_main-default"]'


class ResetPasswordPageLocators:
    EYE_ICON = By.CSS_SELECTOR, '.input__icon.input__icon-action'
    ACTIVE_EMAIL_FIELD = By.CSS_SELECTOR, '.input.input_status_active'


class LoginPageLocators:
    PASSWORD_RECOVERY_LINK = By.XPATH, '//a[@href="/forgot-password"]'
    EMAIL_FIELD = By.XPATH, '//input[@type="text"]'
    PASSWORD_FIELD = By.XPATH, '//input[@type="password"]'
    LOGIN_BUTTON = By.XPATH, '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]'


class ProfilePageLocators:
    SAVE_BUTTON = By.XPATH, '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]'
    LOGOUT_BUTTON = By.XPATH, '//button[@class="Account_button__14Yp3 text text_type_main-medium text_color_inactive"]'
    HISTORY_BUTTON = By.XPATH, '//a[@href="/account/order-history"]'
    ORDER_ID = By.XPATH, '//*[contains(@class,"textBox")]//p[contains(@class,"digits-default")]'


class FeedPageLocators:
    HEADER = By.XPATH, '//h1[@class="text text_type_main-large mt-10 mb-5"]'
    ORDER = By.XPATH, '//li[@class="OrderHistory_listItem__2x95r mb-6"]'
    ORDER_DETAILS_WINDOW = By.XPATH, '//section[@class="Modal_modal_opened__3ISw4 Modal_modal__P3_V5"]'
    ORDER_FEED_ID = By.XPATH, '//p[@class="text text_type_digits-default"]'
    OVERALL_ORDERS = By.XPATH, '//p[text()="Выполнено за все время:"]/following-sibling::p'
    TODAY_ORDERS = By.XPATH, '//p[text()="Выполнено за сегодня:"]/following-sibling::p'
    ORDERS_IN_PROGRESS = By.XPATH, '//*[@class="OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi"]/li[@class="text text_type_digits-default mb-2"]'



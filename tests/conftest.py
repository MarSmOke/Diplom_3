import pytest
import requests
from selenium import webdriver

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as CS
from selenium.webdriver.firefox.service import Service as FS
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

import data
from pages.login_page import LoginPage
from pages.main_page import MainPage


@pytest.fixture(params=['chrome'])
def driver(request):
    if request.param == 'chrome':
        chrome_driver = ChromeDriverManager().install()
        service = CS(chrome_driver)
        options = Options()
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(service=service, options=options)
    elif request.param == 'firefox':
        firefox_driver = GeckoDriverManager().install()
        service = FS(firefox_driver)
        driver = webdriver.Firefox(service=service)
        driver.fullscreen_window()
    driver.get(data.base_url)
    yield driver
    driver.quit()


@pytest.fixture
def user_create_and_delete():
    payload = data.generate_credentials()
    response = requests.post(url='https://stellarburgers.nomoreparties.site/api/auth/register', data=payload)
    access_token = response.json()["accessToken"]
    yield payload
    requests.delete(url='https://stellarburgers.nomoreparties.site/api/auth/register', headers={'Authorization': access_token})


@pytest.fixture
def user_login(driver, user_create_and_delete):
    main_page = MainPage(driver)
    main_page.click_profile_button()
    login_page = LoginPage(driver)
    login_page.set_email(user_create_and_delete['email'])
    login_page.set_password(user_create_and_delete['password'])
    login_page.click_login_button()
    yield driver


@pytest.fixture
def make_order(driver, user_login):
    main_page = MainPage(driver)
    main_page.waiting_for_main_page()
    main_page.drag_and_drop_bun()
    main_page.drag_and_drop_sauce()
    main_page.scroll_to_filling()
    main_page.drag_and_drop_filling()
    main_page.click_order_button()
    main_page.waiting_for_order_window()
    main_page.click_close_order_button()
    yield driver


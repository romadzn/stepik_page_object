import pytest
from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage
import time

product_link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
login_link = "http://selenium1py.pythonanywhere.com/accounts/login/"


@pytest.mark.product_page_login
class TestLoginFromProductPage():

    @pytest.mark.parametrize('link', [product_link])
    def test_guest_should_see_login_link_on_product_page(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()

    @pytest.mark.parametrize('link', [product_link])
    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()
        page.go_to_login_page()
        page = LoginPage(browser, browser.current_url)
        page.should_be_login_page()


@pytest.mark.product_page_add
@pytest.mark.need_review
class TestUserAddToBasketFromProductPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time()) + "@fakepass"
        login_page = LoginPage(browser, login_link)
        login_page.open()
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()

    @pytest.mark.parametrize('link', [product_link])
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        page.check_equal_price()
        page.check_equal_names()

    @pytest.mark.parametrize('link', [product_link])
    def test_user_cant_see_success_message(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.is_not_success_message()


@pytest.mark.parametrize('link', [product_link])
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.check_equal_price()
    page.check_equal_names()


@pytest.mark.parametrize('link', [product_link])
def test_guest_cant_see_success_message(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.is_not_success_message()


@pytest.mark.parametrize('link', [product_link])
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(
        browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.is_not_success_message()


@pytest.mark.parametrize('link', [product_link])
@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.is_dissapeared_success_message()


@pytest.mark.parametrize('link', [product_link])
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(
        browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    page = BasketPage(browser, browser.current_url)
    page.basket_should_be_emprty()
    page.basket_should_be_emprty_text()

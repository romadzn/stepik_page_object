from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуем проверку, что есть "login" в url
        assert "/login" in self.browser.current_url, "'login' not in current url"

    def should_be_login_form(self):
        # реализуем проверку, что есть форма логина
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_FORM), "login form not in current page"

    def should_be_register_form(self):
        # реализуем проверку, что есть форма регистрации
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM
                                       ), "register form not in current page"

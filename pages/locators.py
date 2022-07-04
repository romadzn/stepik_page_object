from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    REGISTRATION_FORM = (By.ID, "register_form")
    LOGIN_FORM = (By.ID, "login_form")


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")
    MESSAGE_PRICE = (By.XPATH,"//*[@id='messages']/div[3]/div/p[1]/strong")
    BOOK_PRICE = (By.XPATH,"//*[@id='content_inner']/article/div[1]/div[2]/p[1]")
    BOOK_NAME = (By.XPATH,'//*[@id="content_inner"]/article/div[1]/div[2]/h1')
    BOOK_NAME_IN_MESSAGE = (By.XPATH,'//*[@id="messages"]/div[1]/div/strong')
    SUCCESS_MESSAGE = (By.XPATH,'//*[@id="messages"]/div[1]/div')
from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    
    def add_to_basket(self):
        # добавление товара в корзину
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()
        
    def check_equal_price(self):
        # проверка одинаковы ли цены на товар в карточке товара и в сообщении с добавлением товара.
        total_basket = self.browser.find_element(*ProductPageLocators.MESSAGE_PRICE)
        product_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE)
        print(total_basket.text)
        print(product_price.text)
        assert total_basket.text == product_price.text, "price not equal"

    def check_equal_names(self):
        # проверка одинаковы ли названия товара в карточке и в сообщении с добавлением товара     
        name_book = self.browser.find_element(*ProductPageLocators.BOOK_NAME)
        name_in_message = self.browser.find_element(*ProductPageLocators.BOOK_NAME_IN_MESSAGE)
        print(name_book.text)
        print(name_in_message.text)
        assert name_book.text == name_in_message.text, "names not equal"
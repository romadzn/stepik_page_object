from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def basket_should_be_emprty(self):
        # проверяем нет ли в корзине товаров
        assert self.is_not_element_present(*BasketPageLocators.ITEM_IN_BUSKET) 
        
    def basket_should_be_emprty_text(self):
        # ожидаем, что есть текст о том что корзина пуста 
        assert 'Your basket is empty' in self.browser.find_element(*BasketPageLocators.EMPRTY_BUSKET_MESSAGE).text

     
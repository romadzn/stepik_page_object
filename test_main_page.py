from pages.main_page import MainPage
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                    # открываем страницу
    page.go_to_login_page          # выполняем метод страницы — переходим на страницу логина (passed)

def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/" 
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()    # проверяем, есть ли на странице ссылка на логин (passed)
    
###  
  
def test_login_should_be_in_url(browser):   
    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()    # проверяем содержит ли url "login" (passed)
     
def test_login_form_should_be_in_page(browser):   
    link = "http://selenium1py.pythonanywhere.com"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_form()    # проверяем содержит ли страница форму логина (failed)
    
def test_registration_form_should_be_in_page(browser):   
    link = "http://selenium1py.pythonanywhere.com"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_register_form() # проверяем содержит ли страница форму регистрации (failed)      
from pages.main_page import MainPage
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()     # переходим на страницу с логином
    login_page = LoginPage(browser, browser.current_url)    # инициализируем LoginPage
    login_page.should_be_login_page() # делаем проверки login_page
    
def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/" 
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()    # проверяем, есть ли на странице ссылка на логин (passed)
    

  
    
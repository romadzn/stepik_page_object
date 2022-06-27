import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    #choose browser in comand line, default = chrome
    parser.addoption('--browser_name',
                     action='store',
                     default='chrome',
                     help="Chose browser: chrome or firefox")
    #choose language in comand line
    parser.addoption('--language',
                     action='store',
                     default='en',
                     help="Choose language: en/ru/es/fr/gb")

    
@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    browser_name = request.config.getoption("browser_name")
    browser = None
    # if your browser chrome
    if browser_name == "chrome":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)
    # if your browser firefox    
    elif browser_name == "firefox":
        fp = webdriver.FirefoxProfile()
        fp.set_preference('intl.accept_languages', 'language')
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(firefox_profile=fp)
    yield browser
    print("\nquit browser..")
    browser.quit() 
    
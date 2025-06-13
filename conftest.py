import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption(
        '--language',
        action='store',
        default='ru',
        help='Language code for browser locale'
    )

@pytest.fixture(scope='function')
def browser(request):
    lang = request.config.getoption('language')
    print(f'\nStarting Chrome browser with language: {lang}')
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': lang})
    driver = webdriver.Chrome(options=options)
    yield driver
    print('\nQuitting browser...')
    driver.quit()
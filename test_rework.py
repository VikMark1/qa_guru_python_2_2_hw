import pytest
from selene.support.shared import browser
from selene import be, have

@pytest.fixture()
def browser_size():
    browser.config.window_width = 500
    browser.config.window_height = 400
    yield
    browser.close()

def test_google_search(browser_size):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in Python'))

def test_negative(browser_size):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('ghdghfghfghfghf4234234').press_enter()
    browser.element('[id="topstuff"]').should(have.text('По запросу ghdghfghfghfghf4234234 ничего не найдено'))
import pytest
from selene import browser
from selene.support.shared import config


@pytest.fixture(autouse=True)
def setup_teardown():
    browser.open(config.base_url)
    yield
    browser.quit()


@pytest.fixture(autouse=True)
def setup_browser():
    config.timeout = 10
    config.window_width = 1680
    config.window_height = 1050
    config.base_url = 'https://demoqa.com/automation-practice-form'

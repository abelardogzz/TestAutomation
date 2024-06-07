import pytest
import time
from selenium import webdriver

url = "https://google.com"


# dlowload Chromedriver https://googlechromelabs.github.io/chrome-for-testing/#stable
# remove quarentine
#  xattr -d com.apple.quarantine
@pytest.fixture(scope="class")
def setup():
    browser = webdriver.Chrome()
    return browser


@pytest.mark.selenium
class TestSelenium:

    def test_simple_browser(self, setup):
        print("testing")
        setup.get(url)

        assert 'Google' in setup.title
        time.sleep(3)
        setup.quit()

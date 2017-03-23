from selenium.webdriver.common.by import By

from selenium_components import base_page
from selenium_components.google import search_page


class LandingPage(base_page.BasePage):
    """
    Page object for www.google.com
    """
    SEARCH_BOX = (By.CSS_SELECTOR, "#lst-ib")
    BUTTON_SEARCH = (By.CSS_SELECTOR, '#tsf > div.tsf-p > div.jsb > center > input[type="submit"]:nth-child(1)')

    def search(self, query):
        el = self.driver.find_element(*self.SEARCH_BOX)
        el.click()
        el.send_keys(query)

        self.driver.find_element(*self.BUTTON_SEARCH).click()
        return search_page.SearchPage(self.driver)
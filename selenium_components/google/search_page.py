from selenium.webdriver.common.by import By

from selenium_components import base_page


class SearchPage(base_page.BasePage):
    SEARCH_RESULTS = (By.CSS_SELECTOR, "#rso > div > div h3 a")

    def select_href_in_result(self, url):
        for el in self.driver.find_elements(*self.SEARCH_RESULTS):
            href = el.get_attribute("href")

            if href == url:
                el.click()
                break
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class WikipediaHomePage(BasePage):
    URL = "https://www.wikipedia.org/"

    SEARCH_INPUT = (By.ID, "searchInput")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    ENGLISH_LINK = (By.ID, "js-link-box-en")
    LOGO = (By.CLASS_NAME, "central-featured-logo")

    def open_home(self):
        self.open(self.URL)

    def is_search_visible(self) -> bool:
        return self.find_visible(self.SEARCH_INPUT).is_displayed()

    def is_english_link_visible(self) -> bool:
        return self.find_visible(self.ENGLISH_LINK).is_displayed()

    def search(self, query: str):
        self.type_text(self.SEARCH_INPUT, query)
        self.click(self.SEARCH_BUTTON)

    def open_english_version(self):
        self.click(self.ENGLISH_LINK)

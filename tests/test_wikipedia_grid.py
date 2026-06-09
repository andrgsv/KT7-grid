import pytest
from pages.wikipedia_page import WikipediaHomePage


@pytest.mark.grid
def test_home_page_opened_through_grid(driver, browser_name):
    page = WikipediaHomePage(driver)
    page.open_home()

    assert "Wikipedia" in driver.title
    assert page.is_search_visible()


@pytest.mark.grid
def test_search_article_through_grid(driver, browser_name):
    page = WikipediaHomePage(driver)
    page.open_home()
    page.search("Selenium WebDriver")

    assert "Selenium" in driver.title or "Selenium" in driver.current_url


@pytest.mark.grid
def test_language_navigation_visible_through_grid(driver, browser_name):
    page = WikipediaHomePage(driver)
    page.open_home()

    assert page.is_english_link_visible()


@pytest.mark.grid
def test_open_english_wikipedia_through_grid(driver, browser_name):
    page = WikipediaHomePage(driver)
    page.open_home()
    page.open_english_version()

    assert "wikipedia.org" in driver.current_url
    assert "English" in driver.title or "Wikipedia" in driver.title

from dataclasses import dataclass
from typing import Generator
from playwright.sync_api import sync_playwright 
from contextlib import contextmanager

from pages import Browser, MainPage
from model import SearchParameters

class SiteController:

    @contextmanager
    def _create_browser(self) -> Generator[Browser,None,None]:
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(
              headless=False, slow_mo=10
              )
            try:
                yield browser
            finally:
                browser.close()
        
    def run(self, search_parameters: SearchParameters):
        with self._create_browser() as browser:
            page = browser.new_page()
            main_page = MainPage(page)
            main_page.search_fly(search_parameters)
            
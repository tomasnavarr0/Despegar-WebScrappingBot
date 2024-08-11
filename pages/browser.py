from playwright.sync_api import Page, sync_playwright

class Browser:
    def create_page(self) -> Page:
        p = sync_playwright().start()
        browser = p.chromiun.launch(channel="chrome")
        page = browser.new_page()
        return page
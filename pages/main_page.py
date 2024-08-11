from playwright.async_api import Page, expect
from abc import abstractmethod
import time
from model import SearchParameters, Date, MONTHS

class MainPage:
    def __init__(self, page: Page):
        """Insert dates in int format"""
        self.page = page

    def validate(self) -> None:
        self.page.locator('btn-icon eva-3-icon-search').wait_for(state='visible')

    def _transform_date(self,date: str) -> Date:
        year = date[:3]
        month = date[4:6]
        day = date[6:]

        return Date(year=year,month=month,day=day)

    def search_fly(self, search_parameters: SearchParameters) -> None:

        time.sleep(2)
        self.page.goto("https://www.despegar.com.ar")
        
        time.sleep(3)
        origin_element = self.page.locator('input[placeholder="Ingresa desde dónde viajas"]')
        origin_element.click()
        origin_element.fill(search_parameters.origin)
        
        time.sleep(1)
        destination_element = self.page.locator('input[placeholder="Ingresa hacia dónde viajas"]')
        destination_element.click()
        destination_element.fill(search_parameters.destination)

        time.sleep(2)
        destination_element = self.page.locator('input[placeholder="Ida"]')
        destination_element.click()

        time.sleep(2)
        start_date = self._transform_date(search_parameters.start_date)
        end_date = self._transform_date(search_parameters.end_date)

        str_month=MONTHS[start_date.month]

        month_text = self.page.locator("div.sbox5-monthgrid-title-month").nth(0).text_content()

        while month_text != str_month:
            arrow_icon = self.page.locator("path#ico_arrow").nth(1)
            arrow_icon.click()
            time.sleep(0.5)
            month_text = self.page.locator("div.sbox5-monthgrid-title-month").nth(0).text_content()


        

import allure
import re
from playwright.sync_api import expect, Locator

from factory.component import Component


class Select(Component):
    @property
    def type_of(self) -> str:
        return 'select'
    
    def fill(self, value: str, **kwargs):
        with allure.step(f'Fill {self.type_of} "{self.entity.locator}" to value "{value}"'):
            # locator = self.get_locator(**kwargs)
            # locator.select_option(value)
            # self.page.pause()
            locator = self.locator.format(**kwargs)
            locator = "div[class='choises']"
            locator = "select[id='data.customer.contractor_id']"
            # select: Locator = self.page.locator(locator, has_text="Select an option")
            select: Locator = self.page.get_by_role("combobox").filter(has_text="Select an option")
            select.click()
            self.page.get_by_role("option", name="System contractor").click()
            self.page.get_by_role("button", name="Continue").click()
            
import allure
from playwright.sync_api import expect, Locator

from factory.component import Component


class Combobox(Component):
    @property
    def type_of(self) -> str:
        return 'combobox'
    
    def fill(self, value: str = None):
        with allure.step(f'Fill {self.type_of} "{self.entity.locator}" to value "{self.entity.value}"'):
            # self.get_locator().click()
            self.page.get_by_role("combobox", disabled=False).filter(has_text=self.entity.name).click() # "Select an option"
            self.page.get_by_role("option", name=(value if value else self.entity.value)).click()

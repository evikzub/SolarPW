import allure
import re
from playwright.sync_api import expect, Locator

from factory.component import Component


class Select(Component):
    @property
    def type_of(self) -> str:
        return 'select'
    
    def select(self, **kwargs):
        with allure.step(f'Select {self.type_of} "{self.entity.locator}" to value "{self.entity.name}"'):
            self.page.locator(self.entity.locator).select_option(self.entity.name)

            
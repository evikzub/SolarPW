from abc import ABC, abstractmethod
import allure
from playwright.sync_api import Locator, Page, expect

from entities.base_entity import BaseEntity


class Component(ABC):
    def __init__(self, page: Page, entity: BaseEntity) -> None:
        self.page = page
        self.entity = entity
        # self.name = name
        # self.locator = locator

    @property
    @abstractmethod
    def type_of(self) -> str:
        return 'component'

    def get_locator(self, **kwargs) -> Locator:
        locator = self.entity.locator.format(**kwargs)
        return self.page.locator(locator)

    def click(self, **kwargs) -> None:
        with allure.step(f'Clicking {self.type_of} with name "{self.entity.locator}"'):
            locator = self.get_locator(**kwargs)
            # print("Locator -> " + str.join("\n", locator.all_text_contents()))
            locator.click()
            # locator = self.locator.format(**kwargs)
            # print("Locator -> " + locator)
            # self.page.click(locator)

    def should_be_visible(self, **kwargs) -> None:
        with allure.step(f'Checking that {self.type_of} "{self.entity.locator}" is visible'):
            locator = self.get_locator(**kwargs)
            expect(locator).to_be_visible()

    def should_have_text(self, text: str, **kwargs) -> None:
        with allure.step(f'Checking that {self.type_of} "{self.entity.locator}" has text "{text}"'):
            locator = self.get_locator(**kwargs)
            expect(locator).to_have_text(text)

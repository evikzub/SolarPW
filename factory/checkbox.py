import allure

# from playwright.sync_api import expect, Locator
from factory.component import Component


class Checkbox(Component):
    @property
    def type_of(self) -> str:
        return "select"

    def check(self, **kwargs) -> None:
        with allure.step(f'Clicking {self.type_of} with name "{self.entity.locator}"'):
            locator = self.get_locator(**kwargs)
            if self.entity.value == "True":
                locator.check()
                # self.page.locator('input[type="checkbox"]').check()

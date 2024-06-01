import allure
from playwright.sync_api import expect

from factory.component import Component


class Input(Component):
    @property
    def type_of(self) -> str:
        return 'input'

    def fill(self, value: str = None, validate_value=False, **kwargs):
        with allure.step(f'Fill {self.type_of} "{self.entity.locator}" to value "{value}"'):
            locator = self.get_locator(**kwargs)
            locator.fill(value if value else self.entity.value)

            if validate_value:
                self.should_have_value(value, **kwargs)

    def should_have_value(self, value: str, **kwargs):
        with allure.step(f'Checking that {self.type_of} "{self.entity.locator}" has a value "{value}"'):
            locator = self.get_locator(**kwargs)
            expect(locator).to_have_value(value)

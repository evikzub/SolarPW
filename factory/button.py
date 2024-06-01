import allure
from factory.component import Component


class Button(Component):
    @property
    def type_of(self) -> str:
        return 'button'

    def click_by_name(self):
        with allure.step(f'Click {self.type_of} "{self.entity.locator}"'):
            self.page.get_by_role("button", name=self.entity.name, disabled=False).click()

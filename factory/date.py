import allure
from playwright.sync_api import expect

from factory.component import Component


class Date(Component):
    @property
    def type_of(self) -> str:
        return 'date'
    
    def fill(self, value: str = None, validate_value=False, **kwargs):
        with allure.step(f'Fill {self.type_of} "{self.entity.locator}" to value "{value}"'):
            locator = self.get_locator(**kwargs)
            # self.page.eval_on_selector(locator, "el => el.removeAttribute('readonly')")
            
            # open calendar 
            locator.click()
            # slect date
            self.page.get_by_role("option", name="30").click()
            # locator.fill(value if value else self.entity.value)

            # if validate_value:
            #     self.should_have_value(value, **kwargs)

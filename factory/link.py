import allure
from factory.component import Component


class Link(Component):
    @property
    def type_of(self) -> str:
        return 'link'
    
    def click(self, **kwargs) -> None:
        with allure.step(f'Clicking {self.type_of} with name "{self.entity.locator}"'):
            self.page.get_by_role("link", name="Customers").click()
            self.page.wait_for_url("**/customers")

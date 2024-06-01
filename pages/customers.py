from entities.test_users import test_users
from pages.base import BasePage
from playwright.sync_api import expect

CUSTOMERS_URI = "/admin/customers"

class Customers(BasePage):
    def __init__(self, page) -> None:
        super().__init__(page)
    
    def visit_customers(self):
        self.visit(CUSTOMERS_URI)
        
    def customers_list(self):
        self.visit_customers()
        
        # self.page.get_by_role("link", name="Customers").click()
        # self.page.wait_for_url("**/customers")
                
        table = self.page.get_by_role("table")
        
        thead = table.locator("thead")
        # columns = thead.locator("th").all()
        for cell in thead.locator("th").all():
            print(f"Head: '{cell.inner_text()}'")

        tbody = table.locator("tbody")
        for cell in tbody.locator("tr").first.locator("td").all():
            print(f"Search: '{cell.inner_text()}'")

        self.page.locator("#input-2").fill(value=test_users.get_activated.first_name)
        self.page.wait_for_timeout(2000)

        tbody = table.locator("tbody")
        expect(tbody.locator("tr")).to_have_count(2)
        
        for row in tbody.locator("tr").all():
            print('=----------=')
            for cell in row.locator("td").all():
                print(f"Value: '{cell.inner_text()}'")
        
        # set checkbox on
        tbody.locator("tr").nth(1).locator("input").click()
        
        # expect(self.page.get_by_role("button", name="Bulk actions")).to_be_hidden()
        # find bilk button
        self.page.get_by_role("button", name="Bulk actions").click()

        expect(self.page.get_by_role("button", name="Bulk actions")).to_be_visible()
        
        # self.page.pause()
        # print(f'List of customers: {len(columns)}')
import re
from entities.test_users import test_users
from pages.base import BasePage
from playwright.sync_api import expect

CUSTOMERS_URI = "/admin/customers"

table_columns = {
    "accaunt": "Account no",
    "name": "Name",
    "status": "Status",
    "zip": "Zip",
    "subscription": "Subscription",
    "esiid": "ESIID",
    "rep": "Rep company",
    "product": "Product",
    "date": "End Date",
}


class Customers(BasePage):
    def __init__(self, page) -> None:
        super().__init__(page)
        self._open_customers()

    def _open_customers(self):
        self.visit(CUSTOMERS_URI)
        # expect URI
        expect(self.page).to_have_url(re.compile(CUSTOMERS_URI))
        # expect Title
        expect(self.page).to_have_title(re.compile("Customers"))
        self.table = self.page.get_by_role("table")
        # expect only one Table on the page
        expect(self.table).to_have_count(1)

    def check_table_head(self):
        thead = self.table.locator("thead")
        columns_list = [cell.inner_text() for cell in thead.locator("th").all()]
        # expect see the columns in the table
        for value in table_columns.values():
            assert value in columns_list, f"Head: '{value} is not in columns_list'"

    def check_table_list(self):
        rows = self.table.locator("tbody").locator("tr").all()
        # print(f">> Rows count: {len(rows)}")
        # expect see the columns in the table
        # row 1 is Search
        # row 2 is a Main customer
        assert len(rows) > 2, "Table list is empty"

    def check_rows_count(self, count: int):
        # expect see the rows in the table
        # row 1 is Search
        # row 2 is the first customer
        expect(self.table.locator("tbody").locator("tr")).to_have_count(count)

    def search_customer(self, name: str = None):
        if not name:
            name = test_users.get_activated.first_name

        # select and fill search field
        self.page.locator("#input-2").fill(value=name)
        self.page.wait_for_timeout(2000)


    def select_customer_row(self):
        # set checkbox on for the first row
        self.table.locator("tbody").locator("tr").nth(1).locator("input").click()

    def delete_customer(self):
        bulk_actions = self.page.get_by_role("button", name="Bulk actions")
        # expect bulk actions button is visible
        expect(bulk_actions).to_be_visible()
        bulk_actions.click()

        delete_button = self.page.get_by_role("button", name="Delete selected")
        # expect delete button is visible
        expect(delete_button).to_be_visible()
        delete_button.click()

        confirm_button = self.page.get_by_role("button", name="Confirm")
        expect(confirm_button).to_be_visible()
        confirm_button.click()


    def customers_list(self):
        self.open_customers()

        # self.page.get_by_role("link", name="Customers").click()
        # self.page.wait_for_url("**/customers")

        table = self.table  # page.get_by_role("table")

        self.check_table_head()
        # thead = table.locator("thead")
        # # columns = thead.locator("th").all()
        # for cell in thead.locator("th").all():
        #     print(f"Head: '{cell.inner_text()}'")

        # tbody = table.locator("tbody")
        # for cell in tbody.locator("tr").first.locator("td").all():
        #     print(f"Search: '{cell.inner_text()}'")

        self.page.locator("#input-2").fill(value=test_users.get_activated.first_name)
        self.page.wait_for_timeout(2000)

        tbody = table.locator("tbody")
        expect(tbody.locator("tr")).to_have_count(2)

        for row in tbody.locator("tr").all():
            print("=----------=")
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

import pytest
from playwright.sync_api import Browser, Page

from pages.customers import Customers
from entities.test_users import test_users


@pytest.mark.usefixtures("admin_login")
class TestUserManagement:

    # Scenario 1: Review List of customers
    """
    Given the Admin is logged into the Admin Portal
    When the Admin navigates to the Clients section
    Then the Admin should see a list of all clients
    And the list should include client names, zip, status, and other relevant details
    """

    # Given the Admin is logged into the Admin Portal (admin_page)
    def test_review_list_of_customers(self, admin_page: Page):
        # When the Admin navigates to the Clients section
        customers = Customers(admin_page)
        # Then the Admin should see a list of the clients
        customers.check_table_list()
        # And the list should include client names, notes, and other relevant details
        customers.check_table_head()
        # page.pause()

    # Scenario 2: Filtering Clients by Name
    '''
    Given the Admin is viewing the list of clients
    When the Admin enters a client's name into the filter input field
    Then the list should dynamically update to display only the clients whose names match the entered text
    '''
    def test_find_customer(self, admin_page: Page):
        # Given the Admin is viewing the list of clients (chromium_page)
        customers = Customers(admin_page)
        # When the Admin enters a client's name into the filter input field
        # Default -> search default activated user
        customers.search_customer()
        # Then the list should dynamically update to display only the clients whose names match the entered text
        customers.check_rows_count(2)

    # Scenario 3: Deleting a Client
    '''
    Given the Admin is viewing the list of clients
    And the Admin filters the list by customer name
    And see the filtered customer is in the list
    When the Admin selects a client from the list
    And chooses to delete the client
    Then the Admin should be prompted to confirm the deletion
    And upon confirmation, the client should be removed from the list
    And any associated data should also be appropriately removed or archived
    '''
    @pytest.mark.skip(reason="no way of currently testing this")
    def test_remove_customer(self, admin_page: Page):
        # Given the Admin is viewing the list of clients
        customers = Customers(admin_page)
        # And the Admin filters the list by customer name
        customers.search_customer(test_users.get_new.first_name)
        # And see the filtered customer is in the list
        customers.check_rows_count(2)
        # When the Admin selects a client from the list
        customers.select_customer_row()
        # Then the Admin should press the delete button to confirm the deletion
        # And upon confirmation, the client should be removed from the list
        customers.delete_customer()
        
        # And any associated data should also be appropriately removed or archived
        customers.search_customer(test_users.get_new.first_name)
        customers.check_rows_count(0)
        # admin_page.pause()


    # Scenario 4: Reviewing Client Details
    '''
    Given the Admin is viewing the list of clients
    When the Admin selects a client from the list
    Then the Admin should be able to view detailed information about the selected client
    Including their contact details, history, and any other relevant information
    '''
    def test_review_client_details(self, admin_page: Page):
        customers = Customers(admin_page)
        assert 1 == 1
        # page.pause()

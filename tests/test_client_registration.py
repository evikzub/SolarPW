import pytest
from playwright.sync_api import Page
from pages.register import RegisterClient


@pytest.mark.smoke
class TestRegistration:
    
    @pytest.mark.skip(reason="no way of currently testing this")
    def test_client_register(self, default_page: Page):
        # Given the Customer is on the registration page
        rc = RegisterClient(default_page)
        # When the Customer fills in their name, address, email, and phone number
        # And clicks on the "Next" button
        # Then the Customer should proceed to the next step
        rc.client_info()

        # When the Customer selects a tariff name, enters the end date, and specifies the monthly fee
        # And clicks on the "Next" button
        # Then the Customer should proceed to the next step
        rc.client_tariff()

        # When the Customer reads and agrees to the terms and conditions
        # And clicks on the checkbox indicating agreement
        # And clicks on the "Next" button
        # Then the Customer should proceed to the next step

'''
When the Customer clicks on the "Subscribe" button
Then the Customer should be successfully registered in the application
And a confirmation message should be displayed
And the Customer should be redirected to their dashboard or a success page
'''

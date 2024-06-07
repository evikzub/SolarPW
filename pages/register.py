import re
from playwright.sync_api import Page, expect

from factory.button import Button
from factory.checkbox import Checkbox
from factory.date import Date
from factory.input import Input
from factory.combobox import Combobox
from factory.select import Select
from pages.base import BasePage
from entities.registration import registration_info, registration_tariff, registration_stripe

CLIENT_REGISTER_URI = "/customer/register"

class RegisterClient(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.first_name = Input(page, registration_info.first_name)
        self.last_name = Input(page, registration_info.last_name)
        self.email = Input(page, registration_info.email)
        self.phone = Input(page, registration_info.phone)
        self.address = Input(page, registration_info.address)
        self.city = Input(page, registration_info.city)
        self.zip = Input(page, registration_info.zip)
        self.contractor = Combobox(page, registration_info.contractor)
        # self.submit = Button(page, registration_info.submit)
        
        self.esiid = Input(page, registration_tariff.esiid)
        self.meter = Input(page, registration_tariff.meter)
        self.rep = Combobox(page, registration_tariff.rep)
        self.product = Input(page, registration_tariff.product)
        self.term = Input(page, registration_tariff.term)
        self.end_date = Date(page, registration_tariff.end_date)
        self.puct = Input(page, registration_tariff.puct)
        self.charge = Input(page, registration_tariff.charge)
        self.utility = Checkbox(page, registration_tariff.utility)
        self.note = Input(page, registration_tariff.note)
    
        self.submit = Button(page, registration_tariff.submit)

        self.card = Input(page, registration_stripe.card)
        self.cvc = Input(page, registration_stripe.cvc)
        self.expiry = Input(page, registration_stripe.expiry)
        self.name = Input(page, registration_stripe.name)
        self.country = Select(page, registration_stripe.country)
        self.zip = Input(page, registration_stripe.zip)
        self.subcribe = Button(page, registration_stripe.submit)


    def client_info(self, consultant: str = None):
        self.visit(CLIENT_REGISTER_URI)
        self.first_name.fill()
        self.last_name.fill()
        self.email.fill()
        self.phone.fill()
        self.address.fill()
        self.city.fill()
        self.zip.fill()
        if not consultant:
            self.contractor.fill(registration_info.contractor.value)
        else:
            self.contractor.fill(consultant)
        self.submit.click_by_name()
        ## ??? Validation
        # self.page.evaluate()
        # expect(self.page.get_by_text("This email already exists")).not_to_be_visible()
        # expect(self.page.get_by_text("This email already exists"), "Should not exist").not_to_be_visible()
        # self.page.pause()

    def client_tariff(self):
        self.esiid.fill()
        self.meter.fill()
        self.rep.fill(registration_tariff.rep.value)
        self.product.fill()
        self.term.fill()
        self.end_date.fill('2024-06-29')
        self.puct.fill()
        self.charge.fill()
        # self.utility.check()
        #self.note.fill() -> textarea
        self.submit.click_by_name()
        # self.page.pause()

    def terms_and_conditions(self):
        # expect(self.page).("Confirm Terms & Conditions")
        self.submit.click_by_name()
        # self.page.pause()
        
    def price_selection(self):
        # select price in Stripe
        # subs_area = self.page.locator("div[id='root']")
        # subs_area.get_by_role("button", name="Monthly") # id='1-month-tab'
        # id='1-year-tab'
        # self.page.pause()
        
        frame = self.page.frame_locator("iframe")
        # there are two price models
        expect(frame.get_by_test_id("price-column")).to_have_count(2)
        # expect(frame.get_by_label("Subscribe")).to_have_count(2)
        
        # select that cost is $5
        frame.get_by_test_id("price-column").filter(
            has_text=re.compile(r"\$5")).get_by_role("button").click()


    def subscription(self):
        # fill in Stripe
        # self.page.locator("input[id='cardNumber']").fill("4242 4242 4242 4242")
        # self.page.locator("input[id='cardExpiry']").fill("12 / 25")
        # self.page.locator("input[id='cardCvc']").fill("111")
        # self.page.locator("input[id='billingName']").fill("Joe Doe")
        # self.page.locator("select[id='billingCountry']").select_option("US")
        # self.page.locator("input[id='billingPostalCode']").fill("78724")
        # self.page.get_by_test_id("hosted-payment-submit-button").click()
        self.card.fill()
        self.cvc.fill()
        self.expiry.fill()
        self.name.fill()
        self.country.fill()
        self.zip.fill()
        self.subcribe.click()
        
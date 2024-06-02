from playwright.sync_api import Page

from factory.button import Button
from factory.checkbox import Checkbox
from factory.date import Date
from factory.input import Input
from factory.combobox import Combobox
from pages.base import BasePage
from entities.registration import registration_info, registration_tariff

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
        self.submit = Button(page, registration_info.submit)
        
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

    def client_info(self):
        self.visit(CLIENT_REGISTER_URI)
        self.first_name.fill()
        self.last_name.fill()
        self.email.fill()
        self.phone.fill()
        self.address.fill()
        self.city.fill()
        self.zip.fill()
        self.contractor.fill(registration_info.contractor.value)
        self.submit.click_by_name()
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

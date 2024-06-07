from pydantic import BaseModel

from entities.base_entity import BaseEntity
from entities.test_users import test_users


class RegistrationContacts(BaseModel):
    first_name: BaseEntity
    last_name: BaseEntity
    email: BaseEntity
    phone: BaseEntity
    address: BaseEntity
    city: BaseEntity
    # state: BaseEntity # TX by default
    zip: BaseEntity
    contractor: BaseEntity
    submit: BaseEntity

test_user = test_users.get_new

_info = {
    "first_name": {
        "locator": "input[id='data.customer.first_name']",
        "value": test_user.first_name
    },
    "last_name": {
        "locator": "input[id='data.customer.last_name']",
        "value": test_user.last_name
    },
    "email": {
        "locator": "input[id='data.email']",
        "value": test_user.login
    },
    "phone": {
        "locator": "input[id='data.customer.phone']",
        "value": "(800) 111-0000"
    },
    "address": {
        "locator": "input[id='data.customer.address_line_1']",
        "value": "address"
    },
    "city": {
        "locator": "input[id='data.customer.city']",
        "value": "Dallas"
    },
    "zip": {
        "locator": "input[id='data.customer.zip']",
        "value": "78724"
    },
    "contractor": {
        # "locator": "select[id='data.customer.contractor_id']",
        "locator": "combobox[name='Select an option']",
        "name": "Select an option",
        "value": "Contractor3",
    },
    "submit": {
        # "locator": "select[id='data.customer.contractor_id']",
        "locator": "button[name='Continue']",
        "name": "Continue"
    },
}

registration_info = RegistrationContacts.model_validate(_info)


class RegistrationTariff(BaseModel):
    esiid: BaseEntity
    meter: BaseEntity
    rep: BaseEntity
    product: BaseEntity
    term: BaseEntity
    end_date: BaseEntity
    puct: BaseEntity
    charge: BaseEntity
    utility: BaseEntity
    note: BaseEntity
    submit: BaseEntity
    
_tariff = {
    "esiid": {
        "locator": "input[id='data.customer.esiid']",
        "value": "01234554321012345"
    },
    "meter": {
        "locator": "input[id='data.customer.smt_number']",
        "value": "12345"
    },
    "rep": {
        "locator": "combobox[id='data.rep']",
        "name": "Select an option",
        "value": "Bulb",
    },
    "product": {
        "locator": "input[id='data.tariff.name']",
        "value": "Yearly Energy Charge"
    },
    "term": {
        "locator": "input[id='data.tariff.terms']",
        "value": "12345"
    },
    "end_date": {
        "locator": "input[id='data.tariff.end_date']",
        "value": "May 31, 2025"
    },
    "puct": {
        "locator": "input[id='data.tariff.puct_certificate']",
        "value": "12345"
    },
    "charge": {
        "locator": "input[id='data.tariff.energy_charge']",
        "value": "550"
    },
    "utility": {
        "locator": "checkbox[id='data.tariff.utility_passthrough']",
        "value": "True"
    },
    "note": {
        "locator": "input[id='data.tariff.description']",
        "value": "",
    },
    "back": {
        "locator": "button[name='Back']",
        "name": "Back"
    },    
    "submit": {
        "locator": "button[name='Continue']",
        "name": "Continue"
    },
}

registration_tariff = RegistrationTariff.model_validate(_tariff)

class RegistrationStripe(BaseModel):
    card: BaseEntity
    expiry: BaseEntity
    cvc: BaseEntity
    name: BaseEntity
    country: BaseEntity
    zip: BaseEntity
    submit: BaseEntity
    
_stripe = {
    "card": {
        "locator": "input[id='cardNumber']",
        "name": "4242 4242 4242 4242"
    },
    "expiry": {
        "locator": "input[id='cardExpiry']",
        "name": "12 / 25"
    },
    "cvc": {
        "locator": "input[id='cardCvc']",
        "name": "111"
    },
    "name": {
        "locator": "input[id='billingName']",
        "name": "Joe Doe"
    },
    "country": {
        "locator": "select[id='billingCountry']",
        "name": "US"
    },
    "zip": {
        "locator": "input[id='billingPostalCode']",
        "name": "Joe Doe"
    },
    "submit": {
        "locator": "button[test_id='hosted-payment-submit-button']",
        "name": "Joe Doe"
    },
}

registration_stripe = RegistrationStripe.model_validate(_stripe)

# SolarPW
## Clone code
git clone https://github.com/evikzub/SolarPW.git SolarPW
cd solarpw
code .

## VEnv Preparation
mkdir venv
python -m venv venv
venv\Scripts\activate

## Install
pip install playwright
pip install pytest
pip install allure-pytest
pip install pydantic

## Run
pytest -m smoke
pytest test_client_registration.py

## locators
https://playwright.dev/python/docs/locators

playwright codegen <url>


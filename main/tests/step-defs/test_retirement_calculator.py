from pytest_bdd import scenario, given, when, then, parsers
import pytest
from main.retirement_calculator import *


# "Constants"
BIRTH_YEAR = 1940
BIRTH_MONTH = 7

@pytest.fixture
def calculator():
    c = RetirementCalculator()
    yield c

@given('the user is on the calculator')
def user_start_calcultor(calculator):
    calculator = RetirementCalculator()

@when(parsers.parse('the birth year is "{birth_year}"'))
def calculate_retirement_age(calculator, birth_year):
    (year, month) = calculator.getRetirementAge(int(birth_year))

@then(parsers.parse('the results will show the age of "{birth_results}"'))
def calculate_retirement_age_results(calculator, birth_results):
    assert birth_results == str(calculator.age_year) + "  years and " + str(calculator.age_month) + " months"

@given('the user is on the date calculator')
def user_start_date_calcultor(calculator):
    calculator = RetirementCalculator()

@when(parsers.parse('the birth year is "{birth_date}"'))
def calculate_retirement_age(calculator, birth_date):
    input_date = birth_date.split(", ")
    input_year = int(input_date[0])
    input_month = int(input_date[1])
    (age_year, age_month) = calculator.getRetirementAge(input_year)
    (year, month) = calculator.getDateForFullBenefits(input_year, input_month, age_year, age_month)

@then(parsers.parse('the results will show the date of "{birth_date_results}"'))
def calculate_retirement_age_results(calculator, birth_date_results):
    assert birth_date_results == "month " + str(calculator.retire_month) + " in the year " + str(calculator.retire_year)







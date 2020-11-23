from pytest_bdd import scenarios, given, when, then, parsers
import pytest
from main.retirement_calculator import RetirementCalculator

scenarios('../features/retirement_calculator.feature')


@pytest.fixture
def calculator():
    return RetirementCalculator()


@given('the user is on the calculator')
def user_start_calculator(calculator):
    calculator = RetirementCalculator()


@when(parsers.parse('the birth year is <birth_year>'))
def calculate_retirement_age(calculator, birth_year):
    calculator.getRetirementAge(int(birth_year))


@then(parsers.parse('the results will show the age of <age_year> years and <age_month> months'))
def calculate_retirement_age_results(calculator, age_year, age_month):
    assert age_year == str(calculator.age_year) and age_month == str(calculator.age_month)


@given('the user is on the date calculator')
def user_start_date_calculator(calculator):
    calculator = RetirementCalculator()


@when(parsers.parse('the birth date is <birth_year> and <birth_month>'))
def calculate_retirement_age(calculator, birth_year, birth_month):
    input_year = int(birth_year)
    input_month = int(birth_month)
    calculator.getRetirementAge(input_year)
    calculator.getDateForFullBenefits(input_year, input_month)


@then(parsers.parse('the results will show the date of <retire_month> in the year <retire_year>'))
def calculate_retirement_age_results(calculator, retire_month, retire_year):
    assert retire_month == str(calculator.retire_month) and retire_year == str(calculator.retire_year)








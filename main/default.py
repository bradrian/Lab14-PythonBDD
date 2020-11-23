from main.retirement_calculator import RetirementCalculator
import calendar

retire_calculator = RetirementCalculator()

print("Social Security Full Retirement Age Calculator")

loop = True
while loop:
    print("")
    year = str(input("Enter the year of birth or to exit ")).strip()
    print("")
    loop = (year != "")
    if loop:

        month = str(input("Enter the month of birth ")).strip()
        print("")

        retYear, retMonth = retire_calculator.getRetirementAge(int(year))
        print("your full retirement age is", retYear, "and", retMonth, "months")
        print("")

        retireYear, retireMonth = retire_calculator.getDateForFullBenefits(int(year), int(month))
        display_month = calendar.month_name[retireMonth]
        print("this will be in", display_month, "of", retireYear)
        print("")

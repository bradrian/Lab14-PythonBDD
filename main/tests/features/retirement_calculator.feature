Feature:  Full Retirement Age Calculator
    I would like to give an easy resource to people to help them figure out what age they can retire, so they can plan their savings accordingly.

Scenario: Calculate retirement age
	Given the user is on the calculator
	When the birth year is "1937"
	Then the results will show the age of "65 years and 0 months"

Scenario: Calculate retirement date
	Given the user is on the date calculator
	When the birth date is "2001, 1"
	Then the results will show the date of "month 1 in the year 2068"

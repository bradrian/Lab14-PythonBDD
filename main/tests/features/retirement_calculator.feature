Feature:  Full Retirement Age Calculator
    I would like to give an easy resource to people to help them figure out what age they can retire, so they can plan their savings accordingly.

Scenario: Calculate retirement age
	Given the user is on the calculator
	When the birth year is <birth_year>
	Then the results will show the age of <age_year> years and <age_month> months

    Examples:
        | birth_year | age_year | age_month |
        |    1937    |    65    |     0     |
        |    1938    |    65    |     2     |
        |    1939    |    65    |     4     |
        |    1940    |    65    |     6     |
        |    1941    |    65    |     8     |
        |    1942    |    65    |     10    |
        |    1954    |    66    |     0     |
        |    1955    |    66    |     2     |
        |    1956    |    66    |     4     |
        |    1957    |    66    |     6     |
        |    1958    |    66    |     8     |
        |    1959    |    66    |     10    |
        |    1960    |    67    |     0     |


Scenario: Calculate retirement date
	Given the user is on the date calculator
	When the birth date is <birth_year> and <birth_month>
	Then the results will show the date of <retire_month> in the year <retire_year>

    Examples:
        | birth_year | birth_month | retire_year | retire_month |
        |    1940    |      7      |    2006     |       1      |
        |    2001    |      1      |    2068     |       1      |

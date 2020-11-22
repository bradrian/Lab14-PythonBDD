class RetirementCalculator:
    def __init__(self):
        self.birth_year = 0
        self.retire_year = 0
        self.retire_month = 0
        self.age_year = 0
        self.age_month = 0


    def getRetirementAge(self, year):
        self.age_year = 0
        self.age_month = 0

        if year < 1937:
            self.age_year = 65
        elif 1937 <= year < 1943:
            self.age_year = 65
            self.age_month = (year - 1937) * 2
        elif 1943 <= year < 1954:
            self.age_year = 66
        elif 1954 <= year < 1960:
            self.age_year = 66
            self.age_month = (year - 1954) * 2
        elif year >= 1960:
            self.age_year = 67
        return self.age_year, self.age_month


    def getDateForFullBenefits(self, year, month):
        self.retire_year = 0
        self.retire_month = 0

        ret_year, ret_month = self.getRetirementAge(year)
        self.retire_month = month + ret_month

        while self.retire_month > 12:
            self.retire_month -= 12
            ret_year += 1

        self.retire_year = year + ret_year

        return self.retire_year, self.retire_month

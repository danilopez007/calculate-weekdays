""" Written by Dani Lopez
    Last update: 2024-07-23
    Description: Determines the number of weekdays between two dates, inclusive of both the first and second date.
"""

import copy
import sys


class MyDataClass:
    # constuctor
    def __init__(self, month, day, year):
        self.month = int(month)
        self.day = int(day)
        self.year = int(year)

    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    """ input: Date as instance of MyDataClass
        return: Number of leap years between 0 and the year of the date provided as an integer
        description: Calculates the number of leap years that have occured up to and included the year of
                        the date provided
    """

    def count_leap_years(self):
        years = self.year
        # If the date is before March in a leap year, don't count this year as a leap year
        if self.month <= 2:
            years -= 1

        return years // 4 - years // 100 + years // 400

    """ input: Date as instance of MyDataClass
        return: boolean
        description: Determines if the year of the date provided is a leap year
    """

    def is_leap_year(self):
        if (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0):
            return True
        return False

    """ input: Two dates, as instances of myDataClass
        return: Number of days between the two dates as an integer
        description: Calculates the number of days between the two provided dates, taking into account leap years. 
                        Calculation is inclusive of the first date, exclusive of the second date.
    """
    @staticmethod
    def num_days(start_date, end_date):
        start_date_sum = (start_date.year * 365) + start_date.day

        for i in range(0, start_date.month - 1):
            start_date_sum += MyDataClass.days_in_month[i]

        start_date_sum += start_date.count_leap_years()

        end_date_sum = (end_date.year * 365) + end_date.day
        for i in range(0, end_date.month - 1):
            end_date_sum += MyDataClass.days_in_month[i]

        end_date_sum += end_date.count_leap_years()

        return (end_date_sum - start_date_sum) + 1

    """ input: Date as instance of MyDataClass
        return: Integer representing day of the week
        description: Determines day of the week for a given date using Zeller's Congruence

        0 : "Saturday",
        1 : "Sunday",
        2 : "Monday",
        3 : "Tuesday",
        4 : "Wednesday",
        5 : "Thursday",
        6 : "Friday",
    """
    @staticmethod
    def day_of_week(date):
        month = date.month
        day = date.day
        year = date.year

        if (month == 1):
            month = 13
            year -= 1

        if (month == 2):
            month = 14
            year -= 1

        q = day
        m = month
        k = year % 100
        j = year // 100
        h = (q + 13 * (m + 1) // 5 + k + k // 4 + j // 4 + 5 * j) % 7

        return h

    """ input: Two dates, as instances of MyDataClass
        return: Number of weekend days between two dates, as an integer
        description: Calculates the number of weekend days between two dates
    """
    @staticmethod
    def num_weekend_days(start_date, end_date):
        current_date = copy.deepcopy(start_date)
        weekend_days = 0

        while (current_date.year < end_date.year) or (current_date.year == end_date.year and current_date.month < end_date.month) or (current_date.year == end_date.year and current_date.month == end_date.month and current_date.day <= end_date.day):
            day_of_week = MyDataClass.day_of_week(current_date)
            if day_of_week == 0 or day_of_week == 1:
                weekend_days += 1

            current_date.day += 1
            if current_date.day > MyDataClass.days_in_month[current_date.month - 1]:
                if current_date.month == 2 and current_date.is_leap_year():
                    if current_date.day > 29:
                        current_date.day = 1
                        current_date.month += 1
                else:
                    current_date.day = 1
                    current_date.month += 1
                if current_date.month > 12:
                    current_date.month = 1
                    current_date.year += 1

        return weekend_days

    """ input: Two dates, as instances of MyDataClass
        return: Number of week days between two dates, as an integer
        description: Calculates the number of week days between two dates
    """
    @staticmethod
    def num_week_days(start_date, end_date):
        return MyDataClass.num_days(start_date, end_date) - MyDataClass.num_weekend_days(start_date, end_date)


def main():
    # Check for correct number of command line arguements, then parse
    if len(sys.argv) != 3:
        print("Usage: python3 myDataClass.py <start_date> <end_date>")
        sys.exit(1)

    start_date = sys.argv[1].split("-")
    end_date = sys.argv[2].split("-")

    start_date = MyDataClass(*start_date)
    end_date = MyDataClass(*end_date)

    print(MyDataClass.num_week_days(start_date, end_date))


if __name__ == '__main__':
    main()

""" Written by Dani Lopez
    Last update: 2024-07-23
    Description: Unittests for myDataClass.
"""

import unittest
from myDataClass import MyDataClass

date1 = MyDataClass(7, 6, 2024)  # Saturday
date2 = MyDataClass(7, 7, 2024)  # Sunday
date3 = MyDataClass(7, 8, 2024)  # Monday
date4 = MyDataClass(7, 9, 2024)  # Tuesday
date5 = MyDataClass(7, 10, 2024)  # Wednesday
date6 = MyDataClass(7, 11, 2024)  # Thursday
date7 = MyDataClass(7, 12, 2024)  # Friday
date8 = MyDataClass(7, 13, 2024)  # Saturday
date9 = MyDataClass(7, 14, 2024)  # Sunday
date10 = MyDataClass(7, 15, 2024)  # Monday


class TestDataClass(unittest.TestCase):
    def test_num_week_days(self):
        self.assertEqual(MyDataClass.num_week_days(
            date1, date2), 0)  # July 6-7
        self.assertEqual(MyDataClass.num_week_days(
            date1, date3), 1)  # July 6-8
        self.assertEqual(MyDataClass.num_week_days(
            date1, date4), 2)  # July 6-9
        self.assertEqual(MyDataClass.num_week_days(
            date1, date5), 3)  # July 6-10
        self.assertEqual(MyDataClass.num_week_days(
            date1, date6), 4)  # July 6-11
        self.assertEqual(MyDataClass.num_week_days(
            date1, date7), 5)  # July 6-12

        # Saturday to Saturday, July 6-13
        self.assertEqual(MyDataClass.num_week_days(date1, date8), 5)
        # Saturday to Sunday, July 6-14
        self.assertEqual(MyDataClass.num_week_days(date1, date9), 5)
        # Saturday to weekday, July 6-15
        self.assertEqual(MyDataClass.num_week_days(date1, date10), 6)
        self.assertEqual(MyDataClass.num_week_days(
            date2, date9), 5)  # Sunday to Sunday, July 7-14
        # Sunday to Saturday, July 7-13
        self.assertEqual(MyDataClass.num_week_days(date2, date8), 5)
        # Sunday to weekday, July 7-12
        self.assertEqual(MyDataClass.num_week_days(date2, date7), 5)
        # weekday to Saturday, July 8-13
        self.assertEqual(MyDataClass.num_week_days(date3, date8), 5)
        # weekday to Sunday, July 8-14
        self.assertEqual(MyDataClass.num_week_days(date2, date9), 5)
        # weekday to weekday, July 8-12
        self.assertEqual(MyDataClass.num_week_days(date3, date7), 5)

        self.assertEqual(MyDataClass.num_week_days(MyDataClass(
            1, 1, 2024), MyDataClass(12, 31, 2024)), 262)  # leap year
        self.assertEqual(MyDataClass.num_week_days(MyDataClass(
            1, 1, 2023), MyDataClass(12, 31, 2023)), 260)  # non-leap year

        self.assertEqual(MyDataClass.num_week_days(MyDataClass(
            1, 1, 2000), MyDataClass(12, 31, 2000)), 260)  # century leap year
        self.assertEqual(MyDataClass.num_week_days(MyDataClass(
            1, 1, 1900), MyDataClass(12, 31, 1900)), 261)  # century non-leap year

        self.assertEqual(MyDataClass.num_week_days(
            MyDataClass(1, 1, 2027), MyDataClass(12, 31, 2027)), 261)

        self.assertEqual(MyDataClass.num_week_days(MyDataClass(
            7, 15, 2024), MyDataClass(7, 15, 2024)), 1)  # same date, weekday

        self.assertEqual(MyDataClass.num_week_days(MyDataClass(
            7, 14, 2024), MyDataClass(7, 14, 2024)), 0)  # same date, sunday

        self.assertEqual(MyDataClass.num_week_days(MyDataClass(
            7, 13, 2024), MyDataClass(7, 13, 2024)), 0)  # same date, saturday

        self.assertEqual(MyDataClass.num_week_days(MyDataClass(
            12, 31, 2023), MyDataClass(1, 1, 2024)), 1)  # year boundary

        self.assertEqual(MyDataClass.num_week_days(
            MyDataClass(1, 1, 1990), MyDataClass(1, 1, 2010)), 5220)
        self.assertEqual(MyDataClass.num_week_days(
            MyDataClass(3, 7, 1995), MyDataClass(2, 12, 2006)), 2854)
        self.assertEqual(MyDataClass.num_week_days(
            MyDataClass(3, 7, 1993), MyDataClass(2, 12, 2027)), 8855)
        self.assertEqual(MyDataClass.num_week_days(
            MyDataClass(3, 7, 1993), MyDataClass(2, 12, 2000)), 1810)
        self.assertEqual(MyDataClass.num_week_days(
            MyDataClass(3, 7, 1992), MyDataClass(11, 12, 2000)), 2265)


if __name__ == '__main__':
    unittest.main()

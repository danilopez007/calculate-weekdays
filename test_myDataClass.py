""" Written by Dani Lopez
    Last update: 2024-07-08
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

date11 = MyDataClass(1, 1, 2024)  # Leap year, 262 week days
date12 = MyDataClass(12, 31, 2024)

date13 = MyDataClass(1, 1, 2023)  # Non-leap year, 260 week days
date14 = MyDataClass(12, 31, 2023)

date15 = MyDataClass(1, 1, 2000)  # Century leap year, 260 week days
date16 = MyDataClass(12, 31, 2000)

date17 = MyDataClass(1, 1, 1900)  # Centruy non-leap year, 261 week days
date18 = MyDataClass(12, 31, 1900)

date19 = MyDataClass(1, 1, 2027)  
date20 = MyDataClass(12, 31, 2027)


class TestDataClass(unittest.TestCase):
    def test_num_week_days(self):
        self.assertEqual(MyDataClass.num_week_days(date1, date2), 0)
        self.assertEqual(MyDataClass.num_week_days(date1, date3), 1)
        self.assertEqual(MyDataClass.num_week_days(date1, date4), 2)
        self.assertEqual(MyDataClass.num_week_days(date1, date5), 3)
        self.assertEqual(MyDataClass.num_week_days(date1, date6), 4)
        self.assertEqual(MyDataClass.num_week_days(date1, date7), 5)

        self.assertEqual(MyDataClass.num_week_days(
            date1, date8), 5)  # Saturday to Saturday
        self.assertEqual(MyDataClass.num_week_days(
            date1, date9), 5)  # Saturday to Sunday
        self.assertEqual(MyDataClass.num_week_days(
            date1, date10), 6)  # Saturday to weekday
        self.assertEqual(MyDataClass.num_week_days(
            date2, date9), 5)  # Sunday to Sunday
        self.assertEqual(MyDataClass.num_week_days(
            date2, date8), 5)  # Sunday to Saturday
        self.assertEqual(MyDataClass.num_week_days(
            date2, date7), 5)  # Sunday to weekday
        self.assertEqual(MyDataClass.num_week_days(
            date2, date8), 5)  # weekday to Saturday
        self.assertEqual(MyDataClass.num_week_days(
            date2, date9), 5)  # weekday to Sunday

        self.assertEqual(MyDataClass.num_week_days(
            date11, date12), 262)  # leap year
        self.assertEqual(MyDataClass.num_week_days(
            date13, date14), 260)  # non-leap year

        self.assertEqual(MyDataClass.num_week_days(
            date15, date16), 260)  # century leap year
        self.assertEqual(MyDataClass.num_week_days(
            date17, date18), 261)  # century non-leap year
        
        self.assertEqual(MyDataClass.num_week_days(
            date19, date20), 261) 


if __name__ == '__main__':
    unittest.main()

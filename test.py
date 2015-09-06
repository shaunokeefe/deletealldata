import unittest
import datetime

from deleteolddata.delete import date_from_days


class CalculateOlderTest(unittest.TestCase):

    def test_calculate_date(self):
        today = datetime.date(2015, 9, 6)
        days = 1
        [year, month, day] = date_from_days(today, days)
        self.assertEqual(year, 2015)
        self.assertEqual(month, 9)
        self.assertEqual(day, 5)

    def test_calculate_date_across_month(self):
        today = datetime.date(2015, 9, 1)
        days = 2
        [year, month, day] = date_from_days(today, days)
        self.assertEqual(year, 2015)
        self.assertEqual(month, 8)
        self.assertEqual(day, 30)

    def test_calculate_date_across_year(self):
        today = datetime.date(2015, 2, 1)
        days = 32
        [year, month, day] = date_from_days(today, days)
        self.assertEqual(year, 2014)
        self.assertEqual(month, 12)
        self.assertEqual(day, 31)

    def test_calculate_date_zero_days(self):
        today = datetime.date(2015, 9, 6)
        days = 0
        [year, month, day] = date_from_days(today, days)
        self.assertEqual(year, 2015)
        self.assertEqual(month, 9)
        self.assertEqual(day, 6)

if __name__ == '__main__':
    unittest.main()

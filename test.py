import datetime
import mock
import unittest

from deleteolddata.delete import date_from_days, calculate_recursion_depth,\
    process_directories


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


class CalculateCurrentLevelTest(unittest.TestCase):
    def test_year(self):
        root = "/first/second"
        current = "/first/second/dataset/year"

        level = calculate_recursion_depth(root, current)

        self.assertEqual(level, 'month')

    def test_dataset(self):
        root = "/first/second"
        current = "/first/second"

        level = calculate_recursion_depth(root, current)

        self.assertEqual(level, 'dataset')

    def test_month(self):
        root = "/first/second"
        current = "/first/second/dataset/year"

        level = calculate_recursion_depth(root, current)

        self.assertEqual(level, 'month')

    def test_day(self):
        root = "/first/second"
        current = "/first/second/dataset/year/month"

        level = calculate_recursion_depth(root, current)

        self.assertEqual(level, 'day')


class ProcessDirectoriesTest(unittest.TestCase):

    def test_dataset(self):
        dataset = 'dataset1'
        filters = {
            'dataset': dataset,
            'year': 2015,
            'month': 9,
            'day': 1,
        }
        current_level = 'dataset'
        directories = ['dataset1', 'dataset2', 'dataset3']
        dry_run = False

        process_directories(directories, filters, current_level, dry_run)

        self.assertEqual(len(directories), 1)
        self.assertEqual(directories[0], 'dataset1')

    @mock.patch('deleteolddata.delete.remove_directory')
    def test_year(self, remove_directory_mock):
        dataset = None
        filters = {
            'dataset': dataset,
            'year': 2014,
            'month': 9,
            'day': 1,
        }
        current_level = 'year'
        directories = ['2013', '2014', '2015']
        dry_run = False

        process_directories(directories, filters, current_level, dry_run)

        self.assertEqual(len(directories), 1)
        self.assertTrue('2014' in directories)
        remove_directory_mock.assert_has_calls([mock.call('2013', False)])

    @mock.patch('deleteolddata.delete.remove_directory')
    def test_month(self, remove_directory_mock):
        dataset = None
        filters = {
            'dataset': dataset,
            'year': 2014,
            'month': 9,
            'day': 1,
        }
        current_level = 'month'
        directories = ['09', '08', '01']
        dry_run = False

        process_directories(directories, filters, current_level, dry_run)

        self.assertEqual(len(directories), 1)
        self.assertTrue('09' in directories)
        remove_directory_mock.assert_has_calls([mock.call('08', False), mock.call('01', False)])

    @mock.patch('deleteolddata.delete.remove_directory')
    def test_no_directories_to_process(self, remove_directory_mock):
        dataset = None
        filters = {
            'dataset': dataset,
            'year': 2014,
            'month': 9,
            'day': 1,
        }
        current_level = 'day'
        directories = []
        dry_run = False

        process_directories(directories, filters, current_level, dry_run)

        self.assertEqual(len(directories), 0)
        self.assertEqual(remove_directory_mock.call_count, 0)

if __name__ == '__main__':
    unittest.main()

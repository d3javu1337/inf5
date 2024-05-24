import unittest
from company import TopManager

class Test(unittest.TestCase):
    def setUp(self):
        self.__topmanager = TopManager()

    def test_getMonthSalary_over(self):
        self.assertEqual(self.__topmanager.getMonthSalary(20_000_000), 375_000)

    def test_getMonthSalary_under(self):
        self.assertEqual(self.__topmanager.getMonthSalary(1_000_000), 150_000)

unittest.main()
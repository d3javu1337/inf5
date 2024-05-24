import unittest
from company import Manager

class Test(unittest.TestCase):
    def setUp(self):
        self.__manager = Manager()

    def test_getMonthSalary(self):
        self.assertEqual(self.__manager.getMonthSalary(1_000_000), 150000)

unittest.main()
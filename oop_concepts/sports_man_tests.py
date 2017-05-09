from unittest import TestCase
from sports_man import SportsMan


class TestCasesSportsMan(TestCase):
    """Tests the functionality of the base class SportsMan"""
    def SetUp(self):
        """Grants access to all the testcases an instance of SportsMan"""
        self.sportsman = SportsMan()

    def tearDown(self):
        del self.sportsman

    def test_sportsman_full_name(self):
        self.assertTrue(self.sportsman.fullname('John' + 'Doe'), 'John Doe')

    def test_pay_raise_is_right(self):
        self.pay_raise_index = 1.5
        self.assertTrue(self.sportsman.pay_raise(2000 * self.pay_raise_index), 30000)

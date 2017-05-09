from unittest import TestCase
from sports_man import SportsMan


class TestCasesSportsMan(TestCase):
    """Tests the functionality of the base class SportsMan"""

    def test_sportsman_full_name(self):
        self.sportsman = SportsMan('Allan', 'Smith', 60000)
        self.assertTrue(self.sportsman.fullname(), 'Allan Smith')

    def test_pay_raise_is_right(self):
        self.sportsman = SportsMan('Allan', 'Smith', 60000)
        self.assertEqual(self.sportsman.pay_raise(), 90000)
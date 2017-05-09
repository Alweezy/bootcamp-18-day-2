from unittest import TestCase
from sports_man import SportsMan, Player


class TestCasesSportsMan(TestCase):
    """Tests the functionality of the base class SportsMan"""

    def test_sportsman_full_name(self):
        self.sportsman = SportsMan('Allan', 'Smith', 60000)
        self.assertTrue(self.sportsman.fullname(), 'Allan Smith')

    def test_pay_raise_is_right(self):
        self.sportsman = SportsMan('Allan', 'Smith', 60000)
        self.assertEqual(self.sportsman.pay_raise(), 90000)


class TestCasesPlayer(TestCase):
    """Test is the class player inherits from Sportsman """
    def test_player_inherits_from_SportsMan(self):
        self.assertTrue(issubclass(Player, SportsMan))

    def test_player_full_name(self):
        self.player = Player('Wayne', 'Rooney', 10000)
        self.assertTrue(self.player.fullname(), 'Wayne Rooney')

    def test_pay_raise_is_right(self):
        self.player = Player('Wayne', 'Rooney', 100000)
        self.assertEqual(self.player.pay_raise(), 200000)
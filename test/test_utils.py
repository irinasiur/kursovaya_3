import unittest
from utils import utils


class TestUtils(unittest.TestCase):
    def test_get_transactions(self):
         self.assertEqual(len(utils.get_transactions("https://api.npoint.io/e69bd7de520b95dd5bb2")), 2)
         self.assertEqual(len(utils.get_transactions("https://api.npoint.io/620a52b6f558d25ecd3e")), 101)

    def test_get_executed_only(self):
        self.assertEqual(len(utils.get_executed_only("https://api.npoint.io/e69bd7de520b95dd5bb2")), 2)
        self.assertEqual(len(utils.get_executed_only("https://api.npoint.io/620a52b6f558d25ecd3e")), 85)


    def test_sorted_by_datetime(self):
        self.assertEqual(len(utils.sorted_by_datetime("https://api.npoint.io/e69bd7de520b95dd5bb2")), 2)
        self.assertEqual(len(utils.sorted_by_datetime("https://api.npoint.io/620a52b6f558d25ecd3e")), 5)


    def test_account_hide(self):
        self.assertEqual(utils.account_hide("Счет 35383033474447895560"), "**5560")


    def test_card_hide(self):
        self.assertEqual(utils.card_hide("Maestro 1596837868705199"), "Maestro  1596 83** **** 5199")






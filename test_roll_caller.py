from unittest import TestCase
from roll_caller import roll_caller


class Testroll_caller(TestCase):
    def test_config(self):
        roll_caller().config()


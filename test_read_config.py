from unittest import TestCase
from read_config import read_config


class Testread_config(TestCase):
    def test_get_sections(self):
        res = read_config().get_sections()
        print(res)

    def test_get_options(self):
        section = 'oppo'
        res = read_config().get_options(section)
        print(res)

    def test_get_option_of_section(self):
        section = 'db'
        option = 'url'
        res_val = read_config().get_option_of_section(section, option)
        print(res_val)
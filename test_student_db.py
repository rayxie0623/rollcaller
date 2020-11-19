from unittest import TestCase
from student_db import student_db

class Teststudent_db(TestCase):
    def test_connect_mysql(self):
        res = student_db().connect_mysql()
        print(res)

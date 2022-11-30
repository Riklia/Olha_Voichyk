from common import PayGradesTest
import unittest

global test

def test_unit_driver():
    global test
    test = PayGradesTest()


def test_login_page():
    test.login_page()


def test_main_page():
    test.main_page()


def test_pay_grades_page():
    test.pay_grades_page()


def test_check_record():
    test.check_record()


def test_remove_check():
    test.remove_record_check()

if __name__ == '__main__':
    unittest.main()

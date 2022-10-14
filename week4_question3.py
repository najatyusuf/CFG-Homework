from unittest import TestCase, mock
from week4_question2 import pin_code, validate_pin_code, withdraw_cash, balance_enquiry, user_enquiries, user


class test_pin_code(TestCase):
    def test_correct_pin(self):
        result = pin_code()
        expected = 1234
        self.assertEqual(result, expected)

    def test_incorrect_pin(self):
        result = pin_code()
        expected = 1111
        self.assertEqual(result, expected)


class test_withdrawal(TestCase):
    def test_sufficient_withdrawal(self):
        result = withdraw_cash()
        expected = None # enter any amount from 1 to 100 when run
        self.assertEqual(result, expected)

    def test_insufficient_withdrawal(self):
        result = withdraw_cash()
        expected = 110
        self.assertFalse(result, expected)


class TestValidPin(TestCase):
    def test_valid_pin(self):
        with mock.patch('builtins.input', side_effect=['1234']):
            result = pin_code()
            self.assertTrue(result)

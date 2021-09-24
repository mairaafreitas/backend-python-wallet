from decimal import Decimal

from app.services.calculate_cashback import calculate_cashback
import unittest


class TestCalculateCashback(unittest.TestCase):

    def test_zero(self):
        expected = Decimal(0)

        result = calculate_cashback(Decimal(0))

        self.assertEqual(result, expected)
        self.assertIsInstance(result, Decimal)

    def test_integer_result(self):
        expected = Decimal('2')

        result = calculate_cashback(Decimal(20))

        self.assertEqual(result, expected)
        self.assertIsInstance(result, Decimal)

    def test_float_result(self):
        expected = Decimal('2.5')

        result = calculate_cashback(Decimal(25))

        self.assertEqual(result, expected)
        self.assertIsInstance(result, Decimal)

    def test_float_arg_round_ceil(self):
        expected = Decimal('4.08')

        result = calculate_cashback(Decimal(40.75))

        self.assertEqual(result, expected)
        self.assertIsInstance(result, Decimal)

    def test_float_arg_round_floor(self):
        expected = Decimal('4.07')

        result = calculate_cashback(Decimal(40.74))

        self.assertEqual(result, expected)
        self.assertIsInstance(result, Decimal)

if __name__ == '__main__':
    unittest.main()
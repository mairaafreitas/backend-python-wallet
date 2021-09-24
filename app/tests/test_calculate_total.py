import unittest
from app.services.calculate_total import calculate_total


class TestCalculateTotal(unittest.TestCase):
    def test_zero_quantity(self):
        products = [{
            "value": 20,
            "qty": 0
        }]
        expected = 0
        result = calculate_total(products)

        self.assertEqual(result, expected)

    def test_zero_value(self):
        products = [{
            "value": 0,
            "qty": 2
        }]
        expected = 0
        result = calculate_total(products)

        self.assertEqual(result, expected)

    def test_empty_list(self):
        products = []
        expected = 0
        result = calculate_total(products)

        self.assertEqual(result, expected)

    def test_two_products(self):
        products = [
            {
                "value": 50,
                "qty": 1
            },
            {
                "value": 20,
                "qty": 5
            }
        ]

        expected = 150
        result = calculate_total(products)

        self.assertEqual(result, expected)

    def test_float_result(self):
        products = [
            {
                "value": 50.55,
                "qty": 1
            },
            {
                "value": 20.98,
                "qty": 5
            }
        ]

        expected = 155.45
        result = calculate_total(products)

        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()

from unittest import TestCase, main
from unit_testing import calculator


class CalculatorTest(TestCase):
    def test_plus(self):
        self.assertEqual(calculator('2+2'), 4)

    def test_minus(self):
        self.assertEqual(calculator('5-3'),2)

    def test_divide(self):
        self.assertEqual(calculator('6/3'),2)

    def test_multiply(self):
        self.assertEqual(calculator('4*5'),20)

    def test_no_operator(self):
        with self.assertRaises(ValueError) as e:
            calculator('sdfdfds')
        self.assertEqual('Expression must contain atleast one of those +-/*', e.exception.args[0])

    def test_two_operator(self):
        with self.assertRaises(ValueError) as e:
            calculator('2+2+2')
        self.assertEqual('Expression must contain two integers and one operator', e.exception.args[0])


if __name__ == '__main__':
    main()

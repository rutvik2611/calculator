import unittest
import csv
from calculator import calculator

class MyTestCase(unittest.TestCase):


    def setUp(self) -> None:
        self.calculator = calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, calculator)

    def test_addition(self):
        self.calculator.__add__(14, 1)
        self.assertEqual(self.calculator.result, 15)

    def test_subtraction(self):
        self.calculator.__sub__(5, 5)
        self.assertEqual(self.calculator.result, 0)

    def test_multiplication(self):
        self.calculator.__mul__(5, 5)
        self.assertEqual(self.calculator.result, 25)

    def test_division(self):
        self.calculator.__div__(5, 5)
        self.assertEqual(self.calculator.result, 1)

    def test_square(self):
        self.calculator.__square__(5)
        self.assertEqual(self.calculator.result, 25)

    def test_squareRoot(self):
        self.calculator.__squareRoot__(25)
        self.assertEqual(self.calculator.result, 5)


    def test_results_property(self):

        self.assertEqual(self.calculator.result, 0)


    def test_read_any_csv(self):

        self.assertEqual(0, 0)








if __name__ == '__main__':
    unittest.main()


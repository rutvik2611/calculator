import unittest
from calculator import calculator


class MyTestCase(unittest.TestCase):


    def setUp(self) -> None:
        self.calculator = calculator()


    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, calculator)

    def test_add_from_csv(self):

        y = self.calculator.read_csv("../src/CSV/uadd.csv")

        for var in range(len(y)):
            self.calculator.__add__(y[0][var], y[1][var])
            self.assertEqual(self.calculator.result, y[2][var])


    def test_subtraction(self):
        y = self.calculator.read_csv("../src/CSV/Unit Test Subtraction.csv")

        for var in range(len(y)):
            self.calculator.__sub__(y[0][var], y[1][var])
            self.assertEqual(self.calculator.result, y[2][var]*-1)


    def test_multiplication(self):

        y = self.calculator.read_csv("../src/CSV/Unit Test Multiplication.csv")

        for var in range(len(y)):
            self.calculator.__mul__(y[0][var], y[1][var])
            self.assertEqual(self.calculator.result, y[2][var])



    def test_division(self):
        y = self.calculator.read_csv("../src/CSV/Unit Test Division.csv")

        for var in range(len(y)):
            self.calculator.__div__(y[1][var], y[0][var])
            self.assertEqual(int(self.calculator.result),int(y[2][var]))

    def test_square(self):

        y = self.calculator.read_csv("../src/CSV/Unit Test Square.csv")

        for var in range(len(y)):
            self.calculator.__square__(y[0][var])
            self.assertEqual(self.calculator.result,y[1][var])


    def test_squareRoot(self):
        y = self.calculator.read_csv("../src/CSV/Unit Test Square Root.csv")

        for var in range(len(y)):
            self.calculator.__squareRoot__(y[0][var])
            self.assertEqual(int(self.calculator.result), int(y[1][var]))




    def test_results_property(self):

        self.assertEqual(self.calculator.result, 0)




if __name__ == '__main__':
    unittest.main()





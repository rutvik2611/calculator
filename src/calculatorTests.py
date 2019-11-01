import unittest
from calculator import calculator


class MyTestCase(unittest.TestCase):


    def setUp(self) -> None:
        self.calculator = calculator()


    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, calculator)

    def test_add_from_csv(self):

        y = self.calculator.read_csv("../src/CSV/uadd.csv")
        a = y[0]
        b = y[1]
        c = y[2]
        for var in range(len(a)):
            self.calculator.__add__(a[var], b[var])
            self.assertEqual(self.calculator.result, c[var])


    def test_subtraction(self):
        y = self.calculator.read_csv("../src/CSV/Unit Test Subtraction.csv")
        a = y[0]
        b = y[1]
        c = y[2]
        for var in range(len(a)):
            self.calculator.__sub__(a[var], b[var])
            self.assertEqual(self.calculator.result, c[var]*-1)


    def test_multiplication(self):

        y = self.calculator.read_csv("../src/CSV/Unit Test Multiplication.csv")
        a = y[0]
        b = y[1]
        c = y[2]
        for var in range(len(a)):
            self.calculator.__mul__(a[var], b[var])
            self.assertEqual(self.calculator.result, c[var])



    def test_division(self):
        y = self.calculator.read_csv("../src/CSV/Unit Test Division.csv")
        a = y[0]
        b = y[1]
        c = y[2]
        for var in range(len(a)):
            self.calculator.__div__(b[var],a[var])
            self.assertEqual(int(self.calculator.result),int(c[var]))

    def test_square(self):

        y = self.calculator.read_csv("../src/CSV/Unit Test Square.csv")
        a = y[0]
        b = y[1]

        for var in range(len(a)):
            self.calculator.__square__(a[var])
            self.assertEqual(self.calculator.result,b[var])


    def test_squareRoot(self):
        y = self.calculator.read_csv("../src/CSV/Unit Test Square Root.csv")
        a = y[0]
        b = y[1]

        for var in range(len(a)):
            self.calculator.__squareRoot__(a[var])
            self.assertEqual(int(self.calculator.result), int(b[var]))




    def test_results_property(self):

        self.assertEqual(self.calculator.result, 0)




if __name__ == '__main__':
    unittest.main()





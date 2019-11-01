import unittest
from calculator import calculator


class MyTestCase(unittest.TestCase):


    def setUp(self) -> None:
        self.calculator = calculator()


    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, calculator)

    def test_add_from_csv(self):
        x = self.calculator.read_csv("../src/CSV/uadd.csv")

        a = []
        b = []
        c = []
        for var in range(len(x)):
            a.append(x[var][0])
            b.append(x[var][1])
            c.append(x[var][2])
            self.calculator.__add__(a[var], b[var])
            self.assertEqual(self.calculator.result, c[var])


    def test_subtraction(self):
        x = self.calculator.read_csv("../src/CSV/Unit Test Subtraction.csv")

        a = []
        b = []
        c = []
        for var in range(len(x)):
            a.append(x[var][0])
            b.append(x[var][1])
            c.append(x[var][2])
            self.calculator.__sub__(a[var], b[var])
            self.assertEqual(self.calculator.result, c[var]*-1)


    def test_multiplication(self):

            x = self.calculator.read_csv("../src/CSV/Unit Test Multiplication.csv")

            a = []
            b = []
            c = []
            for var in range(len(x)):
                a.append(x[var][0])
                b.append(x[var][1])
                c.append(x[var][2])
                self.calculator.__mul__(a[var], b[var])
                self.assertEqual(self.calculator.result, c[var])



    def test_division(self):
        x = self.calculator.read_csv("../src/CSV/Unit Test Division.csv")

        a = []
        b = []
        c = []
        for var in range(len(x)):
            a.append(int(x[var][0]))
            b.append(int(x[var][1]))
            c.append(int(x[var][2]))
            self.calculator.__div__(b[var],a[var])
            self.assertEqual(int(self.calculator.result), c[var])

    def test_square(self):

        x = self.calculator.read_csv("../src/CSV/Unit Test Square.csv")

        a = []
        b = []

        for var in range(len(x)):
            a.append(int(x[var][0]))
            b.append(int(x[var][1]))

            self.calculator.__square__(a[var])
            self.assertEqual(int(self.calculator.result), b[var])


    def test_squareRoot(self):
        x = self.calculator.read_csv("../src/CSV/Unit Test Square Root.csv")

        a = []
        b = []

        for var in range(len(x)):
            a.append(int(x[var][0]))
            b.append(int(x[var][1]))

            self.calculator.__squareRoot__(a[var])
            self.assertEqual(int(self.calculator.result), b[var])




    def test_results_property(self):

        self.assertEqual(self.calculator.result, 0)




if __name__ == '__main__':
    unittest.main()



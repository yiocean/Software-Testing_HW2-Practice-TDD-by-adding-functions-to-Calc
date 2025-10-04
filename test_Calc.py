import unittest
from Calc import Calculator  # The class we are going to implement

class TestCalculator(unittest.TestCase):
    def test_add(self):
        calc = Calculator()
        result = calc.add(2, 3)
        self.assertEqual(result, 5)

    def test_add_floats(self):
        calc = Calculator()
        reslut = calc.add(2.5, 3.1)
        self.assertAlmostEqual(reslut, 5.6, places=7)

    def test_add_with_zero(self):
        calc = Calculator()
        result = calc.add(0, 5)
        self.assertEqual(result, 5)

    def test_subtract(self):
        calc = Calculator()
        result = calc.subtract(5, 3)
        self.assertEqual(result, 2)

    def test_subtract_floats(self):
        calc = Calculator()
        result = calc.subtract(5.5, 2.2)
        self.assertAlmostEqual(result, 3.3, places=7)

    def test_subtract_with_zero(self):
        calc = Calculator()
        result = calc.subtract(0, 3)
        self.assertEqual(result, -3)

    def test_multiply(self):
        calc = Calculator()
        result = calc.multiply(4, 3)
        self.assertEqual(result, 12)

    def test_multiply_floats(self):
        calc = Calculator()
        result = calc.multiply(2.5, 4.0)
        self.assertAlmostEqual(result, 10.0, places=7)

    def test_multiply_with_zero(self):
        calc = Calculator()
        result = calc.multiply(0, 5)
        self.assertEqual(result, 0)

    def test_divide(self):
        calc = Calculator()
        result = calc.divide(10, 2)
        self.assertEqual(result, 5)

    def test_divide_floats(self):
        calc = Calculator()
        result = calc.divide(5.5, 2.0)
        self.assertAlmostEqual(result, 2.75, places=7)

    def test_divide_with_zero(self):
        calc = Calculator()
        result = calc.divide(0, 5)
        with self.assertRaises(ZeroDivisionError):
            calc.divide(5, 0)
        self.assertEqual(result, 0)

if __name__ == "__main__": # pragma: no cover
    unittest.main()
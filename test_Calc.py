import unittest
from Calc import Calculator


class TestCalculator(unittest.TestCase):
    """Unit tests for Calculator class using Test-Driven Development (TDD)."""

    def setUp(self):
        """Set up a Calculator instance before each test."""
        self.calc = Calculator()

    # --- Addition Tests ---
    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_add_floats(self):
        self.assertAlmostEqual(self.calc.add(2.5, 3.1), 5.6, places=7)

    def test_add_with_zero(self):
        self.assertEqual(self.calc.add(0, 5), 5)

    # --- Subtraction Tests ---
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)

    def test_subtract_floats(self):
        self.assertAlmostEqual(self.calc.subtract(5.5, 2.2), 3.3, places=7)

    def test_subtract_with_zero(self):
        self.assertEqual(self.calc.subtract(0, 3), -3)

    # --- Multiplication Tests ---
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(4, 3), 12)

    def test_multiply_floats(self):
        self.assertAlmostEqual(self.calc.multiply(2.5, 4.0), 10.0, places=7)

    def test_multiply_with_zero(self):
        self.assertEqual(self.calc.multiply(0, 5), 0)

    # --- Division Tests ---
    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)

    def test_divide_floats(self):
        self.assertAlmostEqual(self.calc.divide(5.5, 2.0), 2.75, places=7)

    def test_divide_with_zero(self):
        self.assertEqual(self.calc.divide(0, 5), 0)

    def test_divide_by_zero_raises(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(5, 0)

    def test_fail_case():
        assert False


if __name__ == "__main__":  # pragma: no cover
    unittest.main()

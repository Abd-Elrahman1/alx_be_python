import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
  def setUp(self):
        """Create an instance of SimpleCalculator before each test."""
        self.calculator = SimpleCalculator()

    # Test for addition
  def test_add(self):
        self.assertEqual(self.calculator.add(5, 3), 8)
        self.assertEqual(self.calculator.add(-5, -3), -8)
        self.assertEqual(self.calculator.add(-5, 3), -2)
        self.assertEqual(self.calculator.add(0, 0), 0)

    # Test for subtraction
  def test_subtract(self):
        self.assertEqual(self.calculator.subtract(10, 5), 5)
        self.assertEqual(self.calculator.subtract(-10, -5), -5)
        self.assertEqual(self.calculator.subtract(0, 5), -5)
        self.assertEqual(self.calculator.subtract(5, 0), 5)

    # Test for multiplication
  def test_multiply(self):
        self.assertEqual(self.calculator.multiply(4, 5), 20)
        self.assertEqual(self.calculator.multiply(-4, 5), -20)
        self.assertEqual(self.calculator.multiply(0, 5), 0)
        self.assertEqual(self.calculator.multiply(-4, -5), 20)

    # Test for division
  def test_divide(self):
        self.assertEqual(self.calculator.divide(10, 2), 5)
        self.assertEqual(self.calculator.divide(-10, 2), -5)
        self.assertEqual(self.calculator.divide(-10, -2), 5)
        self.assertIsNone(self.calculator.divide(10, 0))  # Division by zero

# Running tests directly if this file is executed
if __name__ == '__main__':
    unittest.main()
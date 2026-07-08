import unittest
from greetings import calculate_pi


class TestPiCalculation(unittest.TestCase):
    """Test cases for the calculate_pi function"""
    
    def test_pi_value(self):
        """Test if calculated Pi is close to the actual value"""
        result = calculate_pi()
        expected = 3.14159  # Pi to 5 decimal places
        self.assertEqual(result, expected)
    
    def test_pi_return_type(self):
        """Test if the function returns a float"""
        result = calculate_pi()
        self.assertIsInstance(result, float)
    
    def test_pi_range(self):
        """Test if Pi is within expected range"""
        result = calculate_pi()
        self.assertGreater(result, 3.14)
        self.assertLess(result, 3.15)
    
    def test_pi_precision(self):
        """Test if Pi has correct number of decimal places"""
        result = calculate_pi()
        # Convert to string and check decimal places
        result_str = str(result)
        if '.' in result_str:
            decimal_places = len(result_str.split('.')[1])
            self.assertLessEqual(decimal_places, 5)


if __name__ == '__main__':
    # Run the tests
    print("Testing Pi calculation function...")
    print(f"Calculated Pi value: {calculate_pi()}")
    print("\nRunning unit tests:\n")
    unittest.main()

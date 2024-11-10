import unittest
from math_quiz import random_int, random_operation, calculate


class TestMathGame(unittest.TestCase):

    def test_random_int(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = random_int(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_random_operation(self):
        valid_operations = ['+', '-', '*']
        for _ in range(100):  # Run multiple checks for randomness
            operation = random_operation()
            self.assertIn(operation, valid_operations)

    def test_calculate(self):
        test_cases = [
            (5, 2, '+', '5 + 2', 7),  # addition case
            (10, 3, '-', '10 - 3', 7),  # subtraction case
            (4, 3, '*', '4 * 3', 12),  # multiplication case
            (0, 5, '+', '0 + 5', 5),  # addition with zero
            (-3, 3, '*', '-3 * 3', -9)  # multiplication with negative number
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = calculate(num1, num2, operator)
            self.assertEqual(problem, expected_problem)
            self.assertEqual(answer, expected_answer)


if __name__ == "__main__":
    unittest.main()

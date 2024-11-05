import unittest


def calculate_average(numbers):
    if not numbers:
        return None
    return sum(numbers) / len(numbers)


# Enter your solution here

class TestCalculateAverage(unittest.TestCase):
    def test_calculate_average_valid_input(self):
        self.assertEqual(calculate_average([]), None, 'test 1')
        self.assertEqual(calculate_average([2.5, 3.5, 4.5]), 3.5, 'test 2')
        self.assertEqual(calculate_average([0.5,1.5]), 1, 'test 3')

    def test_calculate_average_empty_input(self):
        self.assertEqual(calculate_average([]), None, 'test 1')

    def test_calculate_average_invalid_input(self):
        self.assertRaises(TypeError, calculate_average, ['a', 3])
        self.assertRaises(TypeError, calculate_average, [1, 2, '2'])
        self.assertRaises(TypeError, calculate_average, [None, None])
if __name__ == '__main__':
    unittest.main()


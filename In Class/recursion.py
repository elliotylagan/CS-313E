import unittest
# pre-condition:  power >= 0
# Implement the ** operator recursively.
def raise_to_power(base, power):
    assert power >= 0
    if power == 0:
        return 1
    return raise_to_power(base, power-1)

# pre-condition: all initial calls will start at index 0
# pre-condition: values is a list
# Implement the max function recursively.
def recursive_max(values, index):
    max = values[0]
    if index == len(values) - 1:
        return values[index]
    
    if values[index] > values[index + 1]:
        max =  values[index]

    recursive_max(values, index + 1)
    return max


# pre-condition: values is a list of ints
# pre-condition: left will initially be 0, and right will be len(values) - 1
# pre-condition: target is an int
# Implement binary search recursively.
def binary_search(values, left, right, target):
    pass

class TestRecursiveFunctions(unittest.TestCase):
    def test_raise_to_power_1(self):
        self.assertEqual(raise_to_power(3, 3), 27)

    def test_raise_to_power_2(self):
        self.assertEqual(raise_to_power(2, 5), 32)

    def test_raise_to_power_3(self):
        self.assertEqual(raise_to_power(5, 0), 1)

    def test_recursive_max_1(self):
        self.assertEqual(recursive_max([1, 5, 8, 7, 2, 6, 10, 0], 0), 10)

    def test_recursive_max_2(self):
        self.assertEqual(recursive_max([10, 5, 8, 7, 2, 6, 1, 0], 0), 10)

    def test_recursive_max_3(self):
        self.assertEqual(recursive_max([1], 0), 1)

    def test_binary_search_1(self):
        self.assertEqual(binary_search([1, 3, 5, 7, 9, 11, 13, 15, 17], 0, 8, 3), 1)

    def test_binary_search_2(self):
        self.assertEqual(binary_search([1, 3, 5, 7, 9, 11, 13, 15, 17], 0, 8, 10), -1)
        
    def test_binary_search_3(self):
        self.assertEqual(binary_search([1, 3, 5, 7, 9, 11, 13, 15, 17], 0, 8, 17), 8)

if __name__ == '__main__':
    unittest.main()
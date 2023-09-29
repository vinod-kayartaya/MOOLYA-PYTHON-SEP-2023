from mathfunctions import factorial
import unittest


class TestFactorial(unittest.TestCase):

    def test_should_get_factorial_of_positive_number(self):
        actual = factorial(5)
        expected = 120
        self.assertEqual(actual, expected)

    def test_should_get_factorial_of_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_should_get_factorial_negative_number(self):
        self.assertEqual(1, factorial(-12))

    def test_should_get_TypeError_for_non_int_input(self):
        try:
            factorial('asd')
            self.fail('Expected an error of type TypeError, but did not get one!')
        except TypeError:
            pass

    def test_should_raise_TypeError_for_non_int_input(self):
        def fn():
            factorial('asd')

        self.assertRaises(TypeError, fn)


if __name__ == '__main__':
    unittest.main()

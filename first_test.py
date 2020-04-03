import unittest  # import unittest


def two_sum(a, b):
    return a+b


def mult_nums(a, b):
    return a*b

# create a class that will hold all of our tests


class MainTest(unittest.TestCase):
    # now we create individual test as methods within this class and the system knowc to run any
    # method whose name begins with 'test '

    def test_hello(self):
        print("hello from test_hello")

    def test_sumtwo(self):
        returned_value = two_sum(5, 7)
        self.assertEqual(returned_value, 12)
        self.assertEqual(two_sum(-5, 5), 0)

    def test_product(self):
        returned_value = mult_nums(9, 9)
        self.assertEqual(returned_value, 81)
        self.assertEqual(mult_nums(2, 2), 4)


if __name__ == "__main__":
    unittest.main()

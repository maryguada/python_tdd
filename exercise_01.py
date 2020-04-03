import unittest  # import unittest


def min(l):
    # should return
    min = l[0]
    for val in l:
        if val < min:
            min = val
    return min


def sum_list(l):
    # shoul return total value of all list in items
    total = 0
    for val in l:
        total += val
    return total


def less_than(a):
    # should return a bool of whether the value is less than 100
    if a < 100:
        return True
    else:
        return False


class MainTest(unittest.TestCase):
    def test_hello(self):
        print("hello from Example number 1!")

    def test_min(self):
        returned_value = min([0, 1, 2])
        self.assertEqual(returned_value, 0)

    def test_sum(self):
        returned_value = sum_list([2, 3, 3, 4])
        self.assertEqual(returned_value, 12)

    def test_lessthan(self):
        returned_value = less_than(99)
        self.assertTrue(returned_value)


if __name__ == "__main__":
    unittest.main()

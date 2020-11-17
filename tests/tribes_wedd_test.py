import unittest

from manager import tribes_evaluator as ev


class WeddTestCase(unittest.TestCase):
    def test1(self):
        pairs = [[1, 2], [2, 4], [3, 5]]
        self.assertEqual(len(ev.form_tribes(pairs)),2)

    def test2(self):
        pairs = [[1, 2], [2, 4], [1, 3], [3, 5], [8, 10]]
        self.assertEqual(len(ev.form_tribes(pairs)),2)

    def test3(self):
        pairs = [[1, 2], [2, 4], [1, 3], [3, 5], [8, 10]]
        self.assertEqual(ev.form_tribes(pairs), [[1, 2, 4, 3, 5], [8, 10]])

    def test_one_pair(self):
        pairs = [[1, 2]]
        self.assertEqual(len(ev.form_tribes(pairs)), 1)

    def test_empty(self):
        pairs = []
        self.assertEqual(len(ev.form_tribes(pairs)), 0)

    def test_only_boys(self):
        pairs = [[1, 3], [5, 7], [9, 11]]
        tribes=ev.form_tribes(pairs)
        self.assertEqual(ev.calculate_result(tribes), 0)

    def test_only_girls(self):
        pairs = [[2, 4], [6, 8], [8, 12],[12,16],[14,18]]
        tribes = ev.form_tribes(pairs)
        self.assertEqual(ev.calculate_result(tribes), 0)

    def test_zero_value_in_pair(self):
        pairs = [[0, 4], [4, 8]]
        self.assertFalse(pairs[0] in ev.form_tribes(pairs))

if __name__ == '__main__':
    unittest.main()
# vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4:



import unittest
from karmia.utility import KarmiaUtilityArray


class TestKarmiaUtilityArrayUnique(unittest.TestCase):
    def test_unique(self):
        utility = KarmiaUtilityArray()
        items = ['a', 'b', 'b', 'c', 'c', 'c', 'd', 'd', 'd', 'd', 'e', 'e', 'e', 'e', 'e']
        result = utility.unique(items)

        self.assertEqual(len(result), 5)
        self.assertListEqual(result, ['a', 'b', 'c', 'd', 'e'])

class TestKarmiaUtilityArrayCount(unittest.TestCase):
    def test_count(self):
        utility = KarmiaUtilityArray()
        items = ['a', 'b', 'b', 'c', 'c', 'c', 'd', 'd', 'd', 'd', 'e', 'e', 'e', 'e', 'e']

        self.assertEqual(utility.count(items, 'a'), 1)
        self.assertEqual(utility.count(items, 'b'), 2)
        self.assertEqual(utility.count(items, 'c'), 3)
        self.assertEqual(utility.count(items, 'd'), 4)
        self.assertEqual(utility.count(items, 'e'), 5)
        self.assertEqual(utility.count(items, 'f'), 0)

class TestKarmiaUtilityArrayRange(unittest.TestCase):
    def test_range(self):
        utility = KarmiaUtilityArray()
        values = list(utility.range(10))
        for i in range(10):
            self.assertEqual(values[i], i)

    def test_start_end(self):
        utility = KarmiaUtilityArray()
        values = list(utility.range(10, 20))
        for i in range(10):
            self.assertEqual(values[i], i + 10)

    def test_start_end_step(self):
        utility = KarmiaUtilityArray()
        values = list(utility.range(10, 20, 3))
        for i in range(0, 10, 3):
            self.assertEqual(values[int(i / 3)], i + 10)


class TestKarmiaUtilityArrayFlip(unittest.TestCase):
    def test_flip(self):
        utility = KarmiaUtilityArray()
        dictionary = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4}
        result = utility.flip(list(dictionary.keys()))

        self.assertEqual(isinstance(result, dict), True)
        self.assertDictEqual(result, dictionary)

class TestKarmiaUtilityArrayIntersection(unittest.TestCase):
    def test_intersection(self):
        utility = KarmiaUtilityArray()
        values1 = ["a", "b", "b", "c", "c", "c", "d", "d", "d", "d", "e", "e", "e", "e", "e"]
        values2 = ["a", "b", "c"]
        result = utility.intersection(values1, values2)

        self.assertEqual(len(result), 3)
        self.assertListEqual(result, values2)

class TestKarmiaUtilityArrayDifference(unittest.TestCase):
    def test_intersection(self):
        utility = KarmiaUtilityArray()
        values1 = ["a", "b", "b", "c", "c", "c", "d", "d", "d", "d", "e", "e", "e", "e", "e"]
        values2 = ["a", "b", "c"]
        result = utility.difference(values1, values2)

        self.assertEqual(len(result), 9)
        self.assertEqual(utility.count(result, "d"), 4)
        self.assertEqual(utility.count(result, "e"), 5)




# Local variables:
# tab-width: 4
# c-basic-offset: 4
# c-hanging-comment-ender-p: nil
# End:

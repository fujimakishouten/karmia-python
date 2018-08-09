# vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4:



import unittest
from karmia.utility import KarmiaUtilityRandom


class TestKarmiaUtilityRandomString(unittest.TestCase):
    def test_random_string(self):
        utility = KarmiaUtilityRandom()


class TestKarmiaUtilityRandomInteger(unittest.TestCase):
    def test_no_parameters(self):
        utility = KarmiaUtilityRandom()
        result = utility.integer()
        self.assertIsInstance(result, int)
        self.assertGreaterEqual(result, 0)



# Local variables:
# tab-width: 4
# c-basic-offset: 4
# c-hanging-comment-ender-p: nil
# End:

# vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4:



import unittest
from karmia import KarmiaContext


class TestKarmiaContextSet(unittest.TestCase):
    def test_parameter(self):
        context = KarmiaContext()
        key = 'key'
        value = 'value'

        context.set(key, value)

        self.assertEqual(context.parameters[key], value)


    def test_object(self):
        context = KarmiaContext()
        parameter = {'key': 'value'}

        context.set(parameter)

        self.assertEqual(context.parameters['key'], parameter['key'])

    def test_merge(self):
        context = KarmiaContext()
        parameter1 = {'key1': 'value1'}
        parameter2 = {'key2': 'value2'}

        context.set(parameter1)
        context.set(parameter2)

        self.assertEqual(context.parameters['key1'], parameter1['key1'])
        self.assertEqual(context.parameters['key2'], parameter2['key2'])


class TestKarmiaContextGet(unittest.TestCase):
    def test_parameter(self):
        context = KarmiaContext()
        key = 'key'
        value = 'value'

        context.set(key, value)

        self.assertEqual(context.get(key), value)

    def test_default_parameter(self):
        context = KarmiaContext()
        key = 'key'
        default_value = 'default_value'

        self.assertEqual(context.get(key, default_value), default_value)

class TestKarmiaContextRemove(unittest.TestCase):
    def test_remove(self):
        context = KarmiaContext()
        key = 'key'
        value = 'value'

        context.set(key, value)
        self.assertEqual(context.get(key), value)

        context.remove(key)
        self.assertEqual(context.get(key), None)

class TestKarmiaContextChild(unittest.TestCase):
    def test_extend(self):
        context = KarmiaContext()
        key1 = 'key1'
        key2 = 'key2'
        values1 = {'value1': 1}
        values2 = {'value2': 2}
        context.set(key1, values1)

        child = context.child()
        self.assertEqual(child.get(key1), values1)

        child.set(key2, values2)
        self.assertEqual(child.get(key1), values1)
        self.assertEqual(child.get(key2), values2)
        self.assertEqual(context.get(key1), values1)
        self.assertEqual(context.get(key2), None)


# Local variables:
# tab-width: 4
# c-basic-offset: 4
# c-hanging-comment-ender-p: nil
# End:

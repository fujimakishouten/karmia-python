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

class TestAnnotate(unittest.TestCase):
    def test_annotate_function(self):
        context = KarmiaContext()
        fn = lambda value1, value2: value1 + value2

        self.assertEqual(list(context.annotate(fn).keys()), ['value1', 'value2'])

    def test_no_arguments(self):
        context = KarmiaContext()
        fn = lambda: 'result'

        self.assertEqual(list(context.annotate(fn).keys()), [])

class TestInvoke(unittest.TestCase):
    def test_invoke(self):
        context = KarmiaContext()
        fn = lambda value1, value2: value1 + value2
        parameters = {'value1': 1, 'value2': 2}

        self.assertEqual(context.invoke(fn, parameters), parameters['value1'] + parameters['value2'])

class TestCall(unittest.TestCase):
    def test_return(self):
        context = KarmiaContext()
        fn = lambda value1, value2: value1 + value2
        parameters = {'value1': 1, 'value2': 2}

        self.assertEqual(context.call(fn, parameters), parameters['value1'] + parameters['value2'])

    def callback(self):
        def fn(value1, value2, callback):
            callback(None, value1 + value2)

        def callback(error, result):
            self.assertIsNone(error)
            self.assertEqual(result, parameters['value1', 'value2'])

        context = KarmiaContext()
        parameters = {'value1': 1, 'value2': 2}
        context.call(fn, parameters, callback)

    def test_no_parameters(self):
        context = KarmiaContext()
        result = 'result'
        fn = lambda: result

        self.assertEqual(context.call(fn), result)

    def test_merge_parameters(self):
        context = KarmiaContext()
        key = 'value1'
        value = 1
        parameters = {'value2': 2}
        fn = lambda value1, value2: value1 + value2

        context.set(key, value)

        self.assertEqual(context.call(fn, parameters), value + parameters['value2'])

class TestAsync(unittest.TestCase):
    def callback(self):
        def fn(value1, value2, callback):
            return callback(None, value1 + value2)

        def callback(error, result):
            self.assertIsNone(error)
            self.assertEqual(result, parameters['value1', 'value2'])

        context = KarmiaContext()
        parameters = {'value1': 1, 'value2': 2}
        async = context.async(fn, parameters)

        self.assertTrue(callable(async))
        async(callback)



# Local variables:
# tab-width: 4
# c-basic-offset: 4
# c-hanging-comment-ender-p: nil
# End:

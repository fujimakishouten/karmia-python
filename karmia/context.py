# vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4:



import inspect


class KarmiaContext:
    def __init__(self, options = None):
        options = options if options else {}
        callback = options.get('callback', ['callback'])
        self.callback = callback if isinstance(callback, list) else [callback]
        self.parameters = {}


    def set(self, key, value=None):
        parameters = {}

        if isinstance(key, dict):
            parameters = key
        else:
            parameters[key] = value

        self.parameters.update(parameters)

        return self


    def get(self, key, default_value=None):
        return self.parameters.get(key, default_value)


    def remove(self, key):
        if key in self.parameters:
            self.parameters.pop(key)

        return self


    def child(self):
        child = KarmiaContext()
        child.parameters = self.parameters.copy()

        return child


    def annotate(self, fn):
        return inspect.signature(fn).parameters


    def invoke(self, fn, parameters=None):
        parameters = parameters if parameters else {}
        parameters['context'] = parameters.get('context', self)
        values = map(lambda key: parameters.get(key, None), self.annotate(fn))

        return fn(*values)


    def call(self, fn, parameters=None, callback=None):
        parameters = parameters if parameters else {}
        if callable(parameters):
            callback = parameters
            parameters = {}

        values = {}
        values.update(self.parameters)
        values.update(parameters)
        if callback:
            values.update({key: callback for key in self.callback})

        return self.invoke(fn, values)

    def async(self, fn, parameters=None):
        return lambda callback: self.call(fn, parameters, callback)



# Local variables:
# tab-width: 4
# c-basic-offset: 4
# c-hanging-comment-ender-p: nil
# End:

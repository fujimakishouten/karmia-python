# karmia-python
Karmia modules for Python

## Version
0.1.0

## Example

```Python
import Karmia

context = Karmia.KarmiaContext()
```

### Set parameter

```Python
context.set('key', 'value')
```

### Get parameter

```Python
context.get('key', 'default_value')
```

### Remove parameter

```Python
context.remove('key')
```

### Create child context
```Python
child = context.child()
```

### Call function

#### With parameters
```Python
def fn(value1, value2):
    return value1 + value2

parameters = {'value1': 1, 'value2': 2}
context.call(fn, parameters)
```

#### With context parameters

```Python
def fn(value1, value2):
    return value1 + value2

context.set('value1', 1)
context.set('value2', 2)

context.call(fn)
```


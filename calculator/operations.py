from functools import reduce

def add(*args):
    return reduce(lambda x, y: x + y, args)

def subtract(*args):
    return reduce(lambda x, y: x - y, args)

def multiply(*args):
    return reduce(lambda x, y: float(x) * y, args)

def divide(*args):
    return reduce(lambda x, y: float(x) / y, args)

# add your custom operations here

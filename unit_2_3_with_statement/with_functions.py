from contextlib import contextmanager

# generator based implementation
# decorating this function with this, makes this to be used in 'with' statement.
@contextmanager
def managed_file(name):
    try:
        f = open(name, 'w') # acquire resource
        yield f # yields resource
    finally:
        f.close() # release resource

with managed_file('with_functions.txt') as f:
    f.write('hello, world!')
    f.write('bye now')
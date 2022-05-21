# PythonTricks
This repo contains python practice programs that I worked out while studying 'Python Tricks' book by 'Dan Bader'.

## Unit 2.1 - Assertions
* `assert` statements are great way to self-check if our program is working as expected.
* Each `assert` checks if an impossible condition happens.
* `assert` statements **are not** a mechanism for handling **run-time errors**.
* All `assert` statements can globally disabled by interpreter settings.
    * `python -O program.py` gets rid of all assertions in our program.
    * So `assert` statements are not meant for handling **run-time errors** as mentioned above.

### Example(s)
* `assert 10 == 9` - raises AssertionError
* `assert (10 == 9)` - does not raise AssertionError since first is evaluated as tuple and always returns `True` since it is non-empty.
* `assert 10 == 9, '10 is Not Equal to 9'` raises AssertionError with specified message

## Unit 2.2 - Comma Placement in list, set or dict
* **Span the list across multiple lines** which will help us later **to track which element added/removed/modified later using diff tools**.
* It also helps the code reviewers to easily find the changes.
* **Always add ',' to the end of every element including last element** so that comma is not missed whenever a new element is added which will prevent from *string literal concatentation* problem (actually a feature).

### Example(s)
```python
names = [
   'John',
   'David',
   'Peter',
]
```

## Unit 2.3 - Context Managers and the with Statement
* `with` statement makes code that deals with system resources more readable.
* It ensures that open file descriptors (or any system resource) are closed automatically after program execution leaves the ***context*** of `with` statement.

### Examples(s)
```python
f = open('hello.txt', 'w')
f.write('hello, world')
f.close()

# above can be replaced with below code which
# guarantees that the file is closed even if there's
# an exception during f.write(). More Verbose.
f = open('hello.txt', 'w')
try:
    f.write('hello, world')
finally:
    f.close()

# same as above but less verbose
with open('hello.txt', 'w') as f:
    f.write('hello, world!')
```

* ***How to provide the same functionality to our own classes and functions? Implementing Context-Managers***

* ***What is context manager? Protocol (or interface) that our object or function needs to follow in order to support `with` statement.***

### Example(s)
```python
# Using Decorators
from contextlib import contextmanager

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

# By Implementing the interface of context-manager in class
class ManagedFile:
    def __init__(self, name):
        self.name = name
    
    # Acquires the resource when execution enters context.
    def __enter__(self):
        self.file = open(self.name, 'w')
        return self.file
    
    # Free up resource when execution leaves context.
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

with ManagedFile('with_object_hello.txt') as f:
    f.write('hello, world!')
    f.write('bye now')
```

* Indenter exercise and timer exercise are available in indent_exercise.py and timer_exercise.py files respectivly under unit_2_3_with_statement directory.

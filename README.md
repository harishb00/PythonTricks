# PythonTricks
This repo contains python practice programs that I worked out while studying 'Python Tricks' book by 'Dan Bader'.

## Chapter 1 - Assertions
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
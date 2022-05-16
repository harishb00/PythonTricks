names = ['Alice', 'Bob', 'Dilbert']
print(names)

# Spreading the list, dict or set across
# multiple lines helps for code review changes.
# 'diff' commands of many source control systems
# find it hard to shows changes over a single line.

names = [
    'Alice',
    'Bob',
    'Dilbert' # now adding/removing/modifying an element can easily be found in diff tools
]
print(names)

# When we spread out the list across multiple lines,
# we may miss comma before adding a new element
# that leads to unintended outputs.
names = [
    'Alice',
    'Bob',
    'Dilbert' # No Comma!
    'Jane'
]
print(names) # ['Alice', 'Bob', 'DilbertJane'] - string literal concatenation

print('Dilbert''Jane') # Same as concatenation (provided by Python)

# Split string constant across lines without using backslashes
my_str = ('This is a super long string constant '
          'spread out across multiple lines. '
          'And look, no backslash characters needed!')
print(my_str)

# Good Code Style -> place comma after every item
# in the list, dict, or set including last item.
names = [
    'Alice',
    'Bob',
    'Dilbert',
]
print(names)
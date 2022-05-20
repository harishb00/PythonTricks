# My Solution for class Indenter
class Indenter:
    def __init__(self, num_tab_space=0):
        self.num_tab_space = num_tab_space
    
    def __enter__(self):
        self.num_tab_space = self.num_tab_space + 1
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.num_tab_space = self.num_tab_space - 1

    def print(self, text):
        tab_space = '\t' * (self.num_tab_space-1)
        print(f'{tab_space}{text}')

# Python Tricks Book Solution
'''
class Indenter:
    def __init__(self):
        self.level = 0
    
    def __enter__(self):
        self.level += 1
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.level -= 1
    
    def print(self, text):
        # I think this should be self.level-1, else tabspace is visible by default on first level itself
        print('\t' * self.level + text)
'''

with Indenter() as indent:
    indent.print('hi')
    with indent:
        indent.print('hello')
        with indent:
            indent.print('bonjour')

    indent.print('hey')
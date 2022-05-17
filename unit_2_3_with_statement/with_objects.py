# Making 'with' statement possible for our
# own custom objects.

# ManageFile class follows 'context manager' protocol
# or interface by implementing __enter__ and __exit__
# method. These will be called at appropriate times
# in the resource management cycle.
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
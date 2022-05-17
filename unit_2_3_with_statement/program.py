# Create a file and write to it.
# No Guarantee that the file is closed if there's
# an exception during f.write() - our program might
# leak a file descriptor.
f = open('hello.txt', 'w')
f.write('hello, world')
f.close()

# Guarantees that the file is closed even if there's
# an exception during f.write(). More Verbose.
f = open('hello.txt', 'w')
try:
    f.write('hello, world')
finally:
    f.close()

# Same as above but less verbose. Ensures that
# open file descriptors are closed automatically
# after program execution leaves the context of
# 'with' statement.
with open('hello.txt', 'w') as f:
    f.write('hello, world!')

# Acquiring & Releasing resources become easy with 'with'.
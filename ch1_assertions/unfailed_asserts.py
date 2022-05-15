assert(1==2, 'This should fail') # Runs succesfully. Still Python may show warning for syntax issue.

assert (9 == 10, 'It should have counted all items.')

# Assert with first argument as tuple always return True since tuple
# has items.

assert () # Only this may throw error since it is empty tuple.
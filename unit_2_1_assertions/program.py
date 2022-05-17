# All about Assertions in Python

from multiprocessing import AuthenticationError

def apply_discount(product, discount):
    price = int(product['price'] * (1.0 - discount))
    assert 0 <= price <= product['price'] # throws AssertionError when this impossible condition is met.
    return price

shoes = {
    'name': 'Fancy Shoes',
    'price': 14900
}

discounted_price = apply_discount(shoes, 0.25)
print(discounted_price)

discounted_price = apply_discount(shoes, 2.0) # throws AssertionError.
print(discounted_price)

# Don't use Assert for Data Validation
# assert is run if program is in debug mode only.
# so we can't beleive it to be checked always.
# try -O and -OO command line switches while
# running this program.
# > python -O program.py // removes assert and __debug__ dependent statements.
#####So Don't use assert for input data validation#####

store = None
def delete_product(prod_id, user):
    assert user.is_admin(), 'Must be admin'
    assert store.has_product(prod_id), 'Unknown Product'
    store.get_product(prod_id).delete()

# If we depend on assert to validate if user is admin &
# If store has a product, then if assertions are disabled
# without doing these checks, the product will be deleted
# which leads to like 
# 1. Any user can now delete product.
# 2. Trying to delete product even if it doesn't exist

# BELOW IS THE RIGHT WAY FOR VALIDATION
def delete_product(prod_id, user):
    if not user.isadmin():
        raise AuthenticationError('Must be admin to delete')
    if not store.has_product(prod_id):
        raise ValueError('Unknown product id')
    store.get_product(prod_id).delete()

# Summary:
# Assertion is just a debugging aid that self-checks the program.
# Assertions are not mechanism for handling run-time errors.
# Asserts can be globally disabled with interpreter setting. (> python -O program.py)
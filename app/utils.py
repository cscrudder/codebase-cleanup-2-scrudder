## THIS FILE CONTAINS FUNCTIONS USED ACROSS APP FILES. 

# This function formats float into USD
def to_usd(price):
    """
    This function returns the formatted USD value of an input price.
    For example, 1234.56 would become $1234.56.
    The only input to the function is the number to be formatted.
    This function can be used in many applications to make a readable output for the user.
    """
    return '${:,.2f}'.format(price)


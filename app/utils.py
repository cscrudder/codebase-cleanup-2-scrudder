## THIS FILE CONTAINS FUNCTIONS USED ACROSS APP FILES. 

# This function formats float into USD
def to_usd(price):
    return '${:,.2f}'.format(price)

print(to_usd(3234))
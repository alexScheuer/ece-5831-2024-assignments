# pricing.py

def get_net_price(price, tax_rate, discount=0):
    return price * (1 + tax_rate) * (1-discount)


def get_tax(price, tax_rate=0):
    return price * tax_rate

import module_name

import pricing

module_name.function_name()

# main.py
import pricing


net_price = pricing.get_net_price(
    price=100,
    tax_rate=0.01
)

print(net_price)

import pricing as selling_price

net_price = selling_price.get_net_price(
    price=100,
    tax_rate=0.01
)

from module_name import fn1, fn2

fn1()
fn2()

# main.py
from pricing import get_net_price

# main.py
from pricing import get_net_price

net_price = get_net_price(price=100, tax_rate=0.01)
print(net_price)

from <module_name> import <name> as <new_name>

from pricing import get_net_price as calculate_net_price

net_price = calculate_net_price(
    price=100,
    tax_rate=0.1,
    discount=0.05
)

from module_name import *

# product.py
def get_tax(price):
    return price * 0.1

from pricing import *
from product import *

tax = get_tax(100)
print(tax)
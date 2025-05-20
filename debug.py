

from customer import Customer
from coffee import Coffee
from order import Order


alice = Customer("Alice")
bob = Customer("Bob")

latte = Coffee("Latte")
mocha = Coffee("Mocha")


alice.create_order(latte, 5.0)
alice.create_order(mocha, 6.0)
bob.create_order(latte, 7.5)


print(f"Alice's coffees: {[c.name for c in alice.coffees()]}")
print(f"Latte customers: {[c.name for c in latte.customers()]}")
print(f"Latte orders: {latte.num_orders()}")
print(f"Latte average price: {latte.average_price()}")


top = Customer.most_aficionado(latte)
print(f"Most aficionado for latte: {top.name if top else 'None'}")

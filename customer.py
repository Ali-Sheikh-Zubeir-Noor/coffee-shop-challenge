from order import Order

class Customer:
    all = []

    def __init__(self, name):
        self.name = name
        Customer.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 15:
            self._name = value
        else:
            raise ValueError("Name must be a string between 1 and 15 characters.")

    def orders(self):
        return [order for order in Order.all if order.customer == self]

    def coffees(self):
        return list(set(order.coffee for order in self.orders()))

    def create_order(self, coffee, price):
        from coffee import Coffee  
        if not isinstance(coffee, Coffee):
            raise TypeError("Must provide a Coffee instance.")
        return Order(self, coffee, price)

    @classmethod
    def most_aficionado(cls, coffee):
        top_customer = None
        max_spent = 0
        for customer in cls.all:
            total = sum(order.price for order in customer.orders() if order.coffee == coffee)
            if total > max_spent:
                max_spent = total
                top_customer = customer
        return top_customer

from customer import Customer
from coffee import Coffee
from order import Order


cust1 = Customer("Mwendwa")
cust2 = Customer("Ivana")


coffee1 = Coffee("Latte")
coffee2 = Coffee("Cappuccino")


order1 = cust1.create_order(coffee1, 5.0)
order2 = cust1.create_order(coffee2, 6.5)
order3 = cust2.create_order(coffee1, 4.5)

print("Customer 1 Coffees:", [c.name for c in cust1.coffees()])
print("Coffee 1 Customers:", [c.name for c in coffee1.customers()])
print("Coffee 1 Orders Count:", coffee1.num_orders())
print("Coffee 1 Average Price:", round(coffee1.average_price(), 2))

most = Customer.most_aficionado(coffee1)
print("Most Aficionado for Coffee 1:", most.name if most else "None")

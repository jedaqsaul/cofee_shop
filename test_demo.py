from customer import Customer
from coffee import Coffee


customer1 = Customer("Jedidiah")
customer2 = Customer("Aquila")


coffee1 = Coffee("Latte")
coffee2 = Coffee("Espresso")


customer1.create_order(coffee1, 5.0)
customer1.create_order(coffee2, 4.5)
customer2.create_order(coffee1, 6.0)


print(f"\nOrders for {customer1.name}:")
print(customer1.orders())

print(f"\nCoffees ordered by {customer1.name}:")
print(customer1.coffees())

print(f"\nOrders for {customer2.name}:")
print(customer2.orders())

print(f"\nCoffees ordered by {customer2.name}:")
print(customer2.coffees())

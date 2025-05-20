 - Understanding the Domain Model
 - learn about- one to many and many to many relationships
 - identity classes : Customer, Cofee and Order
 -plan attributes and relationshipa

 ### Build the class skeletons
 - create customer.py, cofee,py and order.py
 - create empty class definitions with __init__ methods
 ### implements initializers with validation
 - add and validate -Customer.name, Coffee.name- Order.customer, Order.coffee, order.price

 ### object relationships methoods
 - customer- orders(), coffee()
 - coffee -orders() customers()
 - Order -Returns related Customer and Coffee

### Creating and Aggregating Data
- Customer.create_order(coffee, price)

- Coffee.num_orders()

 - Coffee.average_price()

### Advanced Relationship Logic
C- ustomer.most_aficionado(coffee): who spent the most on a coffee

### Testing with Pytest
- Set up tests/ directory

- create test files and write test functions

### Error Handling and Validation
Use raise for:

Invalid types

Invalid lengths

Invalid price ranges

### Debugging and Refactoring
Create debug.py for testing interactively

Clean up code: PEP8, helper methods, readability

# understanding the domain model
- What objects (classes) exist in the real-world problem

- How they relate

- What attributes and behaviors each object has

#  Coffee Shop Domain
### Classes
Customer

Coffee

Order

### Relationships
A Customer can place many Orders

A Coffee can have many Orders

An Order belongs to one Customer and one Coffee

That makes the relationship between Customer and Coffee a many-to-many, with Order as the join or association class.
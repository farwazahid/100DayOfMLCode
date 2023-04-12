class Item:
#methods
    def price_calculater(self, x, y):
        return x*y

#item1 and item2 are objects
# name, price, quantity are the attributes
item1 = Item()
item1.name = "Airpods"
item1.price = 500
item1.quantity = 4
print(item1.price_calculater(item1.price, item1.quantity))

item2 = Item()
item2.name = "Watches"
item2.price = 5000
item2.quantity = 3
print(item2.price_calculater(item2.price, item2.quantity))


class Item:
#methods
    def __init__(self, name):
        self.name = name
    def price_calculater(self, x, y):
        return x*y

#item1 and item2 are objects
# name, price, quantity are the attributes
item1 = Item("Airpods")
item1.price = 500
item1.quantity = 4


item2 = Item("Watches")
item2.price = 5000
item2.quantity = 3

print(item1.name)
print(item2.name)


class Item:
#methods
    def __init__(self, name):
        self.name = name
    def price_calculater(self, x, y):
        return x*y

#item1 and item2 are objects
# name, price, quantity are the attributes
item1 = Item("Airpods")
item1.price = 500
item1.quantity = 4

item2 = Item("Watches")
item2.price = 5000
item2.quantity = 3

print(item1.name)
print(item2.name)



class Item:
#methods
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


    def price_calculator(self):
        return self.price * self.quantity

#item1 and item2 are objects
# name, price, quantity are the attributes
item1 = Item("Airpods", 500, 4)
item2 = Item("Watches", 800, 3)

print(item1.name)
print(item2.name)
print(item1.price)
print(item2.price)
print(item1.quantity)
print(item2.quantity)
print(item1.price_calculator())
print(item2.price_calculator())



class Item:
    pay_rate = 0.8 #the pay rate after 20% discount
#methods
    def __init__(self, name: str, price: float, quantity: int):
        #run validation to the received argument
        assert price >= 0, f"Price {price} is not greater than or equal to zero"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero"
        self.name = name
        self.price = price
        self.quantity = quantity

    def price_calculator(self):
        return self.price * self.quantity

#item1 and item2 are objects
# name, price, quantity are the attributes
item1 = Item("Airpods", 500, 4)
item2 = Item("Watches", 800, 3)

print(Item.pay_rate)
print(item1.pay_rate)
print(item2.pay_rate)

class Item:
    pay_rate = 0.8 #the pay rate after 20% discount
#methods
    def __init__(self, name: str, price: float, quantity: int):
        #run validation to the received argument
        assert price >= 0, f"Price {price} is not greater than or equal to zero"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero"
        self.name = name
        self.price = price
        self.quantity = quantity

    def price_calculator(self):
        return self.price * self.quantity

#item1 and item2 are objects
# name, price, quantity are the attributes
item1 = Item("Airpods", 500, 4)
item2 = Item("Watches", 800, 3)

print(Item.__dict__) #All the attribuets for the class level. This __dict__ converts all the attributes into a dictionary.
print(item1.__dict__)#All the attributes for the instance level



class Item:
    pay_rate = 0.8 #the pay rate after 20% discount
#methods
    def __init__(self, name: str, price: float, quantity: int):
        #run validation to the received argument
        assert price >= 0, f"Price {price} is not greater than or equal to zero"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero"
        self.name = name
        self.price = price
        self.quantity = quantity

    def price_calculator(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * Item.pay_rate
#item1 and item2 are objects
# name, price, quantity are the attributes
item1 = Item("Airpods", 500, 4)
item1.apply_discount()
print(item1.price)

item2 = Item("Watches", 800, 3)
item2.pay_rate = 0.7 #It will change the discount different for item2

print(Item.__dict__) #All the attribuets for the class level. This __dict__ converts all the attributes into a dictionary.
print(item1.__dict__)#All the attributes for the instance level
--
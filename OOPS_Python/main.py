# item1 = 'Phone'
# item1_price = 100
# item1_quantity = 5
# item1_total = item1_price * item1_quantity
#
# print(type(item1))
# print(type(item1_price))
# print(type(item1_quantity))
# print(type(item1_total))


class Item:
    # class attributes
    payrate = 0.8 #value after 20% discount

    # methods with start and ending udouble underscores are called magic methods
    # when you set datatype as float for price, it accepts both int and float

    def __init__(self, name: str, price: float, quantity=0):
        # to check the received arguments we use assert statements
        assert price >= 0, f"Price {price} is not greater than or equal to zero"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero"

        # received arguments
        self.name = name
        self.price = price
        self.quantity = quantity

        """ , price, quantity """
    def cal_total_price(self):
        return self.price * self.quantity

        # return price * quantity
    def apply_discount(self):
        self.price = self.price * self.payrate

        # self.price = self.price * Item.payrate


# Note: If we send a value other than string value, it shows a warning that it expects str value
item1 = Item('Phone', 100, 5)
# example : str1 = 'anjani' is same as str1 = str('anjani')
# item1.name = 'Phone'
# item1.price = 100
# item1.quantity = 5
# print(item1.cal_total_price( item1.price, item1.quantity))

# print(item1.cal_total_price())
# print(item1.apply_discount())

# print(type(item1))

item2 = Item('Laptop', 1000, 3)
# item2.name = 'Laptop'
# item2.price = 1000
# item2.quantity = 4
# print(item2.cal_total_price( item2.price, item2.quantity))

# print(item2.cal_total_price())


# print(type(item2))

# NOTE: Everytime a method is called using an instance, the instance itself is passed as the first argument
# to the method hence we need to have self parameter as first argument in methods

# to access class attributes, access it by class level
# print(Item.payrate)
# print(item1.payrate)
# print(item2.payrate)

# all attributes for class level
# print(Item.__dict__)
# # all attributes for instance level
# print(item1.__dict__)
item3 = Item('Watches', 2000, 6)
# item3.apply_discount()
# print(item3.price)

# In order to set a discount specificaly for laptop or specific item, you can set that attribute for that
# object at the instance level and hence it will not search for that variable at class level and can
# find that variable at the instance level

item3.payrate = 0.7 #30% discount
# item3.apply_discount()
# print(item3.price)
# so we saw that variable value is from instance level but we are using class variable call i.e.
# Item.payrate so a good practice will be to use self.payrate which will search for the variable at instance level
# first then at class level

item1.apply_discount()
print(item1.price)
item3.apply_discount()
print(item3.price)
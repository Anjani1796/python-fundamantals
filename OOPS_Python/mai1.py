import csv


"""
The @staticmethod is a built-in decorator that defines a static method in the class in Python. 
A static method doesn't receive any reference argument whether it is called by an instance of a class
or by the class itself.

@staticmethod Characteristics
Declares a static method in the class.
It cannot have cls or self parameter.
The static method cannot access the class attributes or the instance attributes.
The static method can be called using ClassName.MethodName() and also using object.MethodName().
It can return an object of the class.

"""

class Item:
    payrate = 0.8

    # To maintain a list of instances we create a list named as "all" and append all instance ata the time of __init__
    all = []
    def __init__(self, name: str, price: float, quantity=0):
        assert price >= 0, f"Price {price} is not greater than or equal to zero"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero"

        self.name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self) #self has the instance which is created whenever an object is created

    def cal_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.payrate

    # when a class method is made it receives a parameter "cls" which means The class itself(here Item)
    # is passed as first parameter
    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f) #reads the content of the file as dictionary
            items = list(reader) #but we converted it to list to keep it standard across

        # it prints a list of dictionaries
        # for item in items:
        #     print(item)

        for item in items:
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                # price = int(item.get('price')), #using int for conversion can be a problem, so use float
                quantity = float(item.get('quantity'))
            )

    # static method neither receives self nor cls as first parameter
    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            # count out the floats that are all zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False
    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"

#these have been shifted to csv and used from there
# item1 = Item('Phone', 100, 1)
# item2 = Item('Laptop', 1000, 3)
# item3 = Item('Cable', 10, 5)
# item4 = Item('Mouse', 50, 5)
# item5 = Item('Keyboard', 75, 5)

# print(Item.all)

# for instance in Item.all:
#     print(instance.name)

# FOR CALLING ststic method
# Item.instantiate_from_csv()
# print(Item.all)

# for calling static method
print(Item.is_integer(2.5)) #False
print(Item.is_integer(2.0)) #True
print(Item.is_integer(2)) #True
print(Item.is_integer(True)) #True


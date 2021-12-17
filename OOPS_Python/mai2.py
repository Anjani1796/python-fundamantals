import csv

class Item:

    payrate = 0.8

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

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f) #reads the content of the file as dictionary
            items = list(reader) #but we converted it to list to keep it standard across

        for item in items:
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity = float(item.get('quantity'))
            )

    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False
    def __repr__(self):
        # calling the class name generically rather than hard coding the class name
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"
        # return f"Item('{self.name}', {self.price}, {self.quantity})"

class Phone(Item):
    # we can remove the "all" attribute coz we are inheriting all attributes and methods of class Item
    # including "all"
    # all = []

    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):

        #call to super function to acess all attributes / methods oof parent class
        # we also have access to the class attribute of parent class i.e. all, so we can access that
        # attribue also
        super().__init__(
            name, price, quantity
        )

        # assert price >= 0, f"Price {price} is not greater than or equal to zero"
        # assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero"
        assert broken_phones >= 0, f"Broken Phones {broken_phones} is not greater than or equal to zero"

        # self.name = name
        # self.price = price
        # self.quantity = quantity
        self.broken_phones = broken_phones

        # removes the "all" attribute coz child class is inheriting the class attributeof parent class
        # "all"
        # Phone.all.append(self)


phone1 = Phone("jscPhonev10", 500, 5, 1)
print(phone1.cal_total_price())
# phone1.broken_phone = 1
phone2 = Phone("jscPhonev20", 700, 5, 1)
# phone2.broken_phone = 2

print(Item.all)
print(Phone.all)

# output
# [Item('jscPhonev10', 500, 5), Item('jscPhonev20', 700, 5)]
# [Item('jscPhonev10', 500, 5), Item('jscPhonev20', 700, 5)]
# output shows the return from print and also the repr method, but we have Item only because
# its hard coded hence we should call the class name generically
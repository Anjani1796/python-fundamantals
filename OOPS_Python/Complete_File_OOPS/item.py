import csv

class Item:
    payrate = 0.8

    all = []
    def __init__(self, name: str, price: float, quantity=0):
        assert price >= 0, f"Price {price} is not greater than or equal to zero"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero"

        self.__name = name
        self.__price = price
        self.quantity = quantity

        Item.all.append(self) #self has the instance which is created whenever an object is created

    @property
    def price(self):
        return self.__price

    def apply_discount(self):
        self.__price = self.__price * self.payrate

    def apply_increment(self, increment_value):
        self.__price = self.__price + self.__price * increment_value

    @property
    # Property Decorator = Read Only Attribute
    # It means once sometjing is assigned inside property then that can't be used anywhere by class
    # hence we will not be able to use self.name = name under __init__() method
    # which gives an error: "name cannot be set" in the init method
    # To solve this issue we make this attribute protected where ever used
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception("Word is too long!!")
        else:
            self.__name = value

    def cal_total_price(self):
        return self.__price * self.quantity


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
        return f"{self.__class__.__name__}('{self.name}', {self.__price}, {self.quantity})"

    # @property
    # def read_only_name(self):
    #     return "AAA"

    def __connect(self, smtp_server):
        pass

    def __prepare_body(self):
        return f"""
        Hello Someone,
        We have {self.name} {self.quantity} times.
        Regards, Delhivan
        """
    def __send(self):
        pass

    def send_email(self):
        self.__connect("connect received")
        self.__prepare_body()
        self.__send()
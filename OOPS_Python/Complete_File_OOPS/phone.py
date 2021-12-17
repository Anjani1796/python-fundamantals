from item import Item

# this class is inheriting the Item class so import that class
class Phone(Item):

    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):

        super().__init__(
            name, price, quantity
        )

        assert broken_phones >= 0, f"Broken Phones {broken_phones} is not greater than or equal to zero"

        self.broken_phones = broken_phones

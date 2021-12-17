from item import Item

class Keyboard(Item):
    payrate = 0.7 #apply 30% discount for all the keyboard instances
    def __init__(self, name: str, price: float, quantity=0):

        super().__init__(
            name, price, quantity
        )
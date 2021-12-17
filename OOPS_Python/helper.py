

# When to use classmethod and when to use static method

"""

A class method takes cls as the first parameter while a static method needs no specific parameters.
A class method can access or modify the class state while a static method can’t access or modify it.
In general, static methods know nothing about the class state. They are utility-type methods that take
some parameters and work upon those parameters. On the other hand class methods must have class as a
parameter.
We use @classmethod decorator in python to create a class method and we use @staticmethod decorator to
create a static method in python.

When to use what?
We generally use class method to create factory methods. Factory methods return class objects
( similar to a constructor ) for different use cases.
We generally use static methods to create utility functions.
"""

class Item:
    @staticmethod
    def is_integer():
        """Does not have something that must be unique per instance"""
        pass

    @classmethod
    def instantiate_from_something(cls):
        """used to manipulate different structures of data to instantiate objects like csv, json, etc."""
        pass

"""
class methods and static methods can be called from class level as well as from the instance level
but there will never be a use case for calling these methods from the instance level
"""
item1 = Item()
item1.is_integer()
item1.instantiate_from_something()
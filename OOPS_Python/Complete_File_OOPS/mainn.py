# use this class to operate those item and phone classes means
# This class is used to create instances and operational stuff
'''
from item import Item
from phone import Phone

Item.instantiate_from_csv()
print(Item.all)
'''

# It is always advised to use parent class for operating other classes which doesn't mean you cannot
# call child classes like these but it is advised to use Parent class

# UNDERSTANDING THE GETTERS AND SETTERS
#
# from item import Item
#
# item1 = Item('MyItem', 750)
# item1.name = 'OtherItem'
#
# print(item1.name)


# SO WHAT WE ARE TRYING TO IMPLEMENT HERE IS THAT WE WANT WE WANT TO RESTRICT THE CHANGE TO THESE
# ATTRIBUTES WHICH WE CHANGED HERE, SO HERE THE ENCAPSULATION COMES INTO PLACE

# JUST GIVE A SINGLE CHANCE TO CHANGE / SET THE ATTRIBUTES OF AN OBJECT

"""
@property is used to get the value of a private attribute without using any getter methods.
We have to put a line @property in front of the method where we return the private variable.

To set the value of the private variable, we use @method_name.setter in front of the method.
We have to use it as a setter.
"""

# print(item1.read_only_name) #AAA

# change the value
# item1.read_only_name = "BBB" # received can't set attribute



from item import Item

# item1 = Item('MyItem', 750)
# item1.name = 'OtherItem' throws error as cannot be set

# print(item1.name)

# print(item1._name) #we can still access this _name from the instance level, so to vaoid this
# we use __name which restrict the access
# print(item1.__name) says attribute cannot be set

# item1.name = "Hi_changed"
# print(item1.name)


# item1.apply_increment(0.2) #20% increment
# print(item1.price) # 900.0


# item1.apply_increment(0.2)
# item1.apply_discount()
# print(item1.price) #720.0


#
# item1 = Item('MyItem', 750, 6)
# item1.send_email()
# here while trying to access the send, connect, prepare_body all these were accessible
# but there is no point of showing these methods to the user, so we will abstract these
# methods by adding "__" double underscores before these methods

# #inheritance
# from phone import Phone
# item1 = Phone("Phone_version", 1000, 6)
# item1.apply_increment(0.2)
# print(item1.price)
# item1.send_email()


# POLYMORPHISM
# Means here the single method apply_discount() is used in many forms by different
# objects and accessible to all
from keyboard import Keyboard

item1 = Keyboard("keyboard_model", 1000, 5)
item1.apply_discount()
print(item1.price)
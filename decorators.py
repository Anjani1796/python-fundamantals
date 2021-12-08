# def non_negative_arguments(decorated_fn):
#     def check_non_negative(*args):
#         for arg in args:
#             if arg <= 0:
#                 raise ValueError("Argument cannot ne negative or zero")
#
#         return decorated_fn(*args)
#     return check_non_negative

# # PRACTICE
# def display_important_msg():
#     print("This is an important message")
# # display_important_msg()
#
#
# def display_boring_msg():
#     print("This is a boring message....")
# # display_boring_msg()
#
# def display_entertaining_msg():
#     print("This is an entertainining message....")
# # display_entertaining_msg()
#
# def emphasize_msg(display_fn):
#     print("*********************************************")
#     display_fn()
#     print("*********************************************")
#
# emphasize_msg(display_important_msg)
# emphasize_msg(display_entertaining_msg)
#
# display_and_emphasize_imp_msg = emphasize_msg(display_important_msg)
# display_and_emphasize_imp_msg
#
#
# display_and_emphasize_enter_msg = emphasize_msg(display_entertaining_msg)
# display_and_emphasize_enter_msg
#
#
# def emphasize(defined_fn):
#     def emp_message():
#         print("*************************************************")
#         defined_fn()
#         print("*************************************************")
#     return emp_message
#
# @emphasize
# def display_imp_msg():
#     print("This is an Important msg")
#
# @emphasize
# def display_boring_msg():
#     print("This is an Boring msg")
#
# @emphasize
# def display_enter_msg():
#     print("This is an Entertaining msg")
#
# display_imp_msg()
# display_boring_msg()
# display_enter_msg()

# OUTPUT
#
# *************************************************
# This is an Important msg
# *************************************************
# *************************************************
# This is an Boring msg
# *************************************************
# *************************************************
# This is an Entertaining msg
# *************************************************
#
# Process finished with exit code 0



import math
#
#
# def compute_circle_area(radius):
#     return math.pi * radius * radius
#
# print(compute_circle_area(5))  #78.53981633974483
# print(compute_circle_area(-11)) #380.1327110843649
# print(compute_circle_area(11)) #380.1327110843649

def non_negative_arguments(decorated_fn):
    def check_non_negative(*args):
        for arg in args:
            if arg <= 0:
                raise ValueError("Argument cannot ne negative or zero")
        return decorated_fn(*args)
    return check_non_negative

@non_negative_arguments
def compute_circle_area(radius):
    return math.pi * radius * radius

@non_negative_arguments
def compute_circle_parameter(radius):
    return 2 * math.pi * radius

print(compute_circle_area(5)) #78.53981633974483
# print(compute_circle_area(-5)) #shows error, argument cannot be negative or zero
print(compute_circle_parameter(5)) #31.41592653589793
# print(compute_circle_parameter(-5)) ##shows error, argument cannot be negative or zero



@non_negative_arguments
def compute_rectangle_area(length, breadth):
    return length * breadth
print(compute_rectangle_area(5, 10)) #50
print(compute_rectangle_area(5, -10)) #shows error, argument cannot be negative or zero
#TypeError: check_non_negative() takes 1 positional argument but 2 were given
# Python pushes the input argument into the closure which further checks the condition and returns the output

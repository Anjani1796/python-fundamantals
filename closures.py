# def outer():
#     def fav_program_print():
#         print("favorite program")
#     print("outer function")
#     fav_program_print()
# outer()
# # output
# # outer function
# # favorite program
#
# # Closures concept means when a function is defined inside of a function and is returned from that function
# Any function returned from the function is called closure
# def outer():
#     def fav_program_print():
#         print("favorite program")
#     print("outer function")
#     fav_program_print()
# outer()
# fav_program_print()

# NameError: name 'fav_program_print' is not defined, cause, inner program is local to the outer () function


# # DESCRIBING A CLOSURE
# def outer():
#     def fav_program_print():
#         print("favorite program")
#     print("outer function")
#     return fav_program_print
# fun_call = outer() #outer function

# print(fun_call) #<function outer.<locals>.fav_program_print at 0x000001FD27B9CB80>
# this returns the whole info about the outer function and locals available to that function including function
# accessing the closure is like taking the function into a variable and then calling the function

#
# fun_call #outer function
# fun_call() #favorite program
#

# def outer1():
#     function_var = "Python"
#     def inner_closure_function():
#         print(f'This is the inner function {function_var}')
#     print("This is the outer function")
#     return inner_closure_function
# fun_Call1 = outer1()
#
# fun_Call1 #This is the outer function
# fun_Call1() #This is the inner function Python
#
#
#
#
# def outer2(function_var):
#     def inner_closure_function1():
#         print(f'This is the inner function {function_var}')
#     print("This is the outer function")
#     return inner_closure_function1
# fun_Call2 = outer2("Python")
# fun_Call3 = outer2("JavaScript")
#
# print(fun_Call2) #This is the outer function
# print(fun_Call2()) #This is the inner function Python
#
# fun_Call2 #This is the outer function
# fun_Call2() #This is the inner function Python
#
#
# del outer2
# # outer2() #NameError: name 'outer2' is not defined
#
# print(fun_Call2())
#
# # when the outer function is deleted, it does not affect the inner closures that is being called,
# # the inner will still remember the inner state of the function call

#
# def add_emp_list(department_name):
#     emp_list = []
#     def add_emp(emp_name):
#         emp_list.append(emp_name)
#         print(f"Added {emp_name} to {department_name}")
#         print(f"{department_name} employees: {emp_list}")
#
#     return add_emp
# add_to_Sales_fn = add_emp_list("sales")
# print(add_to_Sales_fn)
# add_to_Engg_fn = add_emp_list("Engineering")
# print(add_to_Engg_fn)
#
# add_to_Sales_fn("Issac")
# add_to_Sales_fn("Jonas")
# add_to_Sales_fn("Joe")
#
# add_to_Engg_fn("kim")
# add_to_Engg_fn("Mitch")
# add_to_Engg_fn("Elizabeth")
#
#
# def formal_greeting():
#     greeting = "How are you doing"
#     def informal_greeting():
#         greeting = "Hi, there"
#         print("Informal greeting is: ", greeting)
#
#     informal_greeting()
#     print("Formal greeting is: ", greeting)
#
# formal_greeting()

# output
# Informal greeting is:  Hi, there
# Formal greeting is:  How are you doing


def formal_greeting():
    greeting = "How are you doing"
    def informal_greeting():
        nonlocal greeting
        greeting = "Hi, there"
        print("Informal greeting is: ", greeting)

    informal_greeting()
    print("Formal greeting is: ", greeting)

formal_greeting()

# output
# Informal greeting is:  Hi, there
# Formal greeting is:  Hi, there
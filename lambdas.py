def increment(x):
    return (x+1)
print(increment(6))

# using lambdas
func = lambda x: x + 1 #7
print(func) #<function <lambda> at 0x000002D46348CB80>
print(func(10)) #11

def square(a):
    return a ** 2
def cube(a):
    return a ** 3
def square_root(a):
    return a ** 1/2
def cube_root(a):
    return a ** 1/3
def raise_to_power_n(a, n):
    return a ** n

print(square(5)) #11
print(cube(5)) #25
print(square_root(5)) #125
print(cube_root(5)) #1.66666666666666667
print(raise_to_power_n(5, 3)) #3125

square1 = lambda a: a ** 2
cube1 = lambda a: a ** 3
square_root1 = lambda a: a ** 1/2
cube_root1 = lambda a: a ** 1/3
raise_to_a1 = lambda a, n: a ** n


print(square1(5)) #11
print(cube1(5)) #25
print(square_root1(5)) #125
print(cube_root1(5)) #1.66666666666666667
print(raise_to_a1(5, 3)) #3125


# To print a string a specific number of times
create_string = lambda strng, times: [strng for _ in range(times)]
print(create_string("Anjani", 4))


print((lambda x: x * 10)(33)) #330
print((lambda x, y: x * y)(33, 20)) #660



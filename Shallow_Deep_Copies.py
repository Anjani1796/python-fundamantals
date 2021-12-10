# Shallow copy - when we create a copy of any data structure, like list, tuple, dictionary, sets any changes made to the
# copy also change the original, is a shallow copy
# Deep copy - when we create a copy of any data structure, like list, tuple, dictionary, sets any changes made to the
# copy do not change the original, is a deep copy

# old_str = "Python"
# print(old_str)

# new_str = old_str
# print(new_str) #Python
# print(old_str) #Python
#
# print(new_str[2]) #t
# print(old_str[2]) #t

# trying to update the value in copy
# new_str[2] = 'T' #TypeError: 'str' object does not support item assignment


# If we set the new_str to some other string, it will not affect the old_str str
# new_str = "Java"
# print(new_str) #Java
# print(old_str) #Python

import copy

# first_str = 'Will'
# print(first_str) #Will
#
# second_str = copy.copy(first_str)
# # module.function()
# # print("first string: ", first_str) #first string:  Will
# # print("second string: ", second_str) #second string:  Will
#
# second_str = "Smith"
# print("first string: ", first_str) #first string:  Will
# print("second string: ", second_str) #second string:  Smith
# The change in the second copy does not change the first string

# Important - The copy and deepcopy of an object is same in Python



# first_str = "Johnny"
# second_str = copy.deepcopy(first_str)
#
# # print("First String: ",first_str) #First String:  Johnny
# # print("Second String: ",second_str) #Second String:  Johnny
#
# second_str = "Depp"
#
# print("First String: ",first_str) #First String:  Johnny
# print("Second String: ",second_str) #Second String:  Depp
# # the first_string remains unchanged
#


# Shallow Copy
# We know lists are mutable and strings are immutable
# names = ['Sara', 'David', 'Warner', 'Sandy']
# new_names = names #In this line, names and new_names are pointing to the same list, hence on making changes in the new_names also change the names
# print('Original: ', names)
# print('Copy: ', new_names)

# Original:  ['Sara', 'David', 'Warner', 'Sandy']
# Copy:  ['Sara', 'David', 'Warner', 'Sandy']

# If we assign a whole new list for new_names, this points to the new list, then new_names and names become different
#
# new_names[1] = 'Ridley'
# print('Original: ', names)
# print('Copy: ', new_names)

# Original:  ['Sara', 'Ridley', 'Warner', 'Sandy']
# Copy:  ['Sara', 'Ridley', 'Warner', 'Sandy']

# By normal assignment operator, python creates the shallow copy, which means changing the copy will change the original also


# LIST SHALLOW COPY and DEEP COPY
# import copy
#
# companies = ['hackerearth', 'google', 'facebook']
# print(companies)

# new_companies = copy.copy(companies) #this creates a deep copy of the list
# print("Original: ", companies)
# print("Copy: ", new_companies)
#
# # Original:  ['hackerearth', 'google', 'facebook']
# # Copy:  ['hackerearth', 'google', 'facebook']
#
# print(new_companies[1])
#
# new_companies[1] = 'microsoft'
# print("Original: ", companies)
# print("Copy: ", new_companies)

# Original:  ['hackerearth', 'google', 'facebook']
# Copy:  ['hackerearth', 'microsoft', 'facebook']

# creating a list copy using assignment creates the shallow copy and
# creating a list copy using copy.copy() creates the deep copy

# Nested lists

# old_list = [[1,2,3], [4,5,6], [7,8,9]]
#
# new_list = copy.copy(old_list)
# print("Old List: ", old_list)
# print("New List: ", new_list)

# Old List:  [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# New List:  [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# print(old_list[1][1]) #5

# new assignment made using the original list
# old_list[1][1] = 'Five'

# print("Old List: ", old_list)
# print("New List: ", new_list)
# Old List:  [[1, 2, 3], [4, 'Five', 6], [7, 8, 9]]
# New List:  [[1, 2, 3], [4, 'Five', 6], [7, 8, 9]]

# Point - copy.copy(list) created an deep copy of the outer list and an shallow copy of the inner list


# new_list[2].append('Ten')

# print("Old List: ", old_list)
# print("New List: ", new_list)

#Old List:  [[1, 2, 3], [4, 'Five', 6], [7, 8, 9, 'Ten']]
# New List:  [[1, 2, 3], [4, 'Five', 6], [7, 8, 9, 'Ten']]

# copy() function only creates the shallow copy of both inner and outer list

# old_list.append([10, 11,12])
# print("Old List: ", old_list)
# print("New List: ", new_list)

# Old List:  [[1, 2, 3], [4, 'Five', 6], [7, 8, 9, 'Ten'], [10, 11, 12]]
# New List:  [[1, 2, 3], [4, 'Five', 6], [7, 8, 9, 'Ten']]

# copy.copy() creates deep copy of outer list
# Any changes made to original or outer list will not be reflected in inner or new list but any changes made to the inner list or new list will
# be reflected to the both outer and inner lists

# CREATING DEEP COPIES OF NESTED LIST
# names = ['Sara', 'David', 'Warner', 'Sandy']
# print(names)

# new_names = names.copy()

# print("Old Names: ", names)
# print("New Names: ", new_names)

# Old Names:  ['Sara', 'David', 'Warner', 'Sandy']
# New Names:  ['Sara', 'David', 'Warner', 'Sandy']

# new_names[1] = 'Ridley'
# print("Old Names: ", names)
# print("New Names: ", new_names)

# Old Names:  ['Sara', 'David', 'Warner', 'Sandy']
# New Names:  ['Sara', 'Ridley', 'Warner', 'Sandy']

# the list.copy() function creates a deep copy of list

# import copy
#
# companies = ['hackerearth', "google", 'facebook']
# print(companies)
#
# new_companies = copy.copy(companies)
# print("Original: ", companies)
# print("New: ", new_companies)

# Original:  ['hackerearth', 'google', 'facebook']
# New:  ['hackerearth', 'google', 'facebook']

# new_companies[1] = 'microsoft'
# print("Original: ", companies)
# print("New: ", new_companies)

# Original:  ['hackerearth', 'google', 'facebook']
# New:  ['hackerearth', 'microsoft', 'facebook']

# copy.copy() and copy.deepcopy() function both creates deep copies of non-nested lists

# import copy
#
# old_list= [[1,2,3], [4,5,6], [7,8,9]]
# print(old_list)
#
# new_list = copy.deepcopy(old_list)
# print(old_list[1][2])
#
# old_list[1][2] = 'Six'
# print("Original: ", old_list)
# print("New: ", new_list)

# Original:  [[1, 2, 3], [4, 5, 'Six'], [7, 8, 9]]
# New:  [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


# Array slice operation creates the deep copy of the list
companies = ['hackerearth', 'google', 'facebook']

# new_companies = companies[:] #Array slice operation also creates the deep copy
# print(new_companies)
#
# new_companies[0] = 'skillsoft'
# print("original: ", companies)
# print("New: ", new_companies)

#original:  ['hackerearth', 'google', 'facebook']
# New:  ['skillsoft', 'google', 'facebook']


#
# # TUPLES
# fruits = ('apple', 'banana', 'cherry')
# new_fruits = fruits #both variables refers to the same tuple in memory
#
#
# print('Old: ', fruits)
# print('New: ', new_fruits)

#Old:  ['apple', 'banana', 'cherry']
# New:  ['apple', 'banana', 'cherry']

# new_fruits[2] = 'Orange'

#OUTPUT
#TypeError: 'tuple' object does not support item assignment, because tuples are immutable

# special case - when tuple contains a list element
# fruits = ('apple', ['banana', 'cherry'], 'blackcurrant')

# new_fruits = fruits
# print("Old: ", fruits)
# print("New: ", new_fruits)

# Old:  ('apple', ['banana', 'cherry'], 'blackcurrant')
# New:  ('apple', ['banana', 'cherry'], 'blackcurrant')

# print(new_fruits[1][0])
#
# new_fruits[1][0] = 'orange'
# print("Old: ", fruits)
# print("New: ", new_fruits)

#Old:  ('apple', ['orange', 'cherry'], 'blackcurrant')
# New:  ('apple', ['orange', 'cherry'], 'blackcurrant')

# import copy
#
# bikes = ('Honda', 'Suzuki', 'Triumph', ['kawasaki', 'Ducati'])
# print('OLD: ', bikes)

# new_bikes = copy.copy(bikes)
# print('OLD: ', bikes)
# print('NEW: ', new_bikes)

# OLD:  ('Honda', 'Suzuki', 'Triumph', ['kawasaki', 'Ducati'])
# NEW:  ('Honda', 'Suzuki', 'Triumph', ['kawasaki', 'Ducati'])

# new_bikes[3][0] = 'dodge'
# print('OLD: ', bikes)
# print('NEW: ', new_bikes)

# OLD:  ('Honda', 'Suzuki', 'Triumph', ['dodge', 'Ducati'])
# NEW:  ('Honda', 'Suzuki', 'Triumph', ['dodge', 'Ducati'])

# copy.copy() function does not create the deep copy of inner nested list, and rather a shallow copy


import copy

bikes = ('Honda', 'Suzuki', 'Triumph', ['kawasaki', 'Ducati'])
print('OLD: ', bikes)
# OLD:  ('Honda', 'Suzuki', 'Triumph', ['kawasaki', 'Ducati'])

new_bikes = copy.deepcopy(bikes)
print('OLD: ', bikes)
print('NEW: ', new_bikes)
# OLD:  ('Honda', 'Suzuki', 'Triumph', ['kawasaki', 'Ducati'])
# NEW:  ('Honda', 'Suzuki', 'Triumph', ['kawasaki', 'Ducati'])


new_bikes[3][0] = 'Harley Davidson'
print('OLD: ', bikes)
print('NEW: ', new_bikes)

# OLD:  ('Honda', 'Suzuki', 'Triumph', ['kawasaki', 'Ducati'])
# NEW:  ('Honda', 'Suzuki', 'Triumph', ['Harley Davidson', 'Ducati'])

# copy.deepcopy() function create the deep copy of whole list including nested list, and rather a shallow copy

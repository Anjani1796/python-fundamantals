# months = {'jan':1, 'feb':2, 'mar':3, 'apr': 4}
# print(months)
#
# new_months = months #both refers to the same memory here
# print("OLD: ", months)
# print("NEW: ", new_months)
# OLD:  {'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4}
# NEW:  {'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4}
#
# new_months['feb'] = 'FEB'
# print("OLD: ", months)
# print("NEW: ", new_months)
# OLD:  {'jan': 1, 'feb': 'FEB', 'mar': 3, 'apr': 4}
# NEW:  {'jan': 1, 'feb': 'FEB', 'mar': 3, 'apr': 4}
# assignment operator creates a shallow copy of dictionary



import copy

# employees = {'Alison':2007, 'Bart':2008, 'Cathy':2009, 'Dan': 2010}
#
# employees_copy = copy.copy(employees)
#
# # print(employees)
# # print(employees_copy)
#
# # {'Alison': 2007, 'Bart': 2008, 'Cathy': 2009, 'Dan': 2010}
# # {'Alison': 2007, 'Bart': 2008, 'Cathy': 2009, 'Dan': 2010}
#
# employees_copy['Alison'] = 2005
# print(employees)
# print(employees_copy)
#
# # {'Alison': 2007, 'Bart': 2008, 'Cathy': 2009, 'Dan': 2010}
# # {'Alison': 2005, 'Bart': 2008, 'Cathy': 2009, 'Dan': 2010}
# #
#
#
# orig_dic = {'one': 1, 'two': 2, 'three': 3, 'four': [1,2,3,4.0]}
# print(orig_dic)
#
# new_dict = copy.copy(orig_dic)
# print("Original: ", orig_dic)
# print("New: ", new_dict)

# Original:  {'one': 1, 'two': 2, 'three': 3, 'four': [1, 2, 3, 4.0]}
# New:  {'one': 1, 'two': 2, 'three': 3, 'four': [1, 2, 3, 4.0]}

# print(new_dict['four'][3]) #4.0
# new_dict['four'][3] = 'FOUR'
#
# print("Original: ", orig_dic)
# print("New: ", new_dict)

# Original:  {'one': 1, 'two': 2, 'three': 3, 'four': [1, 2, 3, 'FOUR']}
# New:  {'one': 1, 'two': 2, 'three': 3, 'four': [1, 2, 3, 'FOUR']}

# copy.copy(dict) creates the deep copy of outer dictionary but a shallow copy of the nested types

# new_dict['four'].append(5)
#
# print("Original: ", orig_dic)
# print("New: ", new_dict)

# Original:  {'one': 1, 'two': 2, 'three': 3, 'four': [1, 2, 3, 'FOUR', 5]}
# New:  {'one': 1, 'two': 2, 'three': 3, 'four': [1, 2, 3, 'FOUR', 5]}

# Nested Dictionaries
# orig_dic = {'one' : 1, 'two': 2, 'three': {'zero' : 0, 'one' : 1}, 'four' : 4}
#
# new_dic = copy.copy(orig_dic)

# print('Original: ', orig_dic)
# print('New: ', new_dic)
# Original:  {'one': 1, 'two': 2, 'three': {'zero': 0, 'one': 1}, 'four': 4}
# New:  {'one': 1, 'two': 2, 'three': {'zero': 0, 'one': 1}, 'four': 4}

# new_dic['three']['zero'] = 'ZERO'
# print('Original: ', orig_dic)
# print('New: ', new_dic)

# Original:  {'one': 1, 'two': 2, 'three': {'zero': 'ZERO', 'one': 1}, 'four': 4}
# New:  {'one': 1, 'two': 2, 'three': {'zero': 'ZERO', 'one': 1}, 'four': 4}

#
# orig_dict = {'one': 1, 'two': 2, 'three': {0,1,2}, 'four': 4}
# new_dict = copy.copy(orig_dict)
# print("Original: ", orig_dict)
# print("New: ", new_dict)

# Original:  {'one': 1, 'two': 2, 'three': {0, 1, 2}, 'four': 4}
# New:  {'one': 1, 'two': 2, 'three': {0, 1, 2}, 'four': 4}

# new_dict['three'].add(3)
# print("Original: ", orig_dict)
# print("New: ", new_dict)

# Original:  {'one': 1, 'two': 2, 'three': {0, 1, 2, 3}, 'four': 4}
# New:  {'one': 1, 'two': 2, 'three': {0, 1, 2, 3}, 'four': 4}

# Nested complex datatypes are not deep copies

# Dictionary DEep Copies
# months = {'jan':1, 'feb':2, 'mar':3, 'apr':4}
# new_months = months.copy()

# print("Months: ", months)
# print("New Months: ", new_months)

# Months:  {'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4}
# New Months:  {'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4}

# new_months['feb'] = 'FEB'
# print("Months: ", months)
# print("New Months: ", new_months)

# Months:  {'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4}
# New Months:  {'jan': 1, 'feb': 'FEB', 'mar': 3, 'apr': 4}
# for a simple dictionary(without any nested elements), dict.copy() function creates the deep copy

# import copy
# employees = {'Alison': 2007, 'Bart': 2008, 'Cathy': 2009, 'Dan': 2010}
#
# employees_copy = copy.deepcopy(employees)
# print("original: ", employees)
# print("new: ", employees_copy)

# original:  {'Alison': 2007, 'Bart': 2008, 'Cathy': 2009, 'Dan': 2010}
# new:  {'Alison': 2007, 'Bart': 2008, 'Cathy': 2009, 'Dan': 2010}

# employees['Alison'] = 2011
#
# print("original: ", employees)
# print("new: ", employees_copy)

# original:  {'Alison': 2011, 'Bart': 2008, 'Cathy': 2009, 'Dan': 2010}
# new:  {'Alison': 2007, 'Bart': 2008, 'Cathy': 2009, 'Dan': 2010}
# It created the deep copy here

# NESTED Dictionary copy

import copy
#
# orig_dic = {'one': 1, 'two': 2, 'three': 3, 'four': [1,2,3,4.0]}
# new_dic = copy.deepcopy(orig_dic)

# print("Original: ", orig_dic)
# print("NEW: ", new_dic)

# Original:  {'one': 1, 'two': 2, 'three': 3, 'four': [1, 2, 3, 4.0]}
# NEW:  {'one': 1, 'two': 2, 'three': 3, 'four': [1, 2, 3, 4.0]}

# print(new_dic['four'][3]) #4.0
#
# new_dic['four'][3] = 'FOUR'

# print("Original: ", orig_dic)
# print("NEW: ", new_dic)

# Original:  {'one': 1, 'two': 2, 'three': 3, 'four': [1, 2, 3, 4.0]}
# NEW:  {'one': 1, 'two': 2, 'three': 3, 'four': [1, 2, 3, 'FOUR']}
# changes made to the new_dic does not change original when copy created using the copy.deepcopy()

# new_dic['four'].append(5)
#
# print("Original: ", orig_dic)
# print("NEW: ", new_dic)

# Original:  {'one': 1, 'two': 2, 'three': 3, 'four': [1, 2, 3, 4.0]}
# NEW:  {'one': 1, 'two': 2, 'three': 3, 'four': [1, 2, 3, 'FOUR', 5]}
# # changes made to the new_dic does not change original when copy created using the copy.deepcopy()


# orig_dict = {'one' : 1, 'two': 2, 'three': {'zero' : 0, 'one' : 1}, 'four' : 4}
#
# new_dict = copy.deepcopy(orig_dict)

# print("Original: ", orig_dict)
# print("New: ", new_dict)

# Original:  {'one': 1, 'two': 2, 'three': {'zero': 0, 'one': 1}, 'four': 4}
# New:  {'one': 1, 'two': 2, 'three': {'zero': 0, 'one': 1}, 'four': 4}

# new_dict['three']['zero'] = 'ZERO '
#
# print("Original: ", orig_dict)
# print("New: ", new_dict)

# Original:  {'one': 1, 'two': 2, 'three': {'zero': 0, 'one': 1}, 'four': 4}
# New:  {'one': 1, 'two': 2, 'three': {'zero': 'ZERO ', 'one': 1}, 'four': 4}

# whole dict is a deep copy

#
# orig_dict = {'one': 1, 'two': 2, 'three': {0,1,2}, 'four': 4}
# new_dict = copy.deepcopy(orig_dict)
#

# print("Original: ", orig_dict)
# print("New: ", new_dict)

# Original:  {'one': 1, 'two': 2, 'three': {0, 1, 2}, 'four': 4}
# New:  {'one': 1, 'two': 2, 'three': {0, 1, 2}, 'four': 4}

# new_dict['three'].add('THREE')
#
# print("Original: ", orig_dict)
# print("New: ", new_dict)

# Original:  {'one': 1, 'two': 2, 'three': {0, 1, 2}, 'four': 4}
# New:  {'one': 1, 'two': 2, 'three': {0, 1, 2, 'THREE'}, 'four': 4}

# even the nested elements are the deep copy



# SETS
# set1 = {'c++', 'php', 'java', 'python'}
# set2 = set1
# print("Original SET: ", set1)
# print("NEW SET: ", set2)

# Original SET:  {'c++', 'java', 'php', 'python'}
# NEW SET:  {'c++', 'java', 'php', 'python'}

# set2.add('sql')

# print("Original SET: ", set1)
# print("NEW SET: ", set2)

# Original SET:  {'php', 'c++', 'python', 'java', 'sql'}
# NEW SET:  {'php', 'c++', 'python', 'java', 'sql'}
# SHALLOW copy is created because they both are pointing to the same set

# set2.pop() #it pops out some unknown element from set

# print("Original SET: ", set1)
# print("NEW SET: ", set2)

# Original SET:  {'sql', 'java', 'php', 'c++'}
# NEW SET:  {'sql', 'java', 'php', 'c++'}
# It pops the 'python' element and its reflected in both the variables

# sets are not accessble through indexing coz they are not intrinsically ordered
# Example
# set2[2] = 'RUBY'
# You get the following error
# TypeError: 'set' object does not support item assignment


# sets also cannot store nested list inside of it, only immutable data structures can be stored in the sets,
# you can store nested tuple but not lists as lists are immutable
# set1 = {'c++', 'php', ('java', 'c#'), 'python'} #this is possible
# set1 = {'c++', 'php', ['java', 'c#'], 'python'} #this is impossible #TypeError: unhashable type: 'list' #shows this error


import copy

# teachers_set = {'Ava', "Mia", 'Jacob', 'Daniel'}
# new_teachers_set = copy.copy(teachers_set)

# print("Original: ", teachers_set)
# print("New: ", new_teachers_set)
# Original:  {'Ava', 'Mia', 'Jacob', 'Daniel'}
# New:  {'Ava', 'Mia', 'Jacob', 'Daniel'}

# teachers_set.add('Emma') #new element only present in the teachers_set
# print(teachers_set) # {'Jacob', 'Mia', 'Emma', 'Ava', 'Daniel'}
#
# print("Original: ", teachers_set)
# print("New: ", new_teachers_set)

# Original:  {'Ava', 'Mia', 'Emma', 'Daniel', 'Jacob'}
# New:  {'Ava', 'Mia', 'Jacob', 'Daniel'}

# new_teachers_set.remove('Ava')
#
# print("Original: ", teachers_set)
# print("New: ", new_teachers_set)

# Original:  {'Daniel', 'Ava', 'Mia', 'Jacob'}
# New:  {'Daniel', 'Mia', 'Jacob'}

# the copy made using the copy.copy(), change made in original does not change the copy and vica versa


# teachers_set = {'Ava', "Mia", 'Jacob', 'Daniel'}
# new_teachers_set = copy.deepcopy(teachers_set)

# print("Original: ", teachers_set)
# print("New: ", new_teachers_set)

# teachers_set.add('Emma')

# print("Original: ", teachers_set)
# print("New: ", new_teachers_set)

# Original:  {'Emma', 'Ava', 'Daniel', 'Mia', 'Jacob'}
# New:  {'Mia', 'Ava', 'Daniel', 'Jacob'}

# new_teachers_set.remove('Ava')
#
# print("Original: ", teachers_set)
# print("New: ", new_teachers_set)

# Original:  {'Jacob', 'Daniel', 'Mia', 'Ava', 'Emma'}
# New:  {'Jacob', 'Daniel', 'Mia'}


# Important points
# 1. Shallow copies are made whenever two variables are pointing to the same location in memory
# which results in, updation of one variable are reflected onto the other
# The same complex datatypes has just two names i.e. the two variables

# 2. Deep copies are made when the variabls is copied to the entirely- new different memory location
# changes made to the deep copy are not reflected to the original memory

# 3. string copies
# strings are immutable in python, once created strings cannot be updated
# using assignment operators, strings reference the same memory location, but that location cannot be unchanged
# assigning a new string to a variable just created a new variable


# 4. List COPY
# list_b = list_a #this creates a shallow copy
# list_b = list_a[:] #this creates a deep copy
# list_b = copy.copy(list_a) #this creates a deep copy of the outer list but a shallow copy of the any nested complex data types
# list_b = copy.deepcopy(list_a) #this creates a deep copy of the outer list and all of the nested complex data types




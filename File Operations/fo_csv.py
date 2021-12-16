import csv

# file = open('record.csv', 'r')
# with file:
#     read = csv.reader(file)
#
#     for row in read:
#         print(row)

# ['Region', 'Country', 'Capital']
# ['Asia', 'Kyrgyzstan', 'Bishkek']
# ['Central America', 'Honduras', 'Tegucigalpa']
# ['Europe', 'Bulgaria', 'Sofia']
# ['Sub-Saharan Africa', 'Cameroon', ' Yaounde']


# file = open('record_pipe.csv', 'r')
# with file:
#     read = csv.reader(file)
#
#     for row in read:
#         print(row)

# ['Region|Country|Capital']
# ['Asia|Kyrgyzstan|Bishkek']
# ['Central America|Honduras|Tegucigalpa']
# ['Europe|Bulgaria|Sofia']
# ['Sub-Saharan Africa|Cameroon|Yaounde']

# While we are reading the csv file, it only knows by default that comma is the delimiter, so in file with delimiter as '|' symbol it didn't
# recognized the other file but it just treats the whole line is single string, so use the delimiter property in order to  identify the other symbols


# file = open('record_pipe.csv', 'r')
# with file:
#     reader = csv.reader(file, delimiter = '|')
#
#     for row in reader:
#         print(row)

# ['Region', 'Country', 'Capital']
# ['Asia', 'Kyrgyzstan', 'Bishkek']
# ['Central America', 'Honduras', 'Tegucigalpa']
# ['Europe', 'Bulgaria', 'Sofia']
# ['Sub-Saharan Africa', 'Cameroon', 'Yaounde']

# file = open('record_tab.csv', 'r')
# with file:
#     reader = csv.reader(file, delimiter = "\t")
#
#     for row in reader:
#         print(row)

# make sure the file is properly tab-spaced
# ['Region', 'Country', 'Capital']
# ['Asia', 'Kyrgyzstan', 'Bishkek']
# ['Central America', 'Honduras', 'Tegucigalpa']
# ['Europe', 'Bulgaria', 'Sofia']
# ['Sub-Saharan Africa', 'Cameroon', 'Yaounde']

# now elements are present as elements of list, you can access them by index, but if the amount of data is very large, it becmoes impossible to
# to remember indexes. So we call the csv file using the dictreader(), which returns a dictionary with keys being the csv header in row one and
# vealue the corresponding rows

#
# file = open('record.csv', 'r')
# with file:
#     read = csv.DictReader(file)
#
#     for row in read:
#         print(dict(row))

# {'Region': 'Asia', 'Country': 'Kyrgyzstan', 'Capital': 'Bishkek'}
# {'Region': 'Central America', 'Country': 'Honduras', 'Capital': 'Tegucigalpa'}
# {'Region': 'Europe', 'Country': 'Bulgaria', 'Capital': 'Sofia'}
# {'Region': 'Sub-Saharan Africa', 'Country': 'Cameroon', 'Capital': ' Yaounde'}



# file = open('record_tab.csv', 'r')
# with file:
#     read = csv.DictReader(file, delimiter='\t')
#
#     for row in read:
#         print(dict(row))

# {'Region': 'Asia', 'Country': 'Kyrgyzstan', 'Capital': 'Bishkek'}
# {'Region': 'Central America', 'Country': 'Honduras', 'Capital': 'Tegucigalpa'}
# {'Region': 'Europe', 'Country': 'Bulgaria', 'Capital': 'Sofia'}
# {'Region': 'Sub-Saharan Africa', 'Country': 'Cameroon', 'Capital': 'Yaounde'}


# file1 = open('record.csv', 'r')
# with file1:
#     reader = csv.DictReader(file1)
#     for row in reader:
#         print(row)


# converting the python objects into the csv contents

# for converting a python list into csv we use the writerow() and writerows() function
# names = [['FirstName', 'LastName'],
#          ['Shubham', 'Goyal'],
#          ['Anurag', 'Basu'],
#          ['Neelam', 'Shah']]
# file = open('names.csv', 'w')
# with file:
#     file_writer = csv.writer(file)
#     for row in names:
#         file_writer.writerow(row)

#output
# FirstName,LastName
#
# Shubham,Goyal
#
# Anurag,Basu
#
# Neelam,Shah
#
# nums = [[10,20,30],
#         [40,50,60],
#         [70,80,90]]
# file = open('numbers.csv', 'w')
# with file:
#     writer = csv.writer(file)
#     writer.writerows(nums)

# 10,20,30
#
# 40,50,60
#
# 70,80,90


# in order to convert a dictionary into a csv file, we first have to create a list for csv headers and then use writerow() for adding other value rows

# file = open('names1.csv', 'w')
# with file:
#     fnames = ['FirstName', 'LastName']
#     writer = csv.DictWriter(file, fieldnames=fnames)
#     writer.writeheader()
#     writer.writerow({'FirstName': 'Anjani', 'LastName': 'Dubey'})
#     writer.writerow({'FirstName': 'Shubham', 'LastName': 'Basu'})
#     writer.writerow({'FirstName': 'Dheeraj', 'LastName': 'Bajpayee'})

#     following content added to the file names1.txt
# FirstName,LastName
#
# Anjani,Dubey
#
# Shubham,Basu
#
# Dheeraj,Bajpayee


# CSV Dialects
# There can be different delimiters than the default ',' comma seperator for csv values, similarly there can be different line terminators or
# there can be different quote other than the double quotes, so here comes a pre-defined dialects for CSV
# There exists a different class known as register_dialects for identifying or setting the different delimiters, line terminators or quotes, etc.
# You can define your own dialect using this class 'register_dialect'

# So we first have to register a dialect and then make use of it for our csv files


# csv.register_dialect('tab', delimiter = '\t')
#
# with open('record_tab.csv', 'r') as file:
#     reader = csv.reader(file, dialect='tab')
#
#     for row in reader:
#         print(row)

# ['Region', 'Country', 'Capital']
# ['Asia', 'Kyrgyzstan', 'Bishkek']
# ['Central America', 'Honduras', 'Tegucigalpa']
# ['Europe', 'Bulgaria', 'Sofia']
# ['Sub-Saharan Africa', 'Cameroon', 'Yaounde']


# register another dialects
csv.register_dialect('plus', delimiter='+', lineterminator='\n\n\r')

names = [['FirstName', 'LastName'],
         ['Shubham', 'Goyal'],
         ['Anurag', 'Basu'],
         ['Neelam', 'Shah']]

file = open('names_dialect.csv', 'w')
with file:
    file_writer = csv.writer(file, dialect='plus')
    for row in names:
        file_writer.writerow(row)

# output on shell
# ['FirstName', 'LastName']
# ['Shubham', 'Goyal']
# ['Anurag', 'Basu']
# ['Neelam', 'Shah']

# the below content added to the file names_dialect.csv
# FirstName+LastName
#
#
# Shubham+Goyal
#
#
# Anurag+Basu
#
#
# Neelam+Shah


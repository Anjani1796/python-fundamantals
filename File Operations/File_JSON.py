# JSON - JavaScript Object Notation

import json
#
# car = """{"model":"civic",
#        "make":"Honda",
#        "variants": ["Sedan", "Coupe"]}"""

# print(car)
# {'model':'civic',
#        'make':'Honda',
#        'variants': ['Sedan', 'Coupe']}

# loads() function converts the string into python object
# car_dict = json.loads(car) #loads is short form of load string
# print(car_dict) #{'model': 'civic', 'make': 'Honda', 'variants': ['Sedan', 'Coupe']}

# print(type(car)) # <class 'str'>
# print(type(car_dict)) # <class 'dict'>

# with open('currency.json') as json_file:
# the load() function converts the json object into python object
#     data = json.load(json_file)
#     print(data)
#     {'Country': 'USA', 'Currency': 'United States Dollar'}

# always make use of "double quotes" and then create the json file for its objects

# currency = {
#   "Country": "India",
#   "Currency": "Indian Rupee"
# }

# dumps() function converts the python object into json
# json_var = json.dumps(currency)
# print(json_var)
# print(type(json_var)) #<class 'str'>
#
# with open('currency.json') as json_file:
#     data = json.load(json_file)
#     print(data)
#
# with open('currency.json', 'w') as json_file:
#     json_file.write(json_var)
# # this line will open the file in the write mode and then it will overwrite the existing contents of the file
#
# written_data = json.load(open('currency.json'))
# print(written_data)
# # {'Country': 'India', 'Currency': 'Indian Rupee'}

# dumps()- encoding to JSON objects
# dump()- encoded string writing on file
# loads()- Decode the JSON string
# load()- Decode while JSON file read



dessert = {
    "Name": "Ice-cream",
    "flavours": ["chocolate", "pineapple"],
    "Toppings": True,
    "Wafflecone": "Yes"
}

# dessert_str = json.dumps(dessert)
# this converts the python dictionary into string
# print(dessert_str)
# {"Name": "Ice-cream", "flavours": ["Chocolate", "Pineapple"], "Toppings": true, "Wafflecone": "Yes"}
# The "True" in python file is converted to 'true' in small letter because the inside json, the boolean value is represented as small letters 'true'

# print(type(dessert_str)) #<class 'str'>

# with open('eat.txt', 'w') as json_file:
#     json.dump(dessert, json_file)
#
# print(dessert)
# {'Name': 'Ice-cream', 'flavours': ['chocolate', 'pineapple'], 'Toppings': True, 'Wafflecone': 'Yes'}

print(json.dumps(dessert, indent=2))
# {
#   "Name": "Ice-cream",
#   "flavours": [
#     "chocolate",
#     "pineapple"
#   ],
#   "Toppings": true,
#   "Wafflecone": "Yes"
# }

print(json.dumps(dessert, separators=(':', '=')))
# {"Name"="Ice-cream":"flavours"=["chocolate":"pineapple"]:"Toppings"=true:"Wafflecone"="Yes"}

print(json.dumps(dessert, separators=('|', '~')))
# {"Name"~"Ice-cream"|"flavours"~["chocolate"|"pineapple"]|"Toppings"~true|"Wafflecone"~"Yes"}

print(json.dumps(dessert, sort_keys=True))
# {"Name": "Ice-cream", "Toppings": true, "Wafflecone": "Yes", "flavours": ["chocolate", "pineapple"]}

print(json.dumps(dessert, sort_keys=False))
# By default, the sort_keys keyword value is False
# {"Name": "Ice-cream", "flavours": ["chocolate", "pineapple"], "Toppings": true, "Wafflecone": "Yes"}
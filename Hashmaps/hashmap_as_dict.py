import pandas as pd
#Way1 to create a dictionary
my_dict = {'Dave':'001', 'Jane': '002', 'Matthew': '003'}
print(my_dict)
print(type(my_dict))
#Way2 to create a dictionary
new_dict = dict(Dave='001', Jane='002', Matthew='003')
print(new_dict)

#Nested Dictionaries
nested_dict = {'Employees':{'Dave': {'Age': '19', 'Gender': 'Male', 'Designation': 'Team Lead'},
                            'Jane': {'Age': '21', 'Gender': 'Female', 'Designation': 'Team Lead'},
                            'Matthew': {'Age': '23', 'Gender': 'Male', 'Designation': 'Team Lead'}
                            }}

#Accessing values using key values pairs
print(my_dict['Dave'])
print(my_dict.keys())
print(my_dict.values())
print(my_dict.get('Dave'))

for item in my_dict:
    print(item)
for item in my_dict.values():
    print(item)
for item in my_dict.items():
    print(item)

my_dict['Chris'] = '007'
print(my_dict)
my_dict.pop('Dave')
print(my_dict)

#Coverting a dictionary into a pandas dataframe
df = pd.DataFrame(nested_dict['Employees'])
print(df)
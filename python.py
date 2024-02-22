2.Sorting list of dictionaries: Given a list of dictionaries containing name and age keys, write a Python program to sort the list of dictionaries based on the age of the individuals

my_list=[ {'name':'jin', 'age':25},{'name':"tae", 'age': 17}, {'name': 'hope', 'age': 31} ]
sorted_list=sorted(my_list, key=lambda x: x['age'])
print(sorted_list)

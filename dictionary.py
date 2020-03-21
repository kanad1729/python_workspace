'''
Dictionary: A dictionary is a collection which is unordered, changeable and can't access using index. 
'''

#way 1: creating dictionary simple way

student = {'name': "Ram", 'age':12}

print(student['name'])

#using get method
print(student.get("age"))


#way 2: creating dictionary using dict() constructor

employee = dict(name='Raju', age=20)

print(employee)

#way 3: creating the dictionary
emp = {

	'name': 'rajiv',
	'age': 20,
	'timing': [10, 20, 30],

}

print(emp)


#adding data to empty dictionary by taking input

stud = {}

name, age = input("Enter name and age: ").split(" ")

stud["name"] = name
stud["age"] = age

print(stud)

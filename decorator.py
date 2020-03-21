'''
decorator is just way to decorate a function which means just add something new to existion fun or just enhancing capabilities of existing fun with some other fun i.e decorator here.

'''

#code to check candidate is valid or not by writing business logic into another function this calles a decorator.
'''
def decorator_func(funcParam):
	
	x = funcParam()
	def new_func():	
		
		print("before decoration")
		if(x>18):
			print("Cantidade is valid to voting")
		else:
			print("Cantidade is valid to voting")

		print("after decoration")
	return new_func

@decorator_func
def voting():
	
	age = 19
	print("inside func that to decorate")
	return age
	
	

voting() #calling a func to display output
'''
#writing multiple decorators


def validName(func):
	l = func()
	print(l)

	def nameValidator():
	
		'''name = l[0]
		print(name)
		if name.length>0:
			print("Name is valid")
		else:
			print("Name is not valid")'''

	return nameValidator

def validAgeAndSalary(func):
	
	l = list(func())
	print(l)
	
	
	def validator():

		if(l[1]>18 and l[2]>500):
			print("Valid to purchase")

		else:
			print("Not valid to purchse")
	
	return validator

@validAgeAndSalary
@validName
def mainFunc():
	age = 19
	salary = 1000
	name = "rusi"

	#here we can return multiple values from func using list, tuple, dict or object
	return [name, age, salary]

mainFunc()	

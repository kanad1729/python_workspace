'''
	map syntax ==> map(function, iterables)

	in map first parameter is fun and next param is iterable i.e list or tuple while cab be one list or more than one.

	Parameter     |Description
	--------------|---------------------------------------------------
	function      |Required. The function to execute for each item
	--------------|------------------------------------------------------
	iterable      |Required. A sequence, collection or an iterator object. You can send as many iterables as you like, just make sure the 				function has one parameter for each iterable.
'''


"""def myfunc(a, b):
  return a + b

x = map(myfunc, ['apple', 'banana', 'cherry'], ['orange', 'lemon', 'pineapple'])

print(x)

#convert the map into a list, for readability:
print(list(x))

"""
#using lambda fun

x = map(lambda x, y: x+y, [1,2,5,7],[2,3,4,5])
print(x) #map func will return iterator object

#now conver to list

print(list(x))

#or just print in one line

x = list(map(lambda x: x**2,  [1,2,5,7]))

print(x)

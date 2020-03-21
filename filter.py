'''
	filter() function:

	    -The filter() function returns an iterator were the items are filtered through a function to test if the item is accepted or not.
	    - filter is a function in  python which used to filter data like in forrm of sequence by passing to some fun.	
	syntax:
		
		filter(function, iterable)
		
		Parameter	Description
		function	A Function to be run for each item in the iterable
		iterable	The iterable to be filtered		
'''
#filter using normal func.

'''ages = [5, 12, 17, 18, 24, 32]

def myFunc(x):
  if x < 18:
    return False
  else:
    return True

adults = filter(myFunc, ages)

for x in adults:
  print(x)
'''
#filter with lambda func.

out = filter(lambda x: x>18, [5, 12, 17, 18, 24, 32])
print(out) #this will print filter as object and it's present at some address
print(list(out)) #conversion to list type

#in one line
print(tuple(filter(lambda x: x>18, [5, 12, 17, 18, 24, 32])))

#or u can print using this also
output = filter(lambda x: x>18, [5, 12, 17, 18, 24, 32])
for i in output:
	print(i)

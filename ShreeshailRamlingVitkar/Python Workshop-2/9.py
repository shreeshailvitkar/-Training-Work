# A generator function that yields 1 for first time,
# 2 second time and 3 third time
def simpleGeneratorFun():
    value = 1
    result = value**2
    yield result
    result = (value+1)**2
    yield result
    result = (value+2)**2
    yield result
    result = (value+3)**2
    yield result
    result = (value+4)**2
    yield result
    result = (value+5)**2
    yield result
    result = (value+6)**2
    yield result
    result = (value+7)**2
    yield result
    value = (value+8)**2
    yield value
    value = (value+9)**2
    yield value
    result = (value+10)**2
    yield result
	
	
    		

# Driver code to check above generator function
for value in simpleGeneratorFun():
	print(value)
    

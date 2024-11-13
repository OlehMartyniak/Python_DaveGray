#  lambda function is a single expression that returns a value
# lambda is an anonymous function but it can be assigned to a variable

squared = lambda num : num * num

print(squared(3)) # 9

# lambda can accept multiple values

sum = lambda a,b : a + b

print(sum(2,4)) # 6

##################

def funcBuilder(x):
    return lambda num: num + x

addTen = funcBuilder(10)
addTwenty = funcBuilder(20)

print(addTen(7)) # 17
print(addTwenty(7)) # 27


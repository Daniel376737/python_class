numbers={1,2,3,4}
print(numbers)
print(type(numbers))
print (1 in numbers)
#adding a simngle item 
numbers.add("mexico")
print(numbers)

#adding multiple items
numbers.update([500,600,700])
print(numbers)

#removng items from a set
numbers.remove(4)
print(numbers)

numbers.clear()
print(numbers)


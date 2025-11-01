list=[]
for i in range(1,51):
    list.append(i)
print (list)

list2=[] 

for i in list:
    if i%7 ==0 or i%5 ==0:
        list2.append(i)
print (list2)


#4
odd_numbers =[]
for i in range(10,51):
    if i%2 != 0:
        odd_numbers.append(i)
        if len(odd_numbers) == 10:
            break
print(odd_numbers)

first_ten=odd_numbers[0:10]
print(first_ten)

#no5
number = float(input("Enter a number: "))

for i in range(1,11):
    print(f"{number}x{i}={number*i}")


#loop in a
    for i in range(3):
        for j in range(2):
            print(i,j)



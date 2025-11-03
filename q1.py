 #Using Python or PHP or Java or Ruby or JavaScript
#Write a program that prompts the user to enter the base and height of a triangle and returns its area.

height=(input("enter the height of triangle"))
base=(input("enter the base of triangle"))
area= base * height 
print("area of triangle")


# Hint: how does an even / odd number react differently when divided by 2?
 #Using Python or PHP or Java or Ruby or JavaScript
#Prompt the user for a number either on a form input or the terminal. Depending 
# on whether the number is even or odd, display  either “odd” or “even” to the user.
 #Hint: how does an even / odd number react differently when divided by 2?

number = (input("enter number: "))
if number % 2 == 0:
    print("even")
else:
    print("odd")

#Extras:
#If the number is a multiple of 4, print out “divisible by 4”.
number=input("enter a number: ")
if number % 4 == 0:
    print("divisible by 4")

#Write a program which gets a phone number from a form input or terminal. 
# Validates the phone number by checking if it starts with +254.. or 07.. or 7…
#  or 254.. or 01... or  1.. Convert the number to start with +254… 
#e.g if a user enters “0712345678”, the program should display “+254712345678”
#e.g if a user enters “0112345678”, the program should display “+254112345678”
#e.g if a user enters “712345678”, the program should display “+254712345678”

#Write a program which accepts email as form input or from terminal.
#  Validate the email by checking if it's a valid email. 
#Hint: Check if it contains an “@” symbol and “.” symbol.

email= input("enter your email address: ")
if "@" & "." in email:
    print("valid email")
else:
    print("invalid email")

#Implement a program that takes 3 users  inputs from the terminal or the Browser,
#  and stores them in three variables. Return the largest of the three. Do this 
# without using the the inbuilt max () function!
#The goal of this exercise is to think about some internals that programs normally
#  take care of for us.
y=input("enter" "y")
x=input("enter" "x")
z=input("enter" "z")
if y>=x and y>=z:
    large=z
elif x>=y and x>=z:
    large=x
else:
    large=z





#TASK 6:Using Python or PHP or Java or Ruby or JavaScript
#Write a program that lets the user input a password. Give them only 4 attempts 
#to check the passwords entered against “admin@123”. If the password is correct 
#access is granted. After you show them a message , the account is blocked.

password="admin@123"
attempts_entered=4
if password==attempts_entered:
    print("password is correct access granted")
elif attempts_entered>password:
    print("incorrect password")
else:
    print("account bloced")

#Write that prompts the user to input student marks. The input should be between 
#0 and 100.Then output the correct grade: 
#A > 79 , B - 60 to 79, C  > 49 to 59, D - 40 to 49, E - less 40

marks=input("enter student marks(0-100):")
if marks < 0 or marks > 100:
    print("invalid marks")
elif marks > 79:
    grade="A"
elif marks>=60:
    prade="B"
elif marks>=50:
    grade="C"
elif marks >=40:
    grade="D"
else: 
    grade="E"
print("the grade is: ")


#TASK 8: Using Python or PHP or Java or Ruby or JavaScript
##Write a program that takes as input the speed of a car e.g 80. If the speed is 
#less than 70, it should print “Ok”. Otherwise, for every 5 km/s above the speed 
#limit (70), it should give the driver one demerit point and print the total 
#number of demerit points.
#For example, if the speed is 80, it should print: “Points: 2”. If the driver 
#gets more than 12 points, the function should print: “License suspended”.

speed_limit=70
if speed_limit <= ("70 km/h"):
    print("ok")





#TASK 9: Using Python or PHP or Java or Ruby or JavaScript
#Write a program called stars. It should prompt the user for a number, and it should print the number of stars till the number entered.
#Example If rows is 5, it should print the following:
#*
#**
#***
#****
#*****.....
stars = int(input("enter number of stars:"))

for i in range(5, stars + 1):
    print(stars*i)

#TASK 10: Using Python or PHP or Java or Ruby or JavaScript
#Write a program that calculates the total stock in a company from the array/list 
#below if we know that the stock is the last digit in every array/list.

#prods = [[‘omo’,’30kshs’,’300’], [‘milk’,’50kshs’,’200’],[‘bread’,’45kshs’,’359’]
#                                  , [‘coffee’,’5kshs’,’79’]]

#NB: ONCE YOU COPY AND PASTE THE LIST ABOVE,REWRITE THE SINGLE QUOTES AS THE 
#ABOVE LIST WILL GIVE YOU AN ERROR



#TASK 11: Using Python or PHP or Java or Ruby or JavaScript
#Write a program that takes the date of birth of a person and the program outputs 
#the age in terms of years,months,days TODAY.datetime

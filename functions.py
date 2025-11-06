
#global variable
a= 4
b= 5
c= a + b

def add_numbers():
    #local variable
    a=4
    b=5
    c= a+b

#tsk q 1, 2, 5 & 70

#Q1 Using Python or PHP or Java or Ruby or JavaScript
#Write a program that prompts the user to enter the base and height of a triangle 
#and returns its area.

base=float(input("enter the base: "))
height=float(input("enter the height: "))

def get_area(a,b):
    return 0.5*a*b
area1=get_area(base,height)

# Using Python or PHP or Java or Ruby or JavaScript
#Prompt the user for a number either on a form input or the terminal. 
#Depending on whether the number is even or odd, display  either “odd” or “even” to the user.
# Hint: how does an even / odd number react differently when divided by 2?

def even_old(x):
    if x % 2 == 0:
        return "even"
    else:
        return "old"
x = int(input("enter a number: "))

print(f"{(even_old(x))}.")


#Q5 Using Python or PHP or Java or Ruby or JavaScript
#Implement a program that takes 3 users  inputs from the terminal or the 
#Browser, and stores them in three variables. Return the largest of the three. 
#Do this without using the the inbuilt max () function!
#The goal of this exercise is to think about some internals that programs normally 
#take care of for us. 

def largest_number(x,y,z):
    largest = x
    if y > largest:
        largest=y
    if z > largest:
        largest=z
    return largest
x = float(input("enter x: "))
y = float(input("enter y: "))
z = float(input("enter z: "))

print("the largest number is:",largest_number(x,y,z))


#Q15 Using Python or PHP or Java or Ruby or JavaScript
#Write a program that takes input of someone's basic salary and benefits, 
#adds them to find the gross salary then uses  the gross salary to find the NHIF. 
#To find the Kenya NHIF Rate using THIS LINK:  

def nhif_contribution(gross_salary):
    if gross_salary<= 5999:
        return 150
    elif gross_salary<=7999:
        return 300
    elif gross_salary<=11999:
        return 400
    elif gross_salary<=14999:
        return 500
    elif gross_salary<=19999:
        return 600
    elif gross_salary<=24999:
        return 750
    elif gross_salary<=29999:
        return 850
    elif gross_salary<=34999:
        return 900
    elif gross_salary<=39999:
        return 950
    elif gross_salary<=44999:
        return 1000
    elif gross_salary<=49999:
        return 1100
    elif gross_salary<=59999:
        return 1200
    elif gross_salary<=69999:
        return 1300
    elif gross_salary<=79999:
        return 1400
    elif gross_salary<=89999:
        return 1500
    elif gross_salary<=99999:
        return 1600
    else:
        return 1700
    
def gross_salary(basic_salary,benefits):
    return basic_salary+benefits

    nhif=nhif_contribution(gross_salary)
    print(f"gross salary: {gross_salary: }")
    print(f"nhif deduction:{nhif}")



 

#Q16 Using Python or PHP or Java or Ruby or JavaScript
#Continue with the program above, then use  the gross salary to find the NSSF. 
#To find the Kenya NSSF Rate  using 6% of the Gross Salary. BUT ONLY A MINIMUM 
#OF 18,000 Gross Salary CAN BE USED IN NSSF.

def get_nssf(gross_salary):
    if gross_salary > 80000:
       get_nssf =("6%,100*18000")
    else:
        get_nssf = 0.06 * gross_salary
print(f"nssf: ")


 #@17 Using Python or PHP or Java or Ruby or JavaScript
#Continue with the same program and calculate an individual’s NHDF using:
# i.e NHDF = gross_salary *  0.015

def calculate_nhdf(gross_salary):
    return gross_salary * 0.015
gross_salary=float(input("enter gross salary: "))
print(f"nhdf deduction: ")
 #Q18 Using Python or PHP or Java or Ruby or JavaScript
#Calculate the taxable income.
#i.e taxable_income = gross salary - (NSSF + NHDF + NHIF) 

def calculate_taxable_income(gross_salary,nssf,nhdf,nhif):
    taxable_income=gross_salary-(nssf+nhdf+nhif)
    return taxable_income
gross_salary=float(input("enter gross salary: "))
nssf=float(input("enter nssf amount: "))
nhdf=float(input("enter nhdf amount: "))
nhif=float(input("enter nhif amount: "))
print(f"taxable income: ")

#Q19 Using Python or PHP or Java or Ruby or JavaScript
#Continue with the same program and find the person's PAYEE 
#using the taxable income above.
#Find the Kenya PAYEE Tax Rate using THIS LINK

def find_payee(taxable_income):
     personal_relief=2400.00

start_date='2024-01-01'
end_date='2024-12-31'  

month1=float(start_date[5:7])
month2=float(end_date[5:7])

date1=start_date[8:10]
date2=end_date[8:10]

if month1>month2:
    print("valid period")
elif month1==month2 and date1==date2:
    print("one day period")
else:
    print("invalid period")


    if start_date>end_date:
        print("valid period")
    elif start_date==end_date:
        print("one day period")
    else:
        print("invalid period")

"------------------------------------------------------------------------------------------------------------------"
"-----------------------------------------------------------------------------------------------"
  


amount=float(input("enter amount:"))
account_type=("enter account type:")

if account_type=="standard":
    if amount > 500:
        print("transaction exceeds the limit for standard accounts.")
    else:
        print("transaction approved")

elif account_type=="premium":
    if amount>1000:
        print("transaction exceeds the limit for premium accounts.")
    else:
        print("transaction approved")
else:
    print("invalid account type")

    "--------------------------------------------------------------------------------------------------------"
    "''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''"


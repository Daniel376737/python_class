items=["mary",12.856,True,108,"this is the last item"]
print(items)
print(type(items))
print(items[3])

values=[1,2,3,[4,5,6],[7,8,9],10]
values.append(100)
print(values)



#count -returns the number if ocurances in a list
#sort- sorts a list in asending order  by default
#reverse-change order of a list-from the last item to first
#max-finds the largest value in alist / #min finds the smallest vale in a list
#index-this returns the position if an element -first ocurrence 
#copy -makes a copy a list 
#joining list-concantination,extension 

#TUPLES-a data structure used to hold multiple values that cant be changed or moved
##represented using normal brackets ()

#properties of tuples
#they are odered -use indexing to acces/oder items
#they are imutable
#how to update a turple? adding/ removing /changing items in a turple
#converting a turple to list to manipulate then convert back  to turple

#sets-->a collecation of unique , unodered items.--represented using curly braces {}


#tuple
days=("Monday","Tuesday","Wednesday","Thursday")
print(days)
print(type(days))
 
print(len(days))
print(days.index("Thursday"))

print(days.count("Thursday"))

print(days[1])
print(days[-1]) 
person={
    "name":"alice",
    "age":24,
    "married":False,
    "address":"123 kimathi st",
    "friends":["john"]
}
print(person)
print(type(person))

#bracket notation to access values 
print(person["name"])
print(person["friends"])

#another method of accessing values
print(person.get("address"))

#add a new ke-value pair
person['id']=345243
print(person)
person['dob']='17/10/1995'
print(person)
 
#reassing values
person['name']="jack"
print(person)
#update multiple keys
person.update({"name":"alice","age":30})
print (person)

#removing items(pop)

person.pop("age")
print(person)

#popitem removes the last item
person.popitem()
print(person)




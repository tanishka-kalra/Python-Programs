#Dictionary is data type that store data in the form of key: value pair . It  is mutuable
#Created by placeing elements in sequence within curly braces , separated by comma.


#empty dict
my_dict = {}
print(type(my_dict))

#dict with key and values
dt= {
'First_name':"Tanishka",
"Last_name":"Kalra",
"Age": 21
}
print(dt)

#inserting new key value pair
dt["Branch"]='CSIT'
print(dt)

#updating values w.r.t key
dt["Age"]= 22
print(dt)



#tuple is a sequence data type which allows storing elements in sequential manner enclosed within paranthesis sperated by commas .
#It is immutable . hence we can't modify the defined tuple.

#empty tuple
var = ()

#tuple with single value
var = (1,)
var1 = (1)
print(type(var)) #gives type "tuple" 
print(type(var1)) #gives type "int"
# var.append("2")--> gives an error

del var #deleting a tuple

# converting a list to tuple
list1=[1,2,3,4,5]
print(type(list1))

tuple1= tuple(list1) #list is converted to tuple using tuple function
print(type(tuple1))

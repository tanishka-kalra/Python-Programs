#List is a sequence data type which allows to store the data in a sequential manner enclosed within square brackets.
# It is mutable and allows duplicates.

#empty list
my_list = []

#list storing numbers
my_list1=[1,2,3,4,5]

#list with mixed type of values 
my_list2=[1,2,3,"hello",5,6,"bye"]

#adding elements at the end of the list
my_list.append("1")
my_list.append("2")
print("The list has a length of : ", len(my_list)) #used to find the length of the list

#inserting an element at specific position
my_list.insert(1,"0")
my_list.insert(2,"4")
my_list.insert(9,"7") #entering index out of range ,inserts the element at the end
my_list.insert(-1,"7") # entering negative index , inserts the element at the end
print("List have elements : " ,my_list)
last_value = my_list.pop() #removes and returnes the last value from the list
print("The last element popped out is :" , last_value)
my_list.remove("7") # removes the given object from the list(first occurence)
my_list.sort() # sort the list
print("The List in sorted Order :",my_list)
print(my_list.reverse()) # reverse the list
print("The list in reverse order :", my_list)

my_list.extend(my_list1)  #add items of an iterable at the end of the list
print("The extend list :", my_list)



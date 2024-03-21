from string import Template
a=10
b=20
c=a+b
print("Total of", a, "and", b ,"is", c )
#formating using % operator
print("Total of %d and %d is %d"%(a,b,c))

#formating using format function 
print("Total of {} and {} is {}".format(a,b,c))

#formating using string literals
print(f"Total of {a} and {b} is {c}")

#formating using string Template 
x = Template("Total of $p and $q is $s")
print(x.substitute(p=a,q=b,s=c))

# string = "A sentence"
# integers = 99
# floats = 3.14
# list = ["Item 1", floats, integers]
# tuple = ("Item 1", "Item 2", "Item 3")
# sets = {"Item1", "Item2", "item 3"}
# dictionary = {
#     "key": "value",
#     "key2":"value2",
# }
# booleans =True
# none=None

# x is variable and 10 value is stored in x variable
x=10
print(type(x))

# x is variable and 1.5 value is stored in x variablex=10
x=1.5
print(type(x))

# x is variable and 10 value is stored in x variablex=10 and we divided x value with 3
x=10
x=10/3
print(x)

# x is variable and punee value is stored in x variable
x="punee"
print(type(x))

x=[10,"punee"]
print(type(x))

x1=20
print(x1)

x_1=25
print(x_1)

x=10
y=20
z=30
x,y,z=10,20,30
print(x+y+z)


x,y,z=10.2,20.4,30.5
print(x+y+z)


# concatenating string
x="lucky"
y=x+" is awesome"
print(x)
print("Hello "+x)
print(y)

x="lucky"
x=x.upper()
x=x.lower()

x="lucky warriors"
z=x.split()
print(type(z))
print(z)

x="lucky warriors"
z=x.split('r')
print(type(z))
print(z)
print(x[0])
print(x[-1])
print(x[12])
print(len(x))
# above print on indexing, index start with 0 and space also count.
#it stats from forward direction.when we give negative values to start from backward direction.
# x[start:stop:step]start means where we want to start. start is the starting point. stop is the ending point.
#step is after leaving how much gap you want to. starting point starts on the place/index which we give but it stops the index before. for example, 
#we want to stop at index 5 but we need to give index 6. 
x=x[2:6]
print(x)
x="lucky warriors"
x=x[2:]
#it starts from the second index and take until last index
print(x)
x="lucky warriors"
x=x[1:4]
print(x)

x="lucky warriors"
x=x[1: : 2]
print(x)
#it is sticking for the last value through the steps. we give 2 steps. skipping print one letter and skip next letter



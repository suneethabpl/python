# in function, write code once and use it whereever we want means reusable
# in java script 
# function functionName(){

# }

def somename():
    print("Hello world")

somename()

name="punee"
def functionname():
    print(f"Hello {name}")

functionname()

# note--define a function, and then we execute the function and that parameter in here, 
# now this name is available inside of the function. 
def functionName(name):
    print(f"Hello {name}")
functionName('punee')

def functionName(name, food):
    print(f"Hello {name}. Let's eat some {food}")
functionName('punee','pizza')

def functionName(name, food="pizza"):
    if name.lower() == "punee":
        print("Welcome punee")
    print(f"Hello {name}. Let's eat some {food}")
functionName('lucky', food='oranges')
      
def functionName(name=None, food="pizza"):
    if name is None:
        name = "punee"
    print(f"Hello {name}. Let's eat some {food}")
functionName()
        # note-- every function returns false by default in python.

def somefunction():
    return "a value"
thing = somefunction()
print(thing)

def exp(num1,num2):
    total = num1 ** num2
    return total
big_number = exp(4,2)
print(big_number)

def myfunc():
    name = "punee"
    return name
myfunc()
print(name)

name = "punee"
def myfunc():
    return name
myfunc()
print(name)

name = "punee"
def myfunc():
    # name = "New name"
    return name
print(myfunc())
print(name)

# note--whenever we see a name error that a particular variable is not defined, chances are it's just outside 
# of the scope and we have to make it accessible somehow. 


# name = "punee"
# def myfunc(name):
#     # name = "New name"
#     return name
# print(myfunc())
# print(name)

def function_1():
    print("Hello world")
function_1()

#aguments/parameter--pass the values inside of teh function.here we pass name and then we concatenation. 
def function_1(name):
    print("Hello "+name)
function_1("moverick")

# parameter argument r a little different
# above name is parameter.
# and moverick is arguments. 
# parameter is whatever we r writing inside of paraenthisis and finding the function.
# arguments is whatever we r passing the parameters. 

# def function_1(name):
#     print("Hello "+name)
# function_1("moverick",'yash') #we got errore like this TypeError: function_1() takes 1 positional argument but 2 were given

def function_1(name_1,name_2):
    print("Hello "+name_1+" and "+name_2)
function_1('moverick','Yash')


# sometimes we don't know how many arguments of the possibly created are arbitrary paramter like *name. 
def function_1(*name):
    print("Hello "+name[0]+" and "+name[1])
function_1('moverick','Yash')

def function_1(name_1,name_2="Yash"):  # this name_2="Yash" default value. it is used when we are not passed argumenet to name_2 only.
    print("Hello "+name_1+" and "+name_2) # it accept default value when argument is not passesd
function_1('maverick')

def function_1(name_1,name_2="Yash"):  # this name_2="Yash" default value. here we give argument harsh to name_2 so it does not print default value.
    print("Hello "+name_1+" and "+name_2)
function_1('maverick','harsh')

# whatever the variables we create inside of a function are called us local variables. this local variable limits inside of teh function.
def function_1(name_1,name_2="Yash"): 
   y="Hello "+name_1+" and "+name_2
   print(y) #local variable
function_1('maverick','harsh')

# def function_1(name_1,name_2="Yash"): 
#    y="Hello "+name_1+" and "+name_2
# function_1('maverick','harsh')
# print(y) #global variable so here error is NameError: name 'y' is not defined

def function_1(name_1,name_2="Yash"): 
   return "Hello "+name_1+" and "+name_2
str_1=function_1('maverick','harsh')
print(str_1)
#return is returning the value of the function in the main programm. 

#name of function must be small letters.
def add(n1,n2):
    return n1+n2
sum=add(1,2)
print(sum)

#name of function must be small letters.
def add(n1,n2):
    return n1+n2
sum=add(20,40)
print(sum)


#here we use recursion concept means doing something again and again in a loop.
#recursion=call function inside of the function
#sume of first 10 integers are 55.

def sum(n):
    if n==1:
        return 1 #stopping point.
    else:
        return n+sum(n-1)
sum_1=sum(10)
print(sum_1)
#here we call a function inside of the function. that function is also be called inside a function again and again until we put some kind of break point. 
#here if is breaking point. 
#here we call n and give n value 10.   return 1 #stopping point.if we don't give stopping point, it will keep on running.if n==1 then it has to come back out of teh loop. 
#return n+sum(n-1) here n value is 10 but it couldn't return it because there is a sum function. again it went inside of function.
#there was an outer function which is def sum(n): if n==1: return 1 #stopping point.else: return n+sum(n-1) then function is called and then it created its own like a virtual function 
#and went again inside of the function. now there r 2 functions running. one is outer function and same function is running inside of teh function. 
#return n+sum(n-1)here n is 10 and sum(9) and then 9 is again went to sum(n) later if(9==1) it is false. it again comes back to return n+sum(n-1). now n is 9 . means 10+9+sum(n-1) this time 9-1 is 8.
#again it went to sum(8), if(9==1)then it is false so come lese path. return n+sum(n-1) now 10+9+8+sum(n-1) so on so on until 10+9+8+7+6+5+4+3+2+sum(n-1); this time sum(2-1) is 1. def sum(1)
# then if(1==1) so return  1 so 10+9+8+7+6+5+4+3+2+1=55.
#note--Which are the advantages of functions in python?
#reducing duplication of code. decomposing complex problems into simpler pieces.Improving clarity of teh code.

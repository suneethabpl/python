
def somename():
    print("Hello world")

somename()

name="punee"
def functionname():
    print(f"Hello {name}")

functionname()

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
    return name
print(myfunc())
print(name)


def function_1():
    print("Hello world")
function_1()

def function_1(name):
    print("Hello "+name)
function_1("moverick")


def function_1(name_1,name_2):
    print("Hello "+name_1+" and "+name_2)
function_1('moverick','Yash')


def function_1(*name):
    print("Hello "+name[0]+" and "+name[1])
function_1('moverick','Yash')

def function_1(name_1,name_2="Yash"): 
    print("Hello "+name_1+" and "+name_2) 
function_1('maverick')

def function_1(name_1,name_2="Yash"):  
    print("Hello "+name_1+" and "+name_2)
function_1('maverick','harsh')


def function_1(name_1,name_2="Yash"): 
   y="Hello "+name_1+" and "+name_2
   print(y) 
function_1('maverick','harsh')


def function_1(name_1,name_2="Yash"): 
   return "Hello "+name_1+" and "+name_2
str_1=function_1('maverick','harsh')
print(str_1)



def add(n1,n2):
    return n1+n2
sum=add(1,2)
print(sum)


def add(n1,n2):
    return n1+n2
sum=add(20,40)
print(sum)


def sum(n):
    if n==1:
        return 1 
    else:
        return n+sum(n-1)
sum_1=sum(10)
print(sum_1)


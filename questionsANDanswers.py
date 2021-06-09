# 1)what is python?benefits of using Python?
# A)python is a programming language with objects, modules,threads,exceptions and automatic memory management means no need to declare datatype to variable. the benefits of pythons are that it is simple and easy, portable, extensible,build-in data staructure and it is an open source. 


# 2)how python is interpretered?
# a)python language is an interpreted language. python program runs directly from the source code.
# b)It converts the source code that is written by the programmer into an intermediate langauge, which is again translated into machine language that has to be executed.


# 3)difference between list and tuples in Python?
# a)lists are mutable.they can be edited. lists are slower than tuples. syntax:list1=[10,"punee",30]
# b)tuples are immutable(tuples are lists which can't be edited). Tuples are faster than list. syntax:tuple1=(10,'punee',30)


# 4)what type of language is Python? Programming or scripting?
# a)python is capable of scripting because every line is interpretered then go to next line, but in general it is considered as a programming language in general-purpose.


# 5)what is namespace in python?
# a)example import, def are keywords so, we cam not use them as variable name. namespace is a naming system used to make sure taht names are
# unique to avoid naming conflicts.


# 6)what r the python modules?name some commonly used built-in modules in Python?
# A)python modules are files containg python code. This code can either be functions classes or variables. A 
# python module is a .py file containg executable code. Some of the commonly used built-in modules are:
# os;sys;math;random;data time;json


# 7)what r the local variables and global variables?
# A)varaibles declared outside a function or in global spaces r called global variables. These variables can be accessed by any function in the program.
# B)Any variable declared inside a function is known as a local variable. This variable is present in the local space and not in the global space.


# 8)is python case sensitive? yes. 


# 9) is indentation required in python? 
# A)Indenation is neccesary for python. It specifies a block of code. All code within loops, classes, functions, etc is specified within an indented block.
# A)It is usually done using four space characters. if our code is not indented necessarily, it will not execute accurately and will throw errors as well.


# 10) what is the difference between python Arrays and lists?
# a)Array and lists, in python have the same way of sorting data. But, arrays can hold only a single data type elemts 
# whereas lists can hold any data type elements. Arrays need declaration and lists don't. Arithmetic operation can be performed on array not lists.


# 11)what r functions in python?
# a)A function is a block of code which is executed only when it is called. To define a python function, the def keyword is used.
# Example: 
# def newFunc(): 
#     print("hi, welcome to python")
# newFunc(); #calling the function
# o/p--hi, welcome to python


# 12)what is __init__?
# A)__init__ is a method or constructor in python. This method is automatically called to allocate memory 
# when a new object/instance of a class is created. All classes have the __init__method.
# example
# class Employee:
#     def __init__(self,name,age,salary):
#         self.name = name
#         self.age=age
#         self.salary=20000
# E1 = Employee("XYZ",23,20000)
# print(E1.name)
# print(E1.age)
# print(E1.salary)
# o/p--
# XYZ
# 23
# 20000


# 13) what is a lambda function?
# An annonymous function is known as a lambda function. This function can have any number of parameters but, can ahve just one statment.
# Example--
# a = lambda x,y : x+y
# print(a(5,6))
# o/p--
# 11


#14)what is self in python?
# A)# example
# class Employee:
#     def __init__(self,name,age,salary):
#         self.name = name
#         self.age=age
#         self.salary=20000
# E1 = Employee("XYZ",23,20000)
# print(E1.name)
# print(E1.age)
# print(E1.salary)
# o/p--
# XYZ
# 23
# 20000
#A) self is an instance or an object of a class. In Python, this is explicitly included as the first parameter.
#  However, this is not the case in java where it's optional. it helps to differentiate between the methods and attributes of a class with local variables.
# The self variable in the init method refers to the newly created object while in other methods, it refers to the object whose method was called. 

# 15)what does [::-1] do?
# A) [::-1] is used to reverse the order of an array or a sequence. actually -1 is starting from ending point.
# A) but here stepping is -1 means starting at the end/ from right to left and jumped other elemnt

# 16) how fo u write comments in python?#

# 17) How will you capitalize the first letter of string?
# A) in python, the capitalize() method capitalizes the first letter of a string. if the string already consists of a capital letter at teh beginning, then, it returns the original string. 

# 18) How will you convert a string to all lowercase?
# A)
# stg='ABCD'
# print(stg.lower())
# o/p--
# abcd
               
# 19) what is the purpose of is, not and in operators?
# A)operators are special functions. They taKe one or more values and produce a corresponding result.
# is: returns true when 2 operands are true(Example: "a" is 'a')
# not: returns the inverse of the boolean value
# in: checks if some element is present in some sequence.

# 20)what is the dictionary in python?
# the built-in datatypes in python is called dictionary. it defines one-to-one relationship between keys and values. Dictionaries
# contain pair of keys and their corresponding values. Dictionaries are indexed by keys. 

# 21)how can files to be deleted in python?
# To delete a file in python, we need to import the OS module. After that, you need to use the os.remove() function.

# 22)Does python has oops concept? 
# python is an object-oriented programming language. This means that any program can be solved in python by creating an object model.
# However, python can be treated as procedural as well as structural langugae. 

# 23)what are python libraries?Name a few of them?
# python libraries are a collection of python packages. some of the majorly used python libraries are --
# Numpy,Pandas,Matplotlib,Scikit-learn and many more. 

# 24)what is split used for?
# A)the split()method is used to seperate a given string,list etc in python. 

# 25) what is the polymorphism in python?
# A) polymorphism means the ability to take multiple forms. So, for instance, if the parent class has a method named ABC then
# the child class also can have a method with the same name ABC having its own parameters and variables. python allows polymorphism. 


# 26)define encapsulation in python?
# A)Encapsulation means binding the code and the data together. A Python class in an example of encapsulation 

# 27) how do u do data abstraction in python?
# A) data abstraction is providing only the required details and hiding the implementation from the world. It can be achieved in python by using interfaces and abstract classes. 

#28) does python make use of access specifiers?
# A) python does not deprive access to an instance variable or function. Python lays down the concept of prefixing the name of the 
# variable, function or method with a single or double underscore to imitate the behaviour of protected and private access specifiers. 

#29) what is negative index in python?
# A)python sequences can be index in positive and negative numbers. For positive index, 0 is the first index, 1 is the second index,
# and so on. for negative index, (-1) is the last index and (-2) is the second last index and so on. 

# 30) how can you convert a number to a string?
# A) in order to convert a number into a string, use the inbuilt function str(). if we want a octal or hexadecimal representation,
# use the inbuilt function oct() or hex()

# 31) mention the use of // operator in Python?
# A) it is a floor division operator, which is used for dividing 2 operands with the result as quotient showing
# only digits before the decimal point. For instance, 10//5 = 2 and 10.0//5.0 = 2.0 sometimes integer division operator
# for example, 9/5=1.8 ; 9//5=1; so whenever we want to avoid decimal in o/p.

# 32) How to return the binary of an integre?
# A) use the bin() function.
# bin(5)
#=>'0b101'
# whatever we write in bin method. it converts into binary.

# 33) what is teh difference between remove, del and pop?
# A) remove() remove the first matching value.
# li =['a','b','c','d']
# li.remove('b')
# li
# =>['a','c','d']
#B) del removes an element by index.
# li=['a','b','c','d']
# del li[0]
#li
#=>['b','c','d']
# C) pop() removes an element by index and returns that element.
# li=['a','b','c','d']
# li.pop(2)
#=>'c'
# li
#=>['a','b','d']
# li.pop() for removing last item/element.

# 34) what is differnce between .py and .pyc files?
# A) .py files contain the source code of a program. Whereas, .pyc file contains the bytecode of your program.
# we get bytecode after compilation of .py file(source code). .pyc files are not created for all the files that you run.
# it is only created for the files that you import.
# A)Before executing a python program python interpreter checks for the compiled files. if the file is present, the 
# virtual machine executes it. if not found, it checks for .py file. if found, compiles it to .pyc file and then 
# python virtual machine executes it.
# C)Having .pyc file saves you the compilation time.


# in oops, everything is object.object has 2 fields. those are attributes and speed/behaviour. attributes all properties.
# what was the height of the building?
# how many of those are there in teh building?
# behaviour means what is the purpose of teh building?what the building does?
#is the building have a party?
# create method and define the behavours with teh help of methods?
# class is blue print whatever we make.
# behaviours nothing but methods.
# methods are functions.
#example1)
class classname():
    def building(self,height,floors):
        print("Restaurant")
# create an object 
obj1 = classname()
print(type(obj1))
# find out properties. what is inside of the class.
obj1.building(100,10)



#example2)
#1)create class
class student:
    #3)cretae method/function
    def meth(self,name,age):
        print(name)
        pass

# #example3)
# #1)create class
# class student:
#     #3)cretae method/function
#     def meth(self,name,age):
#         print(name)
#         # self.name1=name
#         pass
# #2)create objects of the class
# obj1=student()
# obj2=student()

# #call meth method
# obj1.meth("mav",20)
# obj2.meth("harsh",30)
# # what is self? we r giving 3 parameters but give 2 arguments.
# print(obj1.name)
# #error is AttributeError: 'student' object has no attribute 'name'. beacuse name does not know which object.we need to tell the name variable belongs to which object.
# #so we need to call the object inisde of method/function. 

#example4)
#1)create class
class student:
    #3)cretae method/function
    def meth(others,name,age):
        #self is predefine keyword. but we can use anything instead of self.
        #we use first attribute for object, not for any variable. 
        others.name1=name
        pass
#2)create objects of the class
obj1=student()
obj2=student()

#call meth method
obj1.meth("mav",20)
obj2.meth("harsh",30)
# what is self? we r giving 3 parameters but give 2 arguments.
print(obj1.name1)
#error is AttributeError: 'student' object has no attribute 'name'. beacuse name does not know which object.we need to tell the name variable belongs to which object.
#so we need to call the object inisde of method/function.

#example5)
#1)create class
class student():
        #3)cretae method/function
    def __init__(self,breed):
        # self.breed1=breed
        print("i'm working fine")

#2)create objects of the class
obj1=student("")
obj2=student("")

#example6)
#1)create class
class student():
        #3)cretae method/function
    def __init__(self,breed):
        self.breed1=breed
        print("i'm working fine")

#2)create objects of the class
obj1=student("lab")
obj2=student("german")

# inheritance
#example1
#single inheritance.u can have properties of your father.here we print second properties.
class first:
    def meth1(self):
        print("meth1")
    def meth2(self):
        print("meth2")
class second:
    def meth3(self):
        print("meth3")
    def meth4(self):
        print("meth4")

sec=second()
sec.meth3()
sec.meth4()

    
#example2
#single inheritance.u can have properties of your father.here second inherits to first properties also.
class first:
    def meth1(self):
        print("meth1")
    def meth2(self):
        print("meth2")
class second(first):
    def meth3(self):
        print("meth3")
    def meth4(self):
        print("meth4")

sec=second() # create object for the second class
sec.meth1() # able to use properties of first class.

#example3
#multi level inheritence meand child can inherites both father and grandfather properties.we dont need to go to 
#grandfather/first because father has grandfather properties. 
class first:
    def meth1(self):
        print("meth1")
    def meth2(self):
        print("meth2")
class second(first):
    def meth3(self):
        print("meth3")
    def meth4(self):
        print("meth4")
class third(second):
    def meth5(self):
        print("meth5")
    def meth6(self):
        print("meth6")
thi=third() # create object for the third class
thi.meth1() # able to use properties of first class.
# here we can assume first is grandfather, second is father and third is  child.

#example4
# multiple inheritance. here there is no connection between first and second. third will inherits the both first and second.
class first:
    def meth1(self):
        print("meth1")
    def meth2(self):
        print("meth2")
class second:
    def meth3(self):
        print("meth3")
    def meth4(self):
        print("meth4")
class third(first,second):
    def meth5(self):
        print("meth5")
    def meth6(self):
        print("meth6")
        thi=third() # create object for the third class
thi.meth1()


#example5
# if second has his own meth1 so second doesn't need to go to first.
class first:
    def meth1(self):
        print("meth1")
    def meth2(self):
        print("meth2")
class second:
    def meth1(self):
        print("meth3")
    def meth4(self):
        print("meth4")

sec=second()
sec.meth1()

#example6
#here when we create third object and call meth1 , third object takes meth1 value/properties  which is in first/grandfatehr.
#because first third will check , it has own meth1, here there is no own meth1 in third so we give in third(first,second)
#so, it will go to check the meth1 in first. first has meth1 so print the value of meth1.
class first:
    def meth1(self):
        print("meth1")
    def meth2(self):
        print("meth2")
class second:
    def meth1(self):
        print("meth3")
    def meth4(self):
        print("meth4")
class third(first,second):
    def meth5(self):
        print("meth5")
    def meth6(self):
        print("meth6")
sec=third()
sec.meth1()

#example6
class first:
    def meth1(self):
        print("meth1")
    def meth2(self):
        print("meth2")
class second:
    def meth1(self):
        print("meth3")
    def meth4(self):
        print("meth4")
class third(second,first):
    def meth5(self):
        print("meth5")
    def meth6(self):
        print("meth6")
sec=third()
sec.meth1()

#example7)
# rectangle class contains area and perimeter methods/functions.
# square method.
#step1)create class
class rectangle():
    #step2)create a constructor init
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    #step2)create a constructor init and it has 2 parametrs/attributes which are length and breadth. and then 
    # self.length and       self.breadth
 
 #create area method/function
    def area(self):
        print(self.length*self.breadth)
#create perimeter method/function
    def perimeter(self):
        print(2*(self.length+self.breadth))
 #create square method/function. square is simillar to rectangle but all sides r equal in square
class square(rectangle):
    pass

sq=square(5,5)
sq.area()
sq.perimeter()

#example8)single inheritance
# rectangle class contains area and perimeter methods/functions.
# square method.
#step1)create class
class rectangle():
    #step2)create a constructor init
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    #step2)create a constructor init and it has 2 parametrs/attributes which are length and breadth. and then 
    # self.length and       self.breadth
 
 #create area method/function
    def area(self):
        print(self.length*self.breadth)
#create perimeter method/function
    def perimeter(self):
        print(2*(self.length+self.breadth))
 #create square method/function. square is simillar to rectangle but all sides r equal in square
class square(rectangle):
    def __init__(self,side): # own init function of square. first check init inside of the square first. 
        super().__init__(side,side)
        #super() to call the methods of parent class(init) which we inherited 
    pass

# sq=square(5,5) why r u giving both values as the values r same. 
sq.area()
sq.perimeter()


#example9)
# rectangle class contains area and perimeter methods/functions.
# square method.
#step1)create class
class rectangle():
    #step2)create a constructor init
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
        print("rectangle init")
    #step2)create a constructor init and it has 2 parametrs/attributes which are length and breadth. and then 
    # self.length and       self.breadth
 
 #create area method/function
    def area(self):
        print(self.length*self.breadth)
#create perimeter method/function
    def perimeter(self):
        print(2*(self.length+self.breadth))
 #create square method/function. square is simillar to rectangle but all sides r equal in square

class circle:
    def __init__(self,radius,radius1):
        print("circle init")

class square(circle,rectangle):
    def __init__(self,side): # own init function of square. first check init inside of the square first. 
        super().__init__(side,side)
        #super() to call the methods of parent class(init) which we inherited 
    pass

sq=square(5)
#o/p--we give square(5) so, 5 goes to    def __init__(self,side): in square class. later it goes to super()
#in super() , it goes to circle class because of class square(circle,rectangle) we give parameters/attribues order are circle,rectangle.
#that's why o/p is    circle init



#example10)
# rectangle class contains area and perimeter methods/functions.
# square method.
#step1)create class
class rectangle():
    #step2)create a constructor init
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
        print("rectangle init")
    #step2)create a constructor init and it has 2 parametrs/attributes which are length and breadth. and then 
    # self.length and       self.breadth
 
 #create area method/function
    def area(self):
        print(self.length*self.breadth)
#create perimeter method/function
    def perimeter(self):
        print(2*(self.length+self.breadth))
 #create square method/function. square is simillar to rectangle but all sides r equal in square

class circle:
    def __init__(self,radius,radius1):
        print("circle init")

class square(rectangle,circle):
    def __init__(self,side): # own init function of square. first check init inside of the square first. 
        super().__init__(side,side)
        #super() to call the methods of parent class(init) which we inherited 
    pass

sq=square(5)

#example11)
# rectangle class contains area and perimeter methods/functions.
# square method.
#step1)create class
class rectangle():
    #step2)create a constructor init
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
        print("rectangle init")
    #step2)create a constructor init and it has 2 parametrs/attributes which are length and breadth. and then 
    # self.length and       self.breadth
 
 #create area method/function
    def area(self):
        print(self.length*self.breadth)
#create perimeter method/function
    def perimeter(self):
        print(2*(self.length+self.breadth))
 #create square method/function. square is simillar to rectangle but all sides r equal in square

class circle:
    def __init__(self,radius,radius1):
        print("circle init")

class square(rectangle,circle):
    def __init__(self,side): # own init function of square. first check init inside of the square first. 
        super().__init__(side,side)
        print("rectangle init")
        #super() to call the methods of parent class(init) which we inherited 
    pass

sq=square(5)

#polymoriphism--
#example1)
#poly means many. olymoriphism means many forms with same name.
print(len("moverick"))
print(len(["moverick","meenal","yash"]))
#here length function works on list,it is counting of number inside of list. 
# tupleswhen we are running length on string, it is counting number of characters inside of the string. 
# how length function and everytime working in a different way.this is called polymoriphism. 

class rectangle:
    def area(self,length,breath):
        print(length*breath)

class square:
    def area(self,side):
        print(side**2)

#create object
rec=rectangle()
sq=square()
rec.area(10,15)
sq.area(5)
#here we have same AREAmethods/functions but there r doing different things in different places. 


#example2)
def add(a,b):
    print(a+b)
def add(a,b,c):
    print(a+b+c)
add(5,6,7)
#here answer is 18 because second add method/function overrides first add method/function. it works only in class concepts. 

#example3)
#poly means many. olymoriphism means many forms with same name.
# print(len("moverick"))
# print(len["moverick","meenal","yash"])
#here length function works on list,it is counting of number inside of list. 
# tupleswhen we are running length on string, it is counting number of characters inside of the string. 
# how length function and everytime working in a different way.this is called polymoriphism. 

class rectangle:
    #create constructor here
    def __init__(self,length,breath):
        self.len=length
        self.breadth=breath
    def area(self):
        print(self.len*self.breadth)
    def permiter(self):
        print(2*(self.len+self.breadth))

class square:
    def __init__(self,side):
        self.side=side
    def area(self):
        print(self.side**2)
    def permiter(self):
        print(self.side*4)

#create object
rec=rectangle(10,15)
sq=square(10)

for shape in (rec,sq):
    shape.area()
    shape.permiter()
#here we have same AREAmethods/functions but there r doing different things in different places. 

#example1)
class test:
     def __init__(self,a="Hello World"):
         self.a=a
 
     def display(self):
         print(self.a)
obj=test()
obj.display()

#example2)
class A():
    def disp(self):
        print("A disp()")
class B(A):
    pass
obj = B()
obj.disp()
#Class B inherits class A hence the function disp () becomes part of class B’s definition. Hence disp() method is properly executed and the line is printed.

#example4)
class A:
    def __init__(self):
        self.multiply(15)
        print(self.i)
 
    def multiply(self, i):
        self.i = 4 * i
class B(A):
    def __init__(self):
        super().__init__()
 
    def multiply(self, i):
        self.i = 2 * i
obj = B()
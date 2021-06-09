

class classname():
    def building(self,height,floors):
        print("Restaurant")
obj1 = classname()
print(type(obj1))
obj1.building(100,10)


class student:
    def meth(self,name,age):
        print(name)
        pass


class student:
    def meth(others,name,age):
        others.name1=name
        pass
obj1=student()
obj2=student()

obj1.meth("mav",20)
obj2.meth("harsh",30)
print(obj1.name1)


class student():
    def __init__(self,breed):
        print("i'm working fine")

obj1=student("")
obj2=student("")

class student():
    def __init__(self,breed):
        self.breed1=breed
        print("i'm working fine")

obj1=student("lab")
obj2=student("german")

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

sec=second() 
sec.meth1()


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
thi=third() 
thi.meth1() 

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
        thi=third() 
thi.meth1()

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


class rectangle():
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        print(self.length*self.breadth)
    def perimeter(self):
        print(2*(self.length+self.breadth))
class square(rectangle):
    pass

sq=square(5,5)
sq.area()
sq.perimeter()

class rectangle():
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        print(self.length*self.breadth)
    def perimeter(self):
        print(2*(self.length+self.breadth))
class square(rectangle):
    def __init__(self,side): 
        super().__init__(side,side)
    pass
sq.area()
sq.perimeter()

class rectangle():
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
        print("rectangle init")
    def area(self):
        print(self.length*self.breadth)
    def perimeter(self):
        print(2*(self.length+self.breadth))

class circle:
    def __init__(self,radius,radius1):
        print("circle init")

class square(circle,rectangle):
    def __init__(self,side): 
        super().__init__(side,side)
    pass

sq=square(5)

class rectangle():
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
        print("rectangle init")
 
    def area(self):
        print(self.length*self.breadth)
    def perimeter(self):
        print(2*(self.length+self.breadth))

class circle:
    def __init__(self,radius,radius1):
        print("circle init")

class square(rectangle,circle):
    def __init__(self,side): 
        super().__init__(side,side)
    pass

sq=square(5)

class rectangle():
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
        print("rectangle init")
    def area(self):
        print(self.length*self.breadth)
    def perimeter(self):
        print(2*(self.length+self.breadth))

class circle:
    def __init__(self,radius,radius1):
        print("circle init")

class square(rectangle,circle):
    def __init__(self,side): 
        super().__init__(side,side)
        print("rectangle init")
    pass

sq=square(5)

print(len("moverick"))
print(len(["moverick","meenal","yash"]))

class rectangle:
    def area(self,length,breath):
        print(length*breath)

class square:
    def area(self,side):
        print(side**2)


rec=rectangle()
sq=square()
rec.area(10,15)
sq.area(5)


def add(a,b):
    print(a+b)
def add(a,b,c):
    print(a+b+c)
add(5,6,7)


class rectangle:
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


rec=rectangle(10,15)
sq=square(10)

for shape in (rec,sq):
    shape.area()
    shape.permiter()



class test:
     def __init__(self,a="Hello World"):
         self.a=a
 
     def display(self):
         print(self.a)
obj=test()
obj.display()



class A():
    def disp(self):
        print("A disp()")
class B(A):
    pass
obj = B()
obj.disp()


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
import square

# import square as sq
print(square.area(2))
print(square.perimeter(10))

# import specific module
from square import area
# print(square.area(20))
print(area(20))
# print(perimeter(10))


from square import area as a
# print(square.area(20))
print(a(5))

print(square.list1[3])
print(square.dict1["punee"])

dir(square)
# dir(sq)

#The total size of the program remains the same regardless of whether modules are used or not. Modules simply divide the program.
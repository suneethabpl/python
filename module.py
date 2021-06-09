import square

print(square.area(2))
print(square.perimeter(10))

from square import area
print(area(20))


from square import area as a
print(a(5))

print(square.list1[3])
print(square.dict1["punee"])

dir(square)

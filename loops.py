fav_foods = ['Pizza', 'Tacos', 'Salmon']
for foodItem in fav_foods:
    print(f"My fav food is: {foodItem}")



fav_foods = ['Pizza', 'Tacos', 'Salmon']
for foodItem in fav_foods:
    if foodItem == "Pizza":
        size = input("What size pizza would you like?")
        print(f"you ordered a {size} size pizza")

fav_food = "pizza!"
for foodItem in fav_food:
    print(foodItem)

person = {
    "name": "kalob",
    "twitter": "@KalobTaulien",
    "instagram":"@coding.for.everybody"
}
for value in person:
    print(value)


person = {
    "name": "kalob",
    "twitter": "@KalobTaulien",
    "instagram":"@coding.for.everybody"
}
for key,value in person.items():
    print(f"The key is {key} and the value is {value}")

num = 0
while num <= 100:
    print(num)
    num = num + 1


items = ['One', 'Two', 'Three', 'Four', 'Five']
for item in items:
    if item == 'Two' or item == 'Four':
        continue
    print (item)


items = ['One', 'Two', 'Three', 'Four', 'Five']
for item in items:
    if item == "Three":
        break
    print(item)


num = 0
while num <= 20:
    num = num + 1
    if num % 2 == 0:
        continue
    print(num)


num = 0
while num <= 1_000_000:
    num = num + 1
    if num == 13:
        break
    print(num)

for num in range(10):
 print("hello")

for num in "hello world":
    print("num")

for num in "hello world":
 print(num)

sum=0
for num in [1,2,3,4,5]:
    sum=sum+num
print(sum)

sum=0
for num in (1,2,3,4,5):
    sum=sum+num
print(sum)

dict={'k1':1, 'k2':2, 'k3':3}
for num in dict.items():
    print(num)

dict={'k1':1, 'k2':2, 'k3':3}
for num,values in dict.items():
    print(values)

for num in range(10):
    print("hello")

for num in range(1,11,2):
 print("hi")


my_list=[]
str_1="code warriors"
for letter in str_1:
   my_list.append(letter)
   print(my_list)


my_list=[letter for letter in str_1]

list_2=[num**2 for num in range(0,11)]
print(list_2)

list_3=[num**2 for num in range(0,11) if num%2==0]
print(list_3)

list_4=[num**2 if num%2==0 else num**3 for num in range(0,11)]
print(list_4)


num=0
while num<10:
    print("hai")
    num=num+1
print(num)

number=0
while number>10:
    print("hello")
    number=number+1
else:
    print("number is less than 10")


while True:
    print("Hello")
    break

num=0
while True:
    num=num+1
    if num == 10:
        break
    print("Hello")
num=0
while num<10:
 num = num+1
 if num == 4:
  continue
 print(num)


while True:
 pass

 for num in range(10):
     pass
print(num)


fav_foods = ['Pizza', 'Tacos', 'Salmon']
# use for loop to do for every item in th eiterable,
for foodItem in fav_foods:
    # print(foodItem)
    print(f"My fav food is: {foodItem}")

# for itemFood in iterable:
#     item clear


fav_foods = ['Pizza', 'Tacos', 'Salmon']
# use for loop to do for every item in th eiterable,
for foodItem in fav_foods:
    if foodItem == "Pizza":
        size = input("What size pizza would you like?")
        print(f"you ordered a {size} size pizza")


# let's the loop all the characters 
#because we know strings are subscriptable, 
# fav_foods = ['Pizza', 'Tacos', 'Salmon']
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


# break & continue in for,while loops
items = ['One', 'Two', 'Three', 'Four', 'Five']
for item in items:
    if item == 'Two' or item == 'Four':
        continue
    print (item)



# break & continue in for,while loops
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

# control flow means if-else ,for
for num in range(10):
 print("hello")

for num in "hello world":
    print("num")

for num in "hello world":
 print(num)

# lists
sum=0
for num in [1,2,3,4,5]:
    sum=sum+num
print(sum)

# tuples
sum=0
for num in (1,2,3,4,5):
    sum=sum+num
print(sum)

# dictionary
dict={'k1':1, 'k2':2, 'k3':3}
for num in dict.items():
    print(num)

# dictionary
dict={'k1':1, 'k2':2, 'k3':3}
for num,values in dict.items():
    print(values)

for num in range(10):
    print("hello")

for num in range(1,11,2):
 print("hi")
#  here start from 1 index and end at 10th index and stepping 2 means if we print 1st index then jumped 2nd and then print 3rd.


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


# while
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

#     number=11
# while number>10:
#     print("hello")
#     number=number+1
# else:
#     print("number is less than 10")

while True:
    print("Hello")
    break

num=0
while True:
    num=num+1
    if num == 10:
        break
    print("Hello")
    # break

    # break statement brings out of the current working loop and continue means go back to loop to continue.
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

# Question 1:
# What will be the output of the following Python code?
# x = ['ab', 'cd']
# for i in x:
#     i.upper()
# print(x)
# ans--'ab', 'cd']
# The function upper() does not modify a string in place, it returns a new string which isn’t being stored anywhere.

# 2)What will be the output of the following Python code?
# i = 1
# while True:
#     if i%3 == 0:
#         break
#     print(i)
 
#     i + = 1
#     ans--SyntaxError, there shouldn’t be a space between + and = in +=
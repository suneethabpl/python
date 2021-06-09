# # lst = ["string",1,3.14, ["A new item"], "kilo"]
# # # print(lst)
# # for item in lst:
# #     print("the item is:",item) 

names = ["punee","lucky"]
print(names)
names.append("Sai")
print(names)
names.remove("punee")
print(names)
jhon=names.pop()
print(names)

# # append to add variable into list
# # remove to remove variable into list
# # pop to put the variable into list

list1=[1,2,3,4,5,6,86554,455667]
print(list1)

list2=["code",'warriors',123,56,74]
print(list2)
print(len(list2))

# concatenation
list3=list1+list2
print(list3)
list3=list2+list1
print(list3)

# immutable means, u can not change any character in string.
#lists are mutable. we can change anything.
# mutability
list1=[1,2,3,4,5,6,86554,455667]
list1[6]=7
list1[7]='seven'
print(list1)

# indexing
print(list1[0])
print(list1[7])

# slicing
# list1[start:stop:step] step means what number of gaps we need to take in between them.
#start means where we can start the number for slicing. stop means where we can stop but last index is not printed/included in stop.
list1=[1,2,3,4,5,6,86554,455667]
print(list1[0:3])
print(list1[0:6:2])
print(list1[ : : ])
print(list1[ :5: ])
list1=[1,2,3,4,5,6,86554,455667]
list1.append(8)
print(list1)
# append to add item at the end of the list
list1.append('nine')
print(list1)
# we can not use variable name is list, print

# inserting item/number
list1.insert(4,70)
print(list1)
list1.insert(4,'seventy')
print(list1)

# pop to remove last item/object/number in the list
list1.pop()
print(list1)

# remove to remove particular element/item/number/object
list1.remove('seventy')
print(list1)

list1=[1,2,3,4,5,6,86554,455667,4,6,4]
print(list1.count(4))

# sort() works only integers list and string list.
list5=[34,56,78,1,2,3]
list5.sort()
print(list5)
list5.reverse()
print(list5)

# dictionaries
# it is unordered paired of objects. they cannot be sorted in any way because there r unorder way. key, value pairs.every value has key system.
dict1={"name":"lucky","age":30,"city":"mumai"}
name=dict1['name']
print(dict1.keys())
print(dict1.values())
print(len(dict1))

# changing value in dictionaries
dict1["city"]="mumbai"
print(dict1)
dict1["state"]="maharashtra"
print(dict1)

dict2={"apple":100, 
"banana":[20,30,40],
'grapes':{"black":50,"green":60}}
print(dict2)

price=dict2['grapes']['black']
print(price)

price2=dict2["banana"][2]
print(price2)

dict1={"name":"lucky","age":30,"city":"mumai"}
dict1.pop('city')
print(dict1)

#pop('city') to remove particular item.
# popitem() to remove the last item in list/dictionaries
dict1.popitem()
print(dict1)
dict1.clear()
print(dict1)

# note--
# What is the output when we execute list(“hello”)?['h','e','l','l','0']
# Which of the following statements create a dictionary?Dictionaries are created by specifying keys and values.


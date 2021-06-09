
names = ["punee","lucky"]
print(names)
names.append("Sai")
print(names)
names.remove("punee")
print(names)
jhon=names.pop()
print(names)



list1=[1,2,3,4,5,6,86554,455667]
print(list1)

list2=["code",'warriors',123,56,74]
print(list2)
print(len(list2))


list3=list1+list2
print(list3)
list3=list2+list1
print(list3)


list1=[1,2,3,4,5,6,86554,455667]
list1[6]=7
list1[7]='seven'
print(list1)


print(list1[0])
print(list1[7])

list1=[1,2,3,4,5,6,86554,455667]
print(list1[0:3])
print(list1[0:6:2])
print(list1[ : : ])
print(list1[ :5: ])
list1=[1,2,3,4,5,6,86554,455667]
list1.append(8)
print(list1)

list1.append('nine')
print(list1)


list1.insert(4,70)
print(list1)
list1.insert(4,'seventy')
print(list1)

list1.pop()
print(list1)

list1.remove('seventy')
print(list1)

list1=[1,2,3,4,5,6,86554,455667,4,6,4]
print(list1.count(4))

list5=[34,56,78,1,2,3]
list5.sort()
print(list5)
list5.reverse()
print(list5)

dict1={"name":"lucky","age":30,"city":"mumai"}
name=dict1['name']
print(dict1.keys())
print(dict1.values())
print(len(dict1))

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

dict1.popitem()
print(dict1)
dict1.clear()
print(dict1)




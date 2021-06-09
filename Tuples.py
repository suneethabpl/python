# # tuples are a lot like lists in the sense that they're an iterable.
# # means it's an iterable, it means that we have multiple items that we can loop through
# # and take an action on every single item.
# # differnce between tuple and list are Immutable. 
# # immutable vs mutable
# # not changable vs changable
# # list example--
animals =["cat",'dog',"Zebra",'donkey']
animals.sort()
print(animals)
# the above is lists in python/arrays in Javascript. in lists, it's not work
# list has sort,reverse,index,append,clear,pop,insert all attributes. but tuples dont have any attributes.
# append to add the item at teh end of teh list.
animals.append('fish')
print(animals)
# we can add,remove,sort items in list like above but we can not do anything in Tuples. Tuples have count and index attributes only.
# Tuple start with parentheses. Lists start with square brackets.
# once we set items in Tuples, we can not do anything, just we can iterable. Tuples are restrectable lists
foods=('pizza','orange','Apple','Pasta')
# foods.sort()
print(foods)
for food in foods:
    print("The food is", food)

# list are mutable and tuples are immutable.lists have a lot of feature than tuples
tuple1=(1,2,3)
print(tuple1)
tuple2=('one',56,2,5,4,5,47)
print(tuple2)

print(tuple2[0])
print(tuple2[ :1 ])
print(tuple2[ :2 ])
# print(tuple2[0]='two') it's not working because in tuples we can not assign items.

print(tuple2.count(1))
print(tuple2.count(2))
print(tuple2.count(4))
print(tuple2.count(5))
print(tuple2.index(2))


# string,list,boolean,dictionary,tuple,set and this is normal text. 
age = input("What is your age?")
data_type = type(age)
print(data_type)
# by default all inputs are going to be a string
# but in my case i saw integer need to work out later
age = int(age)
data_type = type(age)
print(data_type)

print("age",age*4)

grocery_list = ['Apples', 'Oranges', 'Bananas','Apples']
print(grocery_list)
print(type(grocery_list))
grocery_list = set(grocery_list)
print(grocery_list)
print(type(grocery_list))

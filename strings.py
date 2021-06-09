# sentence = "A sentence in here And on a new line"
# print(sentence.upper())

# strings
str_1 = "code warriors"
print(str_1)
str_2 = '100'
print(str_2)
# concatenation means adding of 2 numbers
str_3=str_1+str_2
print(str_3)

str_4="python by "+str_1
print(str_4)
print("python by "+str_1)

# indexing. it starts from left and forward direction with positive index and it starts from right and backward direction with negative index
print(str_1[0])
print(str_1[7])

print(len(str_1))
for i in range(len(str_1)):
    print(str_1[i]+" ",i)


print(str_1[-1])
print(str_1[-2])

# slicing--slice means cutting. start means where we want to starting point for slicing, where we want to slice/cut on this string.. 
#stop means upto which point we want to cut the string. step means how much steps we want to take in between. 
# str_1[start:stop:step]
print(str_1[2:12:2])
# ans:d aro
#it starts from the index2. index2 is d. it goes upto the 12th index. third is e but we give step is 2 thatswhy e is jumped and went to space. and print the space. and then 
# it goes to w because of step is 2 it goes/went  to a and print the a.
# it goes to r because of step is 2 it goes/went  to r and print the r.
# it goes to i because of step is 2 it goes/went  to o and print the o.
# it goes to r because of step is 2 it goes/went  to s and not print the s because s is 12th index. we don't print 12 th index. because we give 12th index. thatswhy we stopped printing at 11th. but we can not print 11th because of step.
#step means leave one and move on other.

str_1="i love python"
print(str_1[ 2: :3])
print(str_1.upper())
print(str_1.lower())

print(str_1.split())
print(str_1.split('o'))

#  Python is case sensitive when dealing with identifiers?
# What is the output of the following program?

# import string

# import string

# Line1 = "And Then There Were None"

# Line2 = "Famous In Love"

# Line3 = "Famous Were The Kol And Klaus"

# Line4 = Line1 + Line2 + Line3

# print(string.find(Line1, 'Were'), string.count((Line4), 'And'))
#ans--(15,2)
#‘Were’ is at Index 15 in Line1, find() returns the index of substring if found in the string Line1. 
#count() returns the total number of occurrences of the substring. Line4 is concatenated string from Line1, Line2 and Line3.
# This code works well with Python v2.x, as some string functions are deprecated in Python v3.x.

# Which keyword is used for function?def

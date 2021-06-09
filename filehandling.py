# open is a method to create a file. 
# x means creating a file.
# w means rewrite a file.means it removes the whole whatever written file start from beginning. 
# a  means appending, just opposite of rewrite means whereever file ends, it starts.
# r means reading teh file. 
f=open("file1","x")
f.write("new file")
f.close()

f=open("file1","r")
print(f.read(4))
f.seek(0)
print(f.read())
# f.tell(5)
f.close()

f=open("file1","w")
f.write("new file by rewrite")
f.close()

f=open("file1","a")
f.truncate(5) #it accepts 5 indexes , rest of them in the string are removed
f.write("new file by appending /n newline1 /n newline2")
f.close()

f.readlines()

# f = None
# for i in range (5):
#     with open("data.txt", "w") as f:
#         if i > 2:
#             break
# print(f.closed)
#o/p--true because The WITH statement when used with open file guarantees that the file object is closed when the with block exits.
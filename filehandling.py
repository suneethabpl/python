
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
f.truncate(5) 
f.write("new file by appending /n newline1 /n newline2")
f.close()

f.readlines()

f = None
for i in range (5):
    with open("data.txt", "w") as f:
        if i > 2:
            break
print(f.closed)

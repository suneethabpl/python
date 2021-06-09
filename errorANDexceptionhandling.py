
try:    
    sum=10+"20"
except:
    print("using different data types for addition")
finally:
    sum=10+20
    print(sum)


try:
    file=open("newfile",'r')
except:
    print("there is no such file")
finally:
    file=open("newfile","w")


try:
    file=open("newfile",'r')
except FileNotFoundError:
    print("there is no such file")
finally:
    file=open("newfile","w")



try:
    file=open("newfile",'r')
except TypeError:
    print("there is no such file")
finally:
    file=open("newfile","w")


try:
    file=open("newfile",'r')
    file.write("hello world")
except FileNotFoundError:
    print("there is no such file")
except OSError:
    print("not writeable")
finally:
    file=open("newfile","w")



try:
    file=open("newfile",'w')
    file.write("hello world")
    file.close()
    file=open('newfile','r')
except FileNotFoundError:
    print("there is no such file")
except OSError:
    print("not writeable")
else:
    print(file.read())
finally:
    file=open("newfile","w")




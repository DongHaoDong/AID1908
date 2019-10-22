f = open("test.txt","w+")
f.write("Hello World")
f.flush()
data = f.read()
print(data)
f.close()


file=open("test.txt","w+")
file.write("Hello World\n")

file.seek(0)
print(file.read())
file.close()
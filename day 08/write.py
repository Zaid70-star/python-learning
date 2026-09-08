file=open("demo.txt","w")
file.write("Hello World\n")
file.write("Welcome\n")
file.write("to python programming\n")
file.writelines(["Hello World\n", "Welcome\n", "to python programming"])

file.close()
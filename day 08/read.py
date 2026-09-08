with open("demo.txt","r")as file:
    print(file.read(7))
    print(file.readlines())
    print(file.seek(0))
    print(file.readline())
    print(file.tell())     

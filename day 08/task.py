with open("demo.txt","r") as file:
    data = file.read().split(" ")
    print(data)
    print("Word count: ", len(data))
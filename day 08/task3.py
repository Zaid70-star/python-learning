def read_file(filename,word):
    with open(filename,"r") as file:
        data = file.read().split(" ")
        count = data.count(word)
        print(f"The word '{word}' appears {count} times in the file '{filename}'.")


read_file("demo.txt", "Zaid")
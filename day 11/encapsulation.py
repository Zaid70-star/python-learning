class student:
    def __init__(self):
        self.__name = ""
        self.__age = ""

    def get_name(self):
        print(self.__name) 

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        print(self.__age)

    def set_age(self, age):
        self.__age = age
std=student()
std.set_name("Zain")
std.set_age(20)
std.get_age()
std.get_name()
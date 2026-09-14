class electronic:
    def power(self):
        print("Power is on")
class tv(electronic):
    def display(self):
        print("Display is on")
class phone():
    def call(self):
        print("Calling...")
class smartPhone(tv, phone):
    def internet(self):
        print("Internet is on")
obj = smartPhone()
obj.power()
obj.display()
obj.call()
obj.internet()

class electronicdevice:
    def power(self):
        print("Power is on")
class laptop(electronicdevice):
    def code(self):
        print("Coding in progress")
laptop1 = laptop()
laptop1.power()
laptop1.code()
class Mobile:
    def __init__(self,brand,model,price):
              self.brand = brand
              self.model = model
              self.price = price
              
    def showDetails(self):
        print("Brand:",self.brand)
        print("Model:",self.model)
        print("Price:",self.price)
        print(f"discount:{self.price*0.10}")
        print(f"totalprice:{self.price-self.price*0.10}")
phone1 = Mobile("Samsung","A12",20000)
phone2= Mobile("Iphone","14",200000)
phone2.showDetails()
class vehicle:
    def move(self):
        print("Vehicle is moving")
class car(vehicle):
    def drive(self):
        print("Car is driving")

class ev(car):
    def charge(self):
        print("Electric vehicle is charging")
ecar=ev()
ecar.move() 
ecar.drive()
ecar.charge()
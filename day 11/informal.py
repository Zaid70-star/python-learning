class text:
    def display(self):
        print("This is a text class")
class image:
    def display(self):
        print("This is an image class")
def object_display(obj):
    obj.display()
object_display(text())
object_display(image())

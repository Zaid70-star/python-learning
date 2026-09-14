class camera:
    def capture(self):
        print("Capturing the image")
class phone(camera):
    def call(self):
        print("Calling in progress")
class smartphone(phone,camera):
    def browse(self):
        print("Browsing the internet")
mobile=smartphone()
mobile.capture()    
mobile.call()
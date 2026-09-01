userinput= input("enter Your cnic number (13 digit):")
if userinput.isdigit() and len(userinput)==13:
    print("valid cnic") 
else :
    print("invalid")                                        
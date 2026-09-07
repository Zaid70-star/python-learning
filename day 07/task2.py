

def Allevennum(list):
        finallist=[]
        for a in list:
            if a%2==0:
                finallist.append(a)
        print(finallist)

output=Allevennum([1,2,3,4,5,6,7,8,9,10])
print(output)
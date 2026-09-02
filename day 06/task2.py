data={ "a": 5, "b": 6, "c": 7 }
final={}
for k,v in data.items():
    final[v]=k
print(final)
maxkey=''
maxvalue=0
for k,v in data.items():
    if v>maxvalue:
        maxvalue=v
        maxkey=k
print(maxkey,maxvalue)
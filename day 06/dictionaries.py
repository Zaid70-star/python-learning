d={
    1:10,
    "name":"zaid",
    "age":20,
    "coursename":["python","agentic"],

}
print(d)
print(d[1])
print(d.get(1))
print(d["age"])
for key,value in d.items():
    print(key,value)
d["age"]=30
print(d)
d.update({"name": "M . zaid "})
del d[1]
print(d)
print(d.pop("age"))
d.popitem()
print(d)
d.clear()
print(d)
print(d.setdefault("name","zaid"))
sen="python is fun python is powerful programming language"
list1=sen.split(" ")
print(list1)
word_count={}
for word in list1:
    word_count[word]=word_count.get(word,0)+1
print(word_count)
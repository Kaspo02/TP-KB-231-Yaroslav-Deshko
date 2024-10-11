myList = [12,34,32,2,55,2,543,7,4,0]


myList.extend([1000, 2000])
print(myList)

myList.sort()
print(myList)

myList.append("append")
print(myList)

myList.insert(0, "insert")
print(myList)

myList.remove("append")
print(myList)

myList.reverse()
print(myList)

newList = myList.copy()
print(newList)

myList.clear()
print(myList)
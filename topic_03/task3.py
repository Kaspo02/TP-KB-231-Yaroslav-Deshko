myDict = {
    1 : "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five", 
}

myDict.update({6:"six"})
print(myDict)

print(myDict.keys())

print(myDict.values())

print(myDict.items())

del myDict[6]
print(myDict)

myDict.clear()
print(myDict)
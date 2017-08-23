listOne = ["juice", "Tomatos", "Potatos", "Bananas"]

firstItem = listOne[0]
print("The first item is", firstItem)

listOne[0] = "Green Juice"

print("The First item is now", listOne[0])

# print 1 up to 3 but NOT including 3
print(listOne[1:3])

listOne.append("Onions")
print(listOne)

listOne.insert(1, "Pickle")
print("insert() ", listOne)

listOne.remove("Pickle")
print("\nremove()", listOne)

listOne.sort()
print("\nsort()", listOne)

listOne.reverse()
print("\nreverse()", listOne)

del listOne[4]
print("\ndel", listOne)

print(len(listOne))

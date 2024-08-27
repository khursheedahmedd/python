#List are mutable

List = [67, 76.3, 'str']

print(List)

print(type(List))
print(len(List))
#In list slice function works same as work in string

newList = [3, 4.3, 1, 3.2, .1, 2 ]
newList.append(1.2)
print(newList)
newList.sort()
print(newList)
newList.reverse()
print(newList)
newList.sort(reverse=True)
print(newList)
newList.insert(2,5)
print(newList)
newList.remove(5)
print(newList)
print(newList.pop())
print(newList)
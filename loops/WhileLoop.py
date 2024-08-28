num = 8

while(num>0):
    print("Helo! You")
    num = num -1
    
List = [3, 4, 52, 4, 3, 'er', 9.0, 5.8]

length = len(List)
print("Elements: ")
while(length > 0):
    print(List[length - 1])
    length -= 1
    
count = 0
print("Elements: ")
while(count < len(List)):
    print(List[count])
    count += 1

newList = [5, 3, 5, 7, 78, 34, 32]
toFind = 78

newcount = 0
while(newcount <len(newList)):
    if(newList[newcount] == toFind):
        print("Found on index: ", newcount)
        break
    newcount += 1
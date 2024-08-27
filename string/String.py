str1 = 'This is a string'
str2 = "this is also a string"
str3 = """This is also a string"""

print(str1)
print(str2)
print(str3)

print(len(str3))

print(str1[1:5])
print(str1[:5])
print(str1[5:])
print(str1[-5:-1])

print(str1.endswith('ing'))
print(str1.replace('ri', 'i'))
print(str2.capitalize())
print(str1.find('ing'))
print(str3.count('s'))
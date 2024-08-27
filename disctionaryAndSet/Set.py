 #Sets element are immutable we can add remove new elements but cannot update an element and store only uinique values. Sets are unordered
 
collection1 = {3, 1, 3, 2, "word", 'word'}
collection2 = {6, 1, 7, 2, "str", 'word'}

# print(collection)

# print(type(collection)) 

print(collection1.union(collection2))
print(collection1.intersection(collection2)) 

# python set never used repeatative item.
a = {1,2,3,4,1,2}
print(a)
print(type(a))


b = {"saikat", "avik", "dev"}
print(b)
print(type(b))
print(len(b))

# to remove sets value

b.remove("dev")
# b.remove("ram")
print(b)

'''
# this will show empty disctioary not empty sets
c = {}
print(type(c))

# to create empty set

d = set()
print(d)

# to add value in a empty set
d.add(4)
d.add(5)


# can't add list in a sets but can be add tuple because tuple is immutable. 

# d.add ([1, 3, 4, 6])
d.add ((1,5,6,7),5,9,6)
print(d)
'''

dev = { 20, "20", 10, 40}
print(len(dev))

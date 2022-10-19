# Set Union

print(" Set Union :")
a = {0, 2, 4, 6, 8}
b = {1, 3, 5, 7, 9}
print(a.union(b))
print(a | b)




# set Intersection
print("set Intersection :")
print(a.intersection(b))
print(a & b)
s1 = {1, 3, 4, 2}
s2 = {2, 4, 5, 6}
print(s1 & s2)



# Set Differnce
print("Set Differnce :")
print(s1.difference(s2))
print(s1 - s2)
print(s2 - s1)



# symmetric difference
# Elements that are in exactly one set
print("symmetric difference :")

# print(s1.symmetricdifference(s2))

print((s1 | s2) - (s1 & s2))



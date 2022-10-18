# tup = (1, 3, 5, 'Sau', 'rabh', 99, 100.22)
# print(tup)

# for ele in tup:
# 	print(ele*2)


#  Concatinating Tuples
# t = (1, 3, 5) + (7, 9, 11)
# print(t)

# tt = (1, )*4
# print(tt)

# Tuple Index

t1 = (1, 2, 3, 4, 1 ,3, 2, 0)
print(t1)
print(t1.index(4) ) #index of num
print(t1.count(3))  #count of num

# Tuple Membership

print(5 in t1)  #Check it is present or not in tuple


# Tuple Unpacking

t = (4, 2, 3, 1)
a = t[0]
b = t[1]
c = t[2]
d = t[3]
print(a, b, c, d)
#  its solution is 

s, t, c, d = t
print(s, t, c, d)

print(*t)
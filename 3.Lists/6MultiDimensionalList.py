# list_2d = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
# print(list_2d)

# print(list_2d[2])
# print(list_2d[2][2]) #OR
# print(list_2d[-2][-1])


# Q1. Make 2 MAtices pf 2*2 and Add each elements of each matrix

a = [[1, 2], [3, 1]]
b = [[1, 3], [2, 1]]

print(a)
print(b)

print("\n")

c = [[None, None], [None, None]]
for i in range(2):
	for j in range(2):
		c[i][j] = a[i][j] + b[i][j]
print(c)

d = [[None, None], [None, None]]
for i in range(2):
	for j in range(2):
		d[i][j] =  b[i][j] - a[i][j]
print(d)

e = [[None, None], [None, None]]
for i in range(2):
	for j in range(2):
		e[i][j] =  b[i][j] * a[i][j]
print(e)

f = [[None, None], [None, None]]
for i in range(2):
	for j in range(2):
		f[i][j] =  b[i][j] //a[i][j]
print(f)

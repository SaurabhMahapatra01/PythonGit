n = int(input())
print("The Multiplcation Table of {}" .format(n))
for i in range(1, 11):
	print("{} * {} = {}" .format(n, i, n*i))
else:
	print("The Table of {} is  Done" . format(n))
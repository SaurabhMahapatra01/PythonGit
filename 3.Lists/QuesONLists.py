# Q1. Rotation of a List

list = [1, 3, 5, 7, 9]
steps = int(input())
size = len(list)
print(list)
for _ in range(steps):
	key = list[-1]

	for i in range(size -1, 0, -1):
		list[i] = list[i -1]
	list[0] = key
print(list)
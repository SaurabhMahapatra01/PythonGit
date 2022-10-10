# size = int(input())
# for row in range(size):
# 	for column in range (row + 1):
# 		print("*" , end = " ")
# 	print(end = "\n")

# size = int(input())
# for row in range(size, 0, -1):
# 	for column in range (0, row):
# 		print("*" , end = " ")
# 	print(end = "\n")

size = int(input())
for row in range(size):
	for column in range (row + 1):
		print(column + 1 , end = " ")
	print(end = "\n")
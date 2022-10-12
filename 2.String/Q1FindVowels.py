str = input()
print(len(str))

# for i in range(0, len(str)):
# 	print(str[i])

count = 0
for i in str:
	if i in "aeiouAEIOU":
		count = count + 1
print("Number of Vowels in the string is {}".format(count))
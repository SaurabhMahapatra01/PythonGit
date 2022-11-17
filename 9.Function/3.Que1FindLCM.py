def LCM(a, b):
	max_num = (a if a>b else b)
	while True:
		if ((max_num % a == 0) and (max_num % b == 0)):
			return max_num
		else:
			max_num = max_num + 1

a = 3
b = 5

res = LCM(a, b)
print(res)
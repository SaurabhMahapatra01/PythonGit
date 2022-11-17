# Function can return multiple values in form of a tuple
 
def calculator(a, b):
	res1 = a + b
	res2 = a - b
	res3 = a * b
	res4 = a / b
	return res1, res2, res3, res4

a = int(input())
b = int(input())
print(calculator(a, b))
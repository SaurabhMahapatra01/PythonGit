# Q1. given a variable n, Calculate the sum of first n numbers

# n = int(input())
# sum = 0
# for i in range(n+1):
# 	sum = sum  + i
# print("The Sum of First {} Numbers is {}".format(n, sum))


# # Q2. Given a variable n, Find if n is prime or not

n = int(input())

if n>1:
	for i in range(2, int(n/2) + 1):
		if n % i==0:
			print("{} is Not Prime".format(n))
			break
	else:
			print("{} is Prime".format(n))
else:
	print(" {} Will be Not Prime")
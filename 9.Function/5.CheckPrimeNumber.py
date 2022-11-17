def primeNum(number):
	is_prime = True
	for i in range(2, number - 1):
		if(number % 1 == 0):
			is_prime = False
	if is_prime:
			print("yehh boiii! Number is Prime")
	else:
			print("No mann! it is not prime number")
	 
number = int(input())
primeNum(number)
# Break : used to exit all coming iteration in a loop
# Continue : It just Skips the Current iteration and moves to the next iteration
# Pass : If you want to keep a block as empty just write pass


# Break

# n = int(input())
# for i in range(n):
# 	if(i == 5):
# 		break
# 	print(i)
# else:
# 	print("No Number")

# Continue

n = int(input())
for i in range(n):
	if(i == 5):
		continue
	print(i)
else:
	print("No Number Left")
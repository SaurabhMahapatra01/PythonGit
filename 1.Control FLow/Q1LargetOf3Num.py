num1 = int(input())
num2 = int(input())
num3 = int(input())

if(num1>=num2 and num1>=num3):
	largest =num1
elif(num2>=num3 and num2>=num3):
    larget = num2
else:
    larget = num3
print("Larget is {} ".format(larget))
str = input()
# rev_str = str[::-1]
# if(str == rev_str):
# print("{} is palindrome".format(str))
# else:
# 	print("{} is not a Palindrome".format(str))

start = 0
end = len(str) -1
is_palindrome = True
while(start <=end):
	if(str[start] != str[end]):
		is_palindrome = False
		break
	start = start + 1
	end = end - 1
if(is_palindrome):
	print("{} is palindrome".format(str))
else:
	print("{} is not a Palindrome".format(str))

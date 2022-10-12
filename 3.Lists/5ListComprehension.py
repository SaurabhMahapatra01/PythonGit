my_list = list(range(0, 11))
print(my_list)

#Creating a new List of square of each element
new_list = []
for i in my_list:
	new_list.append(i*2)

print(new_list)

new_list = []
for i in my_list:
	if(i % 2 == 0):
		new_list.append(i*2)
print(new_list)

# for i in my_list:
# 	if(i % 2 == 0):
# 		new_list.append(i*2)
# 	else:
# 		new_list.append(i*3)
# print(new_list)


#List Comprehension

list = [el*2 for el in my_list]
print(list)

lst = [el*2 for el in my_list if el%2==0]
print(lst)

listt = [el*2 if el%2==0 else el*3 for el in my_list]
print(listt)


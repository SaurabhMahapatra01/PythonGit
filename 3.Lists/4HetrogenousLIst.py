list =[1, True, 1.98, [2, 3, 4], "Python", 10]
print(list)
print(type(list))
print(len(list))

list2 = input()
print(list2)
list1 = list2.split()
print(list1)

"-->".join(list1)
print(list1)

#List Are iterable
for i in list:
	print(i * 2)

# c = [[None, None], [None, None]]
# print(c)
# print(c*2)
# print([ [None]*3 ]*3)


list = [1, 3, 5]
lst = list

lst.append(7)
print("The New Lst is  {}".format(lst))
print("The Old List is {}".format(list))

list = [0, 2, 4]
lst = list.copy()

lst.append(6)
print("The New Lst is  {}".format(lst))
print("The Old List is {}".format(list))


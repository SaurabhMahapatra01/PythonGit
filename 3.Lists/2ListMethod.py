list = [11, 55, 44, 77, 22, 33, 66]
print(list)
list.append(66) #Add Given Element at the end of the list
print(list)

#insert Element at the given position
list.insert(1,99)
print(list)

#Delete Last Element
ele = list.pop()
print("Deleted Element is {}".format(ele))
print(list)


#Delete Element of Given Position
ele = list.pop(4)
print("Deleted Element is {}".format(ele))
print(list)


#Remove the Given Element
list.remove(33)
print(list)

#Sort at Increasing Order
list.sort()
print(list)


#Sort  at Decreasing Order
list.sort(reverse = True)
print(list)

#Check Element is Present or not
print(11 in list)
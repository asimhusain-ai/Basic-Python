list = [ 2,1,4,3,6,5,8,7,9]
copy = list.copy()#14
list.append(10)#1
list.extend([11,12])#2
list.insert(11,13)#3
list.sort()#4
print(list)
list.pop(-1)#5
list.remove(11)#6
list.reverse()#7
print(list)
print("Sum: ",sum(list))#8
print("Count: ",list.count(3))#9
print("Max: ",max(list))#10
print("Min: ",min(list))#11
print("Length: ",len(list))#12
list.clear()#13
print(list)
print(copy)
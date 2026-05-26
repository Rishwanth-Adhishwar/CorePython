my_set={1}
my_set.add(2)
print(my_set)

my_set.update([2,3,4])
print(my_set)
my_set.update([4,5],(1,6,8))
print(my_set)

my_set1={1,3,4,5,6}
print(my_set1)
my_set1.discard(4)
print(my_set1)
my_set1.remove(6)
print(my_set1)
my_set1.discard(2)
print(my_set1)
'''my_set1.remove(2)
print(my_set1)'''
my_set1.pop()
print(my_set1)

my_set1.pop()
print(my_set1)

my_set1.clear()
print(my_set1)
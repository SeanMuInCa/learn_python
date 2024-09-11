list1 = []
print(list1)
list1.append(1)
list1.append(2)
print(list1)
print(list1.pop(1))
list2 = list('helloworld')
print(list2)
list2.reverse()
print(list2)

for i in list2:
    print(i)

for i, j in enumerate(list2):
    print(i, j)

info_tuple = ('hello', 1, 2, 3, 'hello')
print(info_tuple)
print(info_tuple.count('hello'))
print(info_tuple[1])
# info_tuple[1] = 10 #not allowed to change
print(info_tuple[1])
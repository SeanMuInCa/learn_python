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
# tuple is an unchangeable list
info_tuple = ('hello', 1, 2, 3, 'hello')
print(info_tuple)
print(info_tuple.count('hello'))
print(info_tuple[1])
# info_tuple[1] = 10 #not allowed to change
print(info_tuple[1])

for i in info_tuple:
    print(i)

for i, j in enumerate(info_tuple):
    print(i, j)
print(info_tuple.count('hello'))

print('*' * 30)
print(list(range(10)))
print(list(range(1, 10)))
print(list(range(1, 10, 2)))
r1 = range(1,5)
print(r1) # range object is iterable but can't see what is inside
for i in r1:
    print(i)
list3 = list(range(1, 10))
print(list3)
list3[0] = 100
print(list3)
list3.append(10)
print(list3)

str1 = 'hello world'
str2 = '''hello-2024-
nihao'''

print(str2.split('-'))
print(str2.removeprefix('\n'),'removed')
print(str2)
print(str2.split('-'))

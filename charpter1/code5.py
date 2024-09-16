s1 = set()
print(s1)
s1 = {1,2,3,4}
print(s1)

s2 = {3, 3, 3, 3, 4}
print(s2, type(s2))

d1 = dict({'a': 1, 'b': 2, 3:'c'})
s3 = set(d1) #只取了keys
print(s3)

print('nothing?',s2.difference(s3))
print('nothing1?',s3.difference(s2))

a = input('input: ')
print(type(a))

print(1 == '1')
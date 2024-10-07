import random

from jedi.inference.gradual.conversion import convert_names


def newf(*arg):
    print(arg[0])

newf(['a','b','c'])

newf('aa','bb','cc')

myfile = open('data.txt', 'r')

mydata = myfile.read()
mydict = {}

for i in mydata.split():
    if i in mydict:
        mydict[i] += 1
    else:
        mydict[i] = 1


print(mydict)

func = lambda x: x+5
print(list(map(func, [1,2,3,4,5,6])))

names = ['Jared', 'Gavin', 'Walter', 'Mike', 'Brett', 'Hugh']

convert_names = map(lambda x: random.choice(['Eagle', 'Hawk', 'Seagull', 'Heron', 'Sparrow', 'Raven']), names)

print(list(convert_names))
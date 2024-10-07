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
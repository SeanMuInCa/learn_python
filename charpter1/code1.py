

print("hello world")
# 这个是注释

print(666)  # 输出666

"""
我也是注释
"""
# 定义变量不用声明
year = 2024
month = 9
day = 5

print(year, month, day,"today")
print(year,month,day,'\n')
print('next line')
print()
print('another line','\n')
print('in another year' + str(year))  #这个有意思的拼接
print('in another year', year)  #和上面的不一样,逗号自带空格效果


print('today is %d, month %02d, %02d day %s' % (year, month, day, isinstance(year, str)))


content = input("input something : ")
print()
print('the content is', content, end=' ')
print("and it's instanceof str?", isinstance(content, str))
print("and it's instanceof number?", isinstance(float(content), int), content)

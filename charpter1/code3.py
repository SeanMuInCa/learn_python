str = 'hello world'
print(str[0])
print(str[0:4])  # 从索引0开始，到索引4结束，但不包括索引4
nums = '123456789'
print(nums[0:9:2])  # 从索引0开始，到索引9结束，步长为2, 0和9可省略
print(nums[::-1])
print(str[::-1])  # 倒序 字符串反转
n1 = 1.12
print(int(n1))

if n1 > 2:
    print('n1 > 2')
elif n1 > 1:
    print('n1 > 1')
else:
    print('n1 <= 1')

match n1:
    case 1:
        print('n1 = 1')
    case 2:
        print('n1 = 2')
    case _:
        print('n1 != 1 and n1 != 2')

print('done')

def isLeapYear(year):
    if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
        return True
    return False
print(isLeapYear(2024))

n = 9

for i in range(n+1):
    for j in range(i+1):
        if j == 0: continue
        print(j,"*",i,"=",i*j, sep=' ',end='   ')
    print()

for i in range(n):
    for j in range(i + 1):
        print('%d * %d = %d' % (j+1,i+1,(j+1)*(i+1)), end=' ')
    print()

import pandas as pd

# 创建一个 DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Score': [85, 90, 95]
}
df = pd.DataFrame(data)
print(pd)
# 查看数据
print(df)
#
# # 选择某一列
print(df['Name'])
print(df['Age'])
#
# # 筛选数据（选择年龄大于30的人）
# filtered_df = df[df['Age'] > 30]
# print(filtered_df)
#
# # 统计每列的平均值
# print(df.mean())

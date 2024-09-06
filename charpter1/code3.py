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
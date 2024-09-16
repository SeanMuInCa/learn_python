
users = [
    {'name': 'aaa', 'password': '123', 'status': True},
    {'name': 'bbb', 'password': '123', 'status': True},
    {'name': 'ccc', 'password': '123', 'status': False},
]
RETRY = 3
userName = input('请输入用户名：')
password = input('请输入密码：')
for i in users:
    if userName == i['name'] and password == i['password'] and i['status']:
            print('登录成功')
    elif i['name'] == userName and i['password'] == password and not i['status']:
            print('账号被冻结')
    elif i['name'] == userName and i['password'] != password:
        print('密码错误')
        if i['status']:
            RETRY -= 1
            print('还有%d次机会' % RETRY)
        else:
            print('账号被冻结')
else:
    print('用户名错误')
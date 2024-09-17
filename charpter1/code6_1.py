
users = [
    {'name': 'aaa', 'password': '123', 'status': True},
    {'name': 'bbb', 'password': '123', 'status': True},
    {'name': 'ccc', 'password': '123', 'status': False},
]
RETRY = 3
userName = input('请输入用户名：')
password = input('请输入密码：')
for i in users:
    if userName == i['name']:
        if password == i['password']:
            if i['status']:
                print('登录成功')
            else: print('账号被冻结')
        else:
            while RETRY > 1:
                print('密码错误，还有%d次机会' % (RETRY - 1))
                password = input('请输入密码：')
                if password == i['password']:
                    print('登录成功')
                    break
                else: RETRY -= 1
            print('密码错误，账号冻结')
        break
else: print('用户名不存在')
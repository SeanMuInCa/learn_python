
users = {
    'aaa':{'name': 'aaa', 'password': '123', 'status': True},
    'bbb':{'name': 'bbb', 'password': '123', 'status': True},
    'ccc':{'name': 'ccc', 'password': '123', 'status': False},
}
RETRY = 3
userName = input('请输入用户名：')
password = input('请输入密码：')
if userName in users:
    if password == users[userName]['password'] and users[userName]['status']:
        print('登录成功')
    elif not users[userName]['status']:
        print('用户被冻结')
    else:
        for i in range(RETRY):
            password = input('密码错误，请重新输入密码：')
            if password == users[userName]['password']:
                print('登录成功')
                break
            elif i == RETRY - 1:
                print('密码输入错误次数超过3次，用户被冻结')
else: print('用户名不存在')

RETRY_TIMES = 3
valid_users = {'aaa':'123456', 'bbb':'12345', 'ccc':'333'}
black_users = ['xxx', 'yyy', 'zzz']
while RETRY_TIMES != 0:
    username = input('Enter the username: ')
    password = input('Enter the password: ')
    if username in black_users:
        print('you are in black list')
        break
    elif username in valid_users.keys():
        if password == valid_users[username]:
            print('login success')
            break
        else:
            print('password error')
            RETRY_TIMES = RETRY_TIMES - 1
            if RETRY_TIMES == 0:
                print('your account has been locked')
            else:print('you have', RETRY_TIMES, 'times to retry')
    else:
        print('you have not register yet')
        break


if __name__ == '__main__':
    with open('D:\\校园网配置文件\\校园网.txt', 'w', encoding='utf-8') as f:
        print("请进行修改账号与密码,默认配置文件在D:\校园网配置文件\校园网.txt")
        username = input("请输入用户名：")
        password = input("请输入密码：")
        text = username + '@telecom' + password
        f.write(text)
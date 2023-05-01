import pprint
import requests
import pathlib
from urllib import parse


def write_file(file, data):
    with open(file, 'w') as f:
        f.write(data)
        f.close()

def read_file(file):
    with open(file, 'r') as f:
        return f.read()

F_USERNAME = './username.txt'
F_PASSWORD = './password.txt'
F_URL = './url.txt'

# 显示消息并2秒后退出
def show_msg(msg):
    print(msg)
    import time
    time.sleep(2)
    import sys
    sys.exit()

# 显示欢迎字符
def show_welcome():
    print(
'''-----------------------------------------------------------
    .88888. dP     dP 88888888bd888888P  dP                       oo        
d8'   `8888     88 88          88     88                                 
88       88     88a88aaaa      88     88       .d8888b..d8888b.dP88d888b.
88   YP8888     88 88          88     88       88'  `8888'  `888888'  `88
Y8.   .88Y8.   .8P 88          88     88       88.  .8888.  .888888    88
 `88888' `Y88888P' 88888888P   dP     88888888P`88888P'`8888P88dPdP    dP
                                                            .88          
                                                        d8888P
                Welcome to use the login script!
                        青铜火机和电吹风 制作           
----------------------------------------------------------- 
''')
    
    
headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,ko;q=0.7',
    'Connection': 'keep-alive',
    'Host': '10.0.1.5',
    'Referer': 'http://10.0.1.5/',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
}


if __name__ == '__main__':
    if not pathlib.Path(F_USERNAME).exists():
        show_welcome()
        write_file(F_USERNAME, input('您的学号：'))
    if not pathlib.Path(F_PASSWORD).exists():
        write_file(F_PASSWORD, input('您的密码：'))
    if not pathlib.Path(F_URL).exists():
        type = int(input('请选择登录类型：1.校园网 2.中国移动 3.中国联通 4.中国电信\n请输入您的选择（一个数字）：'))
        if type == 1:
            write_file(F_URL, f"http://10.0.1.5/drcom/login?callback=dr1003&DDDDD={read_file(F_USERNAME)}&upass={parse.quote(read_file(F_PASSWORD))}&0MKKey=123456&R1=0&R2=&R3=0&R6=0&para=00&v6ip=&terminal_type=3&lang=zh-cn&jsVersion=4.2&v=7004&lang=zh")
        elif type == 2:
            write_file(F_URL, f"http://10.0.1.5/drcom/login?callback=dr1003&DDDDD={read_file(F_USERNAME)}@cmcc&upass={parse.quote(read_file(F_PASSWORD))}&0MKKey=123456&R1=0&R2=&R3=0&R6=0&para=00&v6ip=&terminal_type=3&lang=zh-cn&jsVersion=4.2&v=7004&lang=zh")
        elif type == 3:
            write_file(F_URL, f"http://10.0.1.5/drcom/login?callback=dr1003&DDDDD={read_file(F_USERNAME)}@unicom&upass={parse.quote(read_file(F_PASSWORD))}&0MKKey=123456&R1=0&R2=&R3=0&R6=0&para=00&v6ip=&terminal_type=3&lang=zh-cn&jsVersion=4.2&v=7004&lang=zh")
        else: 
            write_file(F_URL, f"http://10.0.1.5/drcom/login?callback=dr1003&DDDDD={read_file(F_USERNAME)}@telecom&upass={parse.quote(read_file(F_PASSWORD))}&0MKKey=123456&R1=0&R2=&R3=0&R6=0&para=00&v6ip=&terminal_type=3&lang=zh-cn&jsVersion=4.2&v=7004&lang=zh")

    login_IP = 'http://10.0.1.5/'
    not_sign_in_title = '上网登录页'
    result_return = ':1'
    sign_parameter = read_file(F_URL)
    signed_in_title = '注销页'

    try:
        r = requests.get(login_IP, headers=headers,
                        timeout = 1)
        req = r.text
    except:
        req = 'False'

    if signed_in_title in req:
        show_msg("该设备已经登录")

    elif not_sign_in_title in req:
        
        r = requests.get(sign_parameter, headers=headers,timeout=1)
        req = r.text
        pprint.pprint(req)
        if result_return in req:
            show_msg("登录成功")
        else:
            show_msg("登录失败")

    else:
        show_msg("未连接到校园网")

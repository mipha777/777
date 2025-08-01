# -*- coding: utf-8 -*-
"""
@Author   : shaozi
@Version  : Python 3.12
@Date     : 2025/8/2 00:18
@Desc     : 
"""


import requests
def Checklogin(cookie,token,data):
    headers = {
        'user-agent': 'Mozilla/5.0'
    }
    params = {"csrf_token": token}
    response = requests.post(f'https://music.163.com/weapi/pl/count?', headers=headers, params=params,data=data,cookies=cookie)
    if len(response.text) == 0:
        print('登录过期，重新登录')
        return False
    else:
        return True
# -*- coding: utf-8 -*-
"""
@Author   : shaozi
@Version  : Python 3.12
@Date     : 2025/7/29 20:36
@Desc     :  # 所有与网易云音乐接口交互的函数
"""


def get_music_toplist(cookies,listid,ua):
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'priority': 'u=0, i',
        'referer': 'https://music.163.com/',
        'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'iframe',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'upgrade-insecure-requests': '1',
        'user-agent': ua,
        # 'cookie': '_ntes_nnid=b9929e671a0c5d00f0f0ef8475f86e73,1753785264977; _ntes_nuid=b9929e671a0c5d00f0f0ef8475f86e73; NMTID=00OGB0USzNOd0QxHEtAgpN8v2UW5q8AAAGYVb9osA; WEVNSM=1.0.0; WNMCID=pkalun.1753785266103.01.0; WM_TID=TYeaEZKe%2FsBBAEUBUALXkSJznu556ARO; sDeviceId=YD-%2BqhUC3P6%2F4NFQkRUEBfCkTJzjr8%2FCMDT; __snaker__id=Jq562J2MhXS7dlLc; ntes_kaola_ad=1; _iuqxldmzr_=32; __csrf=1e861b79128bec2470f3560f49e13f69; MUSIC_U=005FA2B823AEBB3589DB9F0BDA15A6428B83D4C6A8CA34806C76F6CE4482045190639FE9C3964348DFCABE00BC9E4A2BDB86D59FE3C429755480C8AE98003CECA31D428EA8C1130645920A6EC33E2252F480FFBEE69728D3B84DE093B8A5E410BCAD82A8B580A1C219E630565B021F444BD86BE6F9EAB7203F889766B777522A574015338A8028E4AC7088D5A74C0803B3B4BB9EECA8CCB388DDCD036822BC372BD951E8BA6C955C77D1E4738DA0C320CC2AC223B4BFAEE0B4E79DBDFA7BCEE72C57B5B65FF90ADD619490E2AF328709ED8B18C69A6620ACE76C5D1E0D43EB8BADAB6897A056801ECAFB3AA31029704A35D1FA5C13F669334B6593F3650CF76F79014A52C7992A6EC100A00AB7A111BC6B21FC382FD303C75F89B48E070D7EFF25B1A30B97CFB88747BCC527AB35DD6CFC382A4D6DAA8BDF88126B716626BBC7AC94291566CFFBABD6B8201BA182F35940D087241C2738121CFB824B318C74B8BD5D9A7F41B52FB04CA5DB0853722CC44489893CBCA2DAF314617F4B642E8629EC53E3CCA9F3943F1702D660F785A1316C; gdxidpyhxdE=ewI%2BlMUg8OK04xbxpTn9USXAdpZz%2B4RCj6r66%5CBLBl0vVcT%2FKJb8QumP3yEKTTQxqYrldUGYGRBVY0WN664iOWqGiL8rXCNRHIh4dYwjHm15TES6YeRM0bLx5CnOvpAc9NVzKzlIzZ7gwrYqJQ%5CnsIPtfNGaQZ4MAxWxSVozkdX9OT%2Fy%3A1753810833607; WM_NI=F76bF%2F0wNjdTM1Cg3%2F7x1NTxLeSnfV0ttZk0LUY1joTS8sOv3vovYP7lkMqo62pgcm62RE5N%2FebnbZWKaOwdk%2F7aFa%2BN8Hcq%2FNUZhhgZtOFIf2zDS2b7zvzcJrBCav4cQ2I%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eeaad450ab92af88b665a68a8aa6c14a938b8f87c77d8890ada8e47aa999fd9aed2af0fea7c3b92a86e9fa83c525f4a9828be7608fef8d88b225f5a8ffafd77490bb9d8fe55ef4acbcbbea3c908b97d2e965988df894ce7ef1aaa197dc5cf5b4a5aef465f6eec088e267f6ee9ea6b846edbbae8fe1529595afb0f670a9f1f982c56be992f8a9e27bed929bbbeb64a586bcb0c543a6eeb6a5d23aa2e9b697f9698aae8ea4e47ef8bd9fd3cc37e2a3; ntes_utid=tid._.H5VVJc8vUABERwVBEUeClWd2jus7HSlZ._.0.%2C.edd._.._.0; JSESSIONID-WYYY=ts%5Cj2R3k5fXQFZsyZfYMx%2BC%2BnXFo353%2FC1jz1VP34Za4opGtmBzQR7KaMvNB8pGVxUoiNh6k3j5FNHXbntq8inlIEn%2FAJpYBDy5knCM3vZPM6YnqO2%5C4WI5pK1OHfmRrd9p9Ru5P9yHKM1P%2FKqOdXSFsAB3VMwsTgfs9N9Phy7fKvHzJ%3A1753904868047',
    }
    params = {
        'id': listid,
    }
    import requests
    from bs4 import BeautifulSoup
    print(f'正在访问{listid}')
    response = requests.get('https://y.music.163.com/m/discover/toplist?', cookies=cookies, headers=headers,params=params)
    print(response.status_code)
    print(response.text)
    soup = BeautifulSoup(response.text, 'html.parser')
    # 选中所有歌曲项
    # 找到ul.f-hide
    ul = soup.find('ul', class_='f-hide')
    result = []


    for a in ul.find_all('a'):
        href = a['href']  # /song?id=2730020036
        # 从href中提取id
        song_id = href.split('=')[1]
        song_name = a.text.strip()


        # 提取歌曲名和歌手信息
        # song_name_tag = item.select_one('.sgtl')
        # singer_tag = item.select_one('.sginfo')
        #
        # song_name = song_name_tag.get_text(strip=True) if song_name_tag else ''
        # singer = singer_tag.get_text(strip=True) if singer_tag else ''

        result.append({
            'id': song_id,
            'song_name': song_name,
            # 'singer': singer
        })
    print('共查询到',len(result),'首歌')
    return result

if __name__ == '__main__':
    print(get_music_toplist())

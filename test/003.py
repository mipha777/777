# -*- coding: utf-8 -*-
"""
@Author   : shaozi
@Version  : Python 3.12
@Date     : 2025/8/1 17:40
@Desc     : 
"""
import os
import pandas as pd
from config import SONGS_PATH
data1 = {
        'song_name': '稻香',
        'artist': '周杰伦',
        'comments': [
            {'user_id': '123', 'username': '小明', 'content': '太好听了'},
            {'user_id': '456', 'username': '阿花', 'content': '回忆满满'},
        ]
    }
data2 = {
        'song_name': '晴天',
        'artist': '周杰伦',
        'comments': [
            {'user_id': '789', 'username': '李雷', 'content': '经典！'},
        ]
    }


df = pd.DataFrame(data1)
df.to_csv(
    'song_comments.csv',
    mode='a',                         # 👈 a = append 追加写入
    index=False,
    header=False,
    encoding='utf-8-sig'
)

df = pd.DataFrame(data2)
df.to_csv(
    'song_comments.csv',
    mode='a',                         # 👈 a = append 追加写入
    index=False,
    header=False,
    encoding='utf-8-sig'
)


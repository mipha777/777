# -*- coding: utf-8 -*-
"""
@Author   : shaozi
@Version  : Python 3.12
@Date     : 2025/7/29 20:37
@Desc     : # 保存 JSON / CSV 工具
"""
import os

import pandas as pd
from config import SONGS_PATH

def save(all_data:dict):
    song_name = all_data.get('song_name', '')
    songer = all_data.get('songer', '')
    new_comments = all_data.get('new_comments', [])
    hot_comments = all_data.get('hot_comments', [])
    def parse_comments(comments, comment_type):
        return [
            {
                "歌名": song_name,
                "歌手": songer,
                "评论类型": comment_type,
                "发言人": c.get('发言人'),
                "ip地址": c.get("ip地址"),
                "发言内容": c.get("发言内容")
            }
            for c in comments
        ]

    new_comment = parse_comments(new_comments, "new")
    hot_comment = parse_comments(hot_comments, "hot")
    comments =  new_comment + hot_comment  # 返回合并后的列表

    df = pd.DataFrame(comments)
    df.to_csv(SONGS_PATH, index=False, encoding='utf-8-sig',mode='a',header=False)

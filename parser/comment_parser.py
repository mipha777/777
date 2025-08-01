# -*- coding: utf-8 -*-
"""
@Author   : shaozi
@Version  : Python 3.12
@Date     : 2025/7/29 20:36
@Desc     : # 提取评论数据，分页处理
"""
import json

def parser(response):
    res = json.loads(response.text)
    new_comments = res.get('data', {}).get('comments', [])
    hot_comments = res.get('data', {}).get('hotComments', [])
    def parse_comments(comments):
        return [
            {
                 "发言人": c.get("user", {}).get("nickname", "None"),
                "ip地址": c.get("ipLocation", {}).get("location", "None"),
                "发言内容": c.get("content", "None")
            }
            for c in comments
        ]
    new_comment = parse_comments(new_comments)
    hot_comment = parse_comments(hot_comments)
    return new_comment, hot_comment

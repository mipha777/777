# -*- coding: utf-8 -*-
"""
@Author   : shaozi
@Version  : Python 3.12
@Date     : 2025/7/29 20:34
@Desc     : # 主程序入口，控制整体流程
"""
import json
import threading
import time
import random
from queue import Queue
from config import ua,COOKIE_PATH,top_list_url,hotsong_listid,upsong_listid,newsong_listid,Original_listid,back_cookie
from cookie_manager.browser_cookie import main_get_cookies
from cookie_manager.Check_login import Checklogin
from encrypt.crypto_api import get_p_e
from api.commit_api import get_hot_commit
from api.music_api import get_music_toplist
from parser.comment_parser import parser
from utils.file_helper import save
from utils.cookie_clean import cookie_clean



# ---提前配置线程---
requests_threads = 2
parser_threads= 3
save_threads = 1
song_queue = Queue()
comment_queue = Queue()
save_queue = Queue()

# 程序运行
cookies = back_cookie()
if cookies is False:
    main_get_cookies()
token = cookies["__csrf"]
# 获取加密参数
js_login = json.dumps({"csrf_token": token})
p_e_for_login = get_p_e(js_login)
data = {
        'params': p_e_for_login[0],
        'encSecKey': p_e_for_login[1]
    }
# 检查登录状态是否失效

state = Checklogin(cookie=cookies,token=token,data=data)
if state is False:
    # 执行cookie清除计划
    # 执行重新登录
    cookie_clean()
    main_get_cookies()

# 获取某个榜单下的所有歌曲信息 # 榜单id在config配置文件内
all_songs = get_music_toplist(cookies=cookies,listid=hotsong_listid,ua=ua)
for song in all_songs:
    song_queue.put(song)

def work_song():
    while not song_queue.empty():
        song = song_queue.get()
        try:
            songid = song['id']  # 歌曲id
            songname = song['song_name']  # 歌名
            js_dict = {
                "rid": f"R_SO_4_{songid}",
                "threadId": f"R_SO_4_{songid}",
                "pageNo": "1",
                "pageSize": "20",
                "cursor": "-1",
                "offset": "0",
                "orderType": "1",
                "csrf_token": f"{token}"
            }
            json_str = json.dumps(js_dict)
            p_e = get_p_e(json_str)  # 获取加密参数
            params_key = p_e[0]
            encSecKey = p_e[1]
            params = {"csrf_token": token}  # 请求参数
            # 获取评论请求的响应体
            comments_response = get_hot_commit(cookie=cookies, params_key=params_key, encSecKey=encSecKey, params=params,
                                               songid=songid, ua=ua)
            time.sleep(random.randint(1, 3))
            comment_queue.put((songname,songer,comments_response))
        except Exception as e:
            print(f'{songname}请求失败 错误：{e}')
        song_queue.task_done()

def work_comment():
    while 1:
        try:
            songname,songer,comments_response = comment_queue.get(timeout=5)
            print(f"正在解析{songname}")
        except  :
            break
        try:
            # 解析评论
            new_comments ,hot_comments= parser(comments_response)
            # 保存队列
            save_queue.put(
                {
                    'song_name':songname,
                    'songer':songer,
                    'new_comments': new_comments,
                    'hot_comments':hot_comments,
                }
            )
        except Exception as e:
            print(f'{songname}解析错误：{e}')
        comment_queue.task_done()

def work_save():
    while True:
        all_data = save_queue.get()
        if all_data is None:
            print("保存线程退出")
            save_queue.task_done()
            break
        try:
            songname = all_data['song_name']
            print(f"正在保存：{songname}")
            save(all_data)
        except Exception as e:
            print(f'{songname} 保存失败：{e}')
        save_queue.task_done()

def main ():
    # 启动请求线程
    request_num = []
    for _ in range(requests_threads):
        t = threading.Thread(target=work_song)
        t.start()
        request_num.append(t)

    # 循环检测有没有请求后的数据
    while comment_queue.empty():
        time.sleep(0.5)
    print('已经获取请求数据，开始解析')

    # 启动解析线程
    parse_num = []
    for _ in range(parser_threads):
        t = threading.Thread(target=work_comment)
        t.start()
        parse_num.append(t)

    # 启动保存线程
    save_num = []
    for _ in range(save_threads):
        t = threading.Thread(target=work_save)
        t.start()
        save_num.append(t)

    # 等待线程结束
    for t in request_num:
        t.join()
    for t in parse_num:
        t.join()
    save_queue.join()
    save_queue.put(None)
    for t in save_num:
        t.join()
    print('所有任务完成')


if __name__ == '__main__':
    main()
# -*- coding: utf-8 -*-
"""
@Author   : shaozi
@Version  : Python 3.12
@Date     : 2025/8/2 00:41
@Desc     : 
"""
import os
import shutil
from config import COOKIE_PATH,folder_path

def cookie_clean():
    if os.path.exists(COOKIE_PATH):
        os.remove(COOKIE_PATH)
        print("cookie.json 已删除")
    else:
        print("cookie.json 不存在，无需删除")

    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        shutil.rmtree(folder_path)
        print(f"已删除文件夹：{folder_path}")
    else:
        print(f"文件夹不存在：{folder_path}")

if __name__ == '__main__':
    cookie_clean()
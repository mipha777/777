# -*- coding: utf-8 -*-
"""
@Author   : shaozi
@Version  : Python 3.12
@Date     : 2025/7/29 20:35
@Desc     : # 使用 execjs 调用 JS 加密函数
"""

def get_p_e(token):
    import os
    import execjs
    # 获取当前 py 文件所在目录
    base_dir = os.path.dirname(os.path.abspath(__file__))
    js_path = os.path.join(base_dir, 'encrypt.js')

    with open(js_path, 'r', encoding='utf-8') as f:
        js_code = f.read()

    p_e = execjs.compile(js_code)
    params = p_e.call('get_params_encSecKey',token)
    return params
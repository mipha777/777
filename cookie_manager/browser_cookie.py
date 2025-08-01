# -*- coding: utf-8 -*-
"""
@Author   : shaozi
@Version  : Python 3.12
@Date     : 2025/7/29 20:34
@Desc     : # 使用 Playwright 自动登录并保存 cookie
"""

import os
import json
import asyncio
from webbrowser import Chrome
from playwright_stealth import Stealth
from playwright.async_api import async_playwright
from config import base_url, COOKIE_PATH


BROWSER_DATA_DIR = "browser_data"
user_login_url = 'https://music.163.com/weapi/login/qrcode/client/login'
async def browser_get():
    # 确保浏览器数据目录存在
    os.makedirs(BROWSER_DATA_DIR, exist_ok=True)
    # 创建 Stealth 实例
    stealth = Stealth()
    # 2. 启动带持久化上下文的浏览器
    async with async_playwright() as p:
        context = await p.chromium.launch_persistent_context(
            BROWSER_DATA_DIR,
            headless=False,
            slow_mo=100,
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/114.0.0.0 Safari/537.36',
            # ---- 增强伪装参数 ----
            viewport={'width': 1920, 'height': 1080}, # 设置标准分辨率
            locale='zh-CN',                          # 设置为中文
            timezone_id='Asia/Shanghai',             # 设置为东八区时区
            args=['--disable-blink-features=AutomationControlled'] # 禁用自动化标志
        )

        # 将 stealth 应用到上下文中
        await stealth.apply_stealth_async(context)
        page = await context.new_page()

        try:
            print("正在检查登录状态...")
            await page.goto(base_url, timeout=15000)

            # 等待片刻，让页面充分加载或跳转
            await page.wait_for_timeout(2000)

            login_button = page.locator('[data-action="login"]')
            # 检查当前 URL 判断是否已登录
            if await login_button.is_visible():
                print("请登录")
                await login_button.click()
                # 等待用户登录（扫码、账号密码等），最长等待 2 分钟
                for _ in range(120):  # 每秒检查一次，最多 120 秒
                    cookies = await page.context.cookies()
                    cookie_names = [cookie['name'] for cookie in cookies]
                    if 'MUSIC_U' in cookie_names:
                        print("登录成功")
                        break
                    await page.wait_for_timeout(1000)  # 每秒检查一次
                else:
                    print("登录超时，未检测到登录成功")
                    exit()
            else:
                print("检测到您已登录。")

            # 无论之前是否登录，都刷新一下 cookie
            print("正在刷新并保存 cookie...")
            cookies = await context.cookies()
            cookies_dict = {cookie['name']: cookie['value'] for cookie in cookies}
            save_cookies(cookies_dict)
        except Exception as e:
            print(f"操作过程中出现错误: {e}")
            exit()
        finally:
            # 自动关闭
            await context.close()
            exit()
            # return True, cookies_dict  # 表示登录成功，返回 cookie 字典

def save_cookies(cookies):
    with open(COOKIE_PATH, 'w',encoding='utf-8') as f:
        json.dump(cookies, f, ensure_ascii=False, indent=4)
    print('cookie已更新')


def main_get_cookies():
    asyncio.run(browser_get())

if __name__ == '__main__':
    main_get_cookies()
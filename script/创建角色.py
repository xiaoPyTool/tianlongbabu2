# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 创建角色.py
# Time       ：2023.4.16 11:16
# Author     ：Lex
# HomePage   : lexgeeker.com
# Email      : 2983997560@qq.com
# Description：
"""
import time
from xiaopy import *

while True:
    # 创建角色界面判断
    res = xp.getTextAll()
    if res:
        for i in res:
            # 创建过角色, 直接进入游戏
            if "进入游戏" in i.text:
                xp.tap(i.x, i.y)

            # 没有创建过角色, 进入创建角色界面, 然后进入游戏
            if "左右滑动屏幕查看更多门派" in i.text:
                print("创建角色界面, 点击创建角色")
                xp.tap(182, 191)
                time.sleep(2)
                xp.tap(461, 254)
                time.sleep(2)
                xp.tap(878, 498)
                time.sleep(2)
                xp.tap(823, 504)
                time.sleep(2)
                xp.tap(554, 349)
    time.sleep(2)

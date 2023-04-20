# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 打开APP.py
# Time       ：2023.4.16 10:56
# Author     ：Lex
# HomePage   : lexgeeker.com
# Email      : 2983997560@qq.com
# Description：
"""
import time
from xiaopy import *

while True:
    # 判断当前运行的APP是否是指定的APP
    ret = xp.currentAppPackageName()
    if ret != "com.pwrd.projectt.ld":
        # 打开APP
        xp.launchApp("com.pwrd.projectt.ld")

    # 关闭公告
    res = xp.findImage("公告叉号.png", 830, 67, 844, 80, 0.9)
    if res:
        xp.tap(res.x, res.y)
        print("点击公告叉号")

    # 点击上次登陆
    res = xp.findText("闯荡江湖", 604, 331, 721, 376, 0.7)
    if res:
        xp.tap(res.x, res.y)
        print("点击上次登陆")

    time.sleep(2)
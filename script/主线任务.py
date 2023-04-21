# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 主线任务.py
# Time       ：2023.4.21 22:18
# Author     ：Lex
# HomePage   : lexgeeker.com
# Email      : 2983997560@qq.com
# Description：
"""
import time
from loguru import logger
from xiaopy import *

while True:
    # 跳过剧情
    res = xp.findText("跳过剧情", 801, 9, 940, 57, 0.7)
    if res:
        xp.tap(res.x, res.y)
        logger.info("找到跳过剧情, 点击跳过 %s %s" % (res.x, res.y))
        time.sleep(0.5)

    # 跳过剧情_确定
    res = xp.findText("确定", 471, 282, 624, 374, 0.6)
    if res:
        xp.tap(res.x, res.y)
        logger.info("找到跳过剧情_确定, 点击跳过剧情_确定 %s %s" % (res.x, res.y))
        time.sleep(0.5)

    # 判断是否在主界面
    res = xp.findImage("任务.png", 70, 99, 88, 124, 0.9)
    if res:
        xp.tap(res.x + 120, res.y + 5)
        logger.info("找到任务, 点击任务 %s %s" % (res.x, res.y))
        time.sleep(0.5)

    # 向右箭头
    res = xp.findImage("右.png", 0.9)
    if res:
        xp.tap(res.x + 30, res.y + 10)
        logger.info("找到向右箭头, 点击向右箭头 %s %s" % (res.x + 30, res.y + 10))
        time.sleep(0.5)

    # 向左箭头
    res = xp.findImage("左.png", 0.95)
    if res:
        xp.tap(res.x - 30, res.y + 10)
        logger.info("找到向左箭头, 点击向左箭头 %s %s" % (res.x - 30, res.y + 10))
        time.sleep(0.5)

    # 向下箭头
    res = xp.findImage("下.png", 0.95)
    if res:
        xp.tap(res.x + 10, res.y + 50)
        logger.info("找到向下箭头, 点击向下箭头 %s %s" % (res.x + 10, res.y + 50))
        time.sleep(0.5)

    # 手指转轮
    res = xp.findText("手指轮转", 79, 4, 329, 444, 0.7)
    if res:
        # 使用gesture方法, 传入手指转轮的坐标
        logger.info("找到手指轮转")
        # Android8+ 以上使用gesture

    # 自动释放技能
    res = xp.findImage("战斗目标.png", 611, 16, 620, 23, 0.95)
    if res:
        logger.info("找到战斗目标, 自动释放技能")
        xp.tap(858, 439)
        time.sleep(0.2)
        xp.tap(787, 501)
        time.sleep(0.2)
        xp.tap(761, 432)
        time.sleep(0.2)
        xp.tap(786, 368)
        time.sleep(0.2)
        xp.tap(842, 337)

    # 向上的小手
    res = xp.findImageAll("小手.png", 0.95)
    if res and len(res) < 4:
        for item in res:
            if (item.x - 10) < 0 or (item.y - 30) < 0:
                continue
            xp.tap(item.x - 10, item.y - 30)
            logger.info("找到向上的小手, 点击向上的小手 %s %s" % (item.x - 10, item.y - 30))
            time.sleep(0.2)

    # 向下的小手
    res = xp.findImageAll("小手_下.png", 0.95)
    if res and len(res) < 4:
        for item in res:
            xp.tap(item.x + 30, item.y + 50)
            logger.info("找到向下的小手, 点击向下的小手 %s %s" % (item.x + 30, item.y + 50))
            time.sleep(0.2)
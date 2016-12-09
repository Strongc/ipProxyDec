#!/usr/bin/python
#coding:utf-8

import schedule


import logging
import crawlermain

logging.basicConfig()#日志基础配置
mainschedule=None
#定时任务添加函数
def addschedule(event, day_of_week='0-7', hour='11',minute='57' ,second='0',id=''):
    global mainschedule
    if mainschedule is None:
        mainschedule=schedule.schedulecontrol()
    mainschedule.addschedule(event,day_of_week,hour,minute,second,id=id)
#定时任务初始化函数
def scheduleinit():

    global mainschedule
    mainschedule=schedule.schedulecontrol()
    mainschedule.addschedule(crawlermain.zmaptask, '0-7', '0-23', '*/10', '0', id='proxy_zmap')  # 定时任务器
    mainschedule.addschedule(crawlermain.taskinit,'0-7','0-23','*/30','0',id='proxy_get')#定时任务器
    # mainschedule.addschedule(event=crawlermain.taskinit, type='date')#单次任务
    mainschedule.start()
    print 'init schedule'

scheduleinit()
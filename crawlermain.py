#!/usr/bin/python
#coding:utf-8

import crawlercore
import config
import crawlertask
import time
def init():

    import proxytask,Sqldatatask
    item=proxytask.getObject()
    data=Sqldatatask.getObject()
def getdatafromFile():

    temp = crawlertask.getObject()
    # init()
    for website in config.proxysource:
        for item in crawlercore.ruletowebsite(website):

            temp.add_work([item])
def taskinit():
    getdatafromFile()
def zmaptask():
    import zmaptool
    t=zmaptool.getObject()
    t.do_scan()
if __name__ == "__main__":
    getdatafromFile()
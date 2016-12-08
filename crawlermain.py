#!/usr/bin/python
#coding:utf-8

import crawlercore
import config
import crawlertask
import time
def getdatafromFile():
    temp = crawlertask.getObject()
    for website in config.proxysource:
        for item in crawlercore.ruletowebsite(website):

            temp.add_work([item])
def taskinit():
    getdatafromFile()

if __name__ == "__main__":
    getdatafromFile()
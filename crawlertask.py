#!/usr/bin/python
#coding:utf-8
from ThreadTool import ThreadTool
import datetime,config
import time
import connectpool
from TaskTool import TaskTool

import webtool
import config
import crawlercore
import Sqldatatask
snifferinstance=None
def getObject():
    global snifferinstance
    if snifferinstance is None:
        snifferinstance=crawlerTask(2)
        snifferinstance.set_deal_num(5)
    return snifferinstance
class crawlerTask(TaskTool):
    def __init__(self,isThread=1,logger=None):
        TaskTool.__init__(self,isThread)
        self.logger = logger
        self.__sqltool=Sqldatatask.getObject()
        self.config=config.Config
    def task(self,req,threadname):

        result=crawlercore.getStaticHtml(req)
        ips=crawlercore.getIPfromPage(result)
        self.__sqltool.add_work(list(ips))

        return None
if __name__ == "__main__":

    for website in config.proxysource:
        for item in crawlercore.ruletowebsite(website):
            result = crawlercore.getStaticHtml(item)
            ips = crawlercore.getIPfromPage(result)
            print ips
            print len(ips)
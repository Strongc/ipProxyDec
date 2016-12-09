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
        rules=req[1]

        result=crawlercore.getStaticHtml(path=req[0])
        ips=crawlercore.getIPfromPage(page=result,rules=rules)
        ipsall=[list(ips)]
        self.__sqltool.add_work(ipsall)

        return None
if __name__ == "__main__":

    for website in config.proxysource:
        for item in crawlercore.ruletowebsite(website):
            result = crawlercore.getStaticHtml(path=item[0])

            ips = crawlercore.getIPfromPage(page=result,rules=website)
            print ips
            print len(ips)

# __cfduid=dff31348dc917e11686bea84826aaa2041480994843; Hm_lvt_1761fabf3c988e7f04bec51acd4073f4=1480994463; Hm_lpvt_1761fabf3c988e7f04bec51acd4073f4=1481006102; CNZZDATA1253901093=1597796917-1480989095-http%253A%252F%252Fwww.66ip.cn%252F%7C1480991790; cf_clearance=061b6886dd44da722fc3e842bf666eb4c9ef5b6a-1481005891-300
# __cfduid=dff31348dc917e11686bea84826aaa2041480994843; Hm_lvt_1761fabf3c988e7f04bec51acd4073f4=1480994463; Hm_lpvt_1761fabf3c988e7f04bec51acd4073f4=1481006082; CNZZDATA1253901093=1597796917-1480989095-http%253A%252F%252Fwww.66ip.cn%252F%7C1480991790; cf_clearance=061b6886dd44da722fc3e842bf666eb4c9ef5b6a-1481005891-300
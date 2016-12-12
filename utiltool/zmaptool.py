#!/usr/bin/python
#coding:utf-8
import time
import re

import os

import config,proxytask




portname = {'3128':'http','8080':'http','443':'https','22':'telnet','3306':'mysql','873':'rsync'}
zmapinstance=None
def getObject():
    global zmapinstance
    if zmapinstance is None:
        zmapinstance=Zmaptool()
    return zmapinstance
class Zmaptool:
    def __init__(self):


        self.config=config.Config
        self.proxytask=proxytask.getObject()

    def do_scan(self,port='3128',iprange=None):
        path=os.getcwd()
        locate=os.path.split(os.path.realpath(__file__))[0]

        cmd = " zmap "+iprange+"  -B  3M -p " + port + "   -q -O json"

        import commandtool
        returnmsg=None
        try:
            returnmsg=commandtool.command(cmd=cmd)
        except Exception,e:
            pass

        p = re.compile(r""""saddr": "(.*)" """)


        if returnmsg:

            list= p.findall(returnmsg)
            print list
            localtime=str(time.strftime("%Y-%m-%d %X", time.localtime()))
            insertdata=[]
            jobs=[]
            for i in list:
                insertdata.append((str(i),port,portname['3128']))
            print len(insertdata)
            self.proxytask.add_work([insertdata])


def getFile(path,callback):
    with open(path) as file:
        for line in file:
            callback(line)

def dosomething(line):
    temp =getObject()

    iprange= line.split()[0]
    temp.do_scan(iprange=iprange)
def action():
    getFile('CN_cidr.txt', dosomething)

if __name__ == "__main__":
    getFile('CN_cidr.txt',dosomething)

    












 

#!/usr/bin/python
#coding:utf-8
import time
import re
from subprocess import Popen, PIPE
import os
import SQLTool
import config,proxytask

import Sqldatatask

import   trace 

portname = {'80':'http','8080':'http','443':'https','22':'telnet','3306':'mysql','873':'rsync'} 
zmapinstance=None
def getObject():
    global zmapinstance
    if zmapinstance is None:
        zmapinstance=Zmaptool()
    return zmapinstance
class Zmaptool:
    def __init__(self):

        self.sqlTool=Sqldatatask.getObject()
        self.config=config.Config
        self.proxytask=proxytask.getObject()

    def do_scan(self,port='8080',num='15'):
        path=os.getcwd()
        locate=os.path.split(os.path.realpath(__file__))[0]
        # cmd=" zmap 54.32.32.23/20 -B  3M -p "+port+"   -q -O json"
        cmd = " zmap -w " + locate + "/iparea.json  -B  3M -p " + port + " -N " + num + "   -q -O json"

        import commandtool

        returnmsg=commandtool.command(cmd=cmd)
        p = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
        list= p.findall(returnmsg)

        localtime=str(time.strftime("%Y-%m-%d %X", time.localtime()))
        insertdata=[]
        jobs=[]
        for i in list:
            insertdata.append((str(i),port,'http'))
        print len(insertdata)
        self.proxytask.add_work([insertdata])






if __name__ == "__main__":
    temp=Zmaptool()
    temp.do_scan()
    












 

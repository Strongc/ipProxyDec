#!/usr/bin/python
#coding:utf-8
from TaskTool import TaskTool
import time,checkproxy,Sqldatatask
taskdata=None
def getObject():
	global taskdata
	if taskdata is None:
		taskdata=ProxyTask(0)
		taskdata.set_deal_num(1)
	return taskdata
class ProxyTask(TaskTool):
	def __init__(self,isThread=1):
		TaskTool.__init__(self,isThread,deamon=False)

		self.__sqltool = Sqldatatask.getObject()
	def task(self,req,threadname):
		item=checkproxy.Proxy_Gevent()
		item.put(req)

		# ip=req[0]
		# port=req[1]
		# protocol=req[2]
        #
		# result= checkproxy.check(ip=ip,port=port,potocol=protocol)
		# self.__sqltool.add_work(result)


		return None

if __name__ == "__main__":
	p=ProxyTask()
	p.add_work([1])


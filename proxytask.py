#!/usr/bin/python
#coding:utf-8
import  TaskTool
taskdata=None
def getObject():
	global taskdata
	if taskdata is None:
		taskdata=ProxyTask(1)
		taskdata.set_deal_num(1)
	return taskdata
class ProxyTask(TaskTool):
	def __init__(self,isThread=1):
		TaskTool.__init__(self,isThread)

	def task(self,req,threadname):



		return None

if __name__ == "__main__":
	pass
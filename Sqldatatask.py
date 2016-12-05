#!/usr/bin/python
#coding:utf-8
from ThreadTool import ThreadTool
import datetime
import time
import SQLTool
from TaskTool import TaskTool




sqltaskdata=None
def getObject():
	global sqltaskdata
	if sqltaskdata is None:
		sqltaskdata=SqlDataTask(1)
		sqltaskdata.set_deal_num(1)
	return sqltaskdata
class SqlDataTask(TaskTool):
	def __init__(self,isThread=1):
		TaskTool.__init__(self,isThread)
		self.sqlhelp=SQLTool.getObject()
		self.sqlhelp.connectdb()
	def task(self,req,threadname):
		# print threadname+'数据库任务　执行任务中'+str(datetime.datetime.now())
		listarray=[]
		listarray.append((req,))
		self.sqlhelp.replaceinserttableinfo_byparams(table='proxy',select_params=['ip'],insert_values=listarray)
		# print threadname+'数据库任务　结束'+str(datetime.datetime.now())


		return None

if __name__ == "__main__":
	pass



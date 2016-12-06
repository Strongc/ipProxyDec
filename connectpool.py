#!/usr/bin/python
#coding:utf-8

import connecttool
import Queue
import gc


connectpoolinstance=None
def getObject():
	global connectpoolinstance
	if connectpoolinstance is None:
		connectpoolinstance=ConnectPool()
	return connectpoolinstance
class ConnectPool:

	def __init__(self,poolsize=1000,logger=None):
		self.__connect_pool = Queue.Queue(maxsize=poolsize) 		#连接池
		self.connectTool=connecttool.ConnectTool()
		self.logger = logger

	def check_network(self):
		import httplib2 
		try: 
			http = httplib2.Http() 
			resp, content = http.request("http://www.baidu.com") 
		except: 
				return 0
		return 1 
	def  getConnect(self,URL,way='GET',params={},times=1):
		self.__connect_pool.put(1)
		self.logger and self.logger.info('当前访问的位置为：%s', URL)


		head,page=self.connectTool.getHTML(URL,way,params,times)
		i=1
		while i<3:
			if 'cookie/flashcookie.swf' in page:
				head, page = self.connectTool.getHTML(URL, way, params, times)
				print '页面被劫持,重新访问'
			else:
				break
		if head=='err':
			import browsertool
			browser=browsertool.Browser()
			browser.get(path=URL,timewait=5)
			cookie=browser.getcookie()
			self.connectTool.setHeader('Cookie',cookie)
			page=browser.getpage()





		self.__connect_pool.get()
		self.__connect_pool.task_done()
		return head,page


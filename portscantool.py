
#!/usr/bin/python
#coding:utf-8
import time
import re

import os

import socket

portway = {'sip':'INVITE  world \r\n\r\n','2':'8080','3':'443','4':'22','5':'23'}  
class Portscantool:
    def __init__(self):
        
        socket.setdefaulttimeout(8)


        self.socketclient=None
    def do_scan(self,head=None,context=None,ip=None,port=None,name=None,productname=None,nmapscript=None):
        keywords={}
        hackinfo=''
        ans = None
        reply=''
        self.socketclient=None
        try:
          self.socketclient=  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
          self.socketclient.connect((ip,int(port)))

#             message = "GET / HTTP/1.1\r\nHost: oschina.net\r\n\r\n"
          message =portway.get(name,"GET  world \r\n\r\n")
          if self.socketclient:
            self.socketclient.sendall(message)
          else:
            self.socketclient=  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            elf.socketclient.connect((ip,int(port)))
          reply = self.socketclient.recv(4096)

          return 'reply info:  ',reply,keywords,hackinfo

        except Exception, msg:
          print 'Failed to create socket. Error code: ' + str(msg)
          return 'error info:','error',keywords,hackinfo
        finally:
          if self.socketclient is not None:
            self.socketclient.close()
    def http_connect():
      pass
if __name__ == "__main__":
    temp=Portscantool()
    print temp.do_scan(ip='127.0.0.1', port='3306')
#     temp.do_scan('218.106.87.35', '110')
    












 

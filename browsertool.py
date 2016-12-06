#!/usr/bin/python
# coding:utf-8
from selenium import webdriver
import  time
# browser = webdriver.PhantomJS()
# browser.implicitly_wait(10)
# browser.get('http://www.66ip.cn/2.html')
#
# time.sleep(5)
#
# cookie=browser.get_cookies()
# print cookie

# browser.quit()
def singleton(cls, *args, **kw):
    instance={}
    def _singleton():
        if cls not in instance:
            instance[cls]=cls(*args, **kw)
        return instance[cls]
    return _singleton

@singleton
class Browser():
    def __init__(self):


        self.__browser = webdriver.PhantomJS()
        self.__browser.implicitly_wait(10)
    def get(self,path,timewait=0):
        self.__browser.get(path)
        time.sleep(timewait)


    def getpage(self):
        return self.__browser.page_source
    def getcookie(self):
        cookie = self.__browser.get_cookies()
        li = eval(cooke)
        cookie = ''
        for i in li:
            cookie = cookie + i['name'] + '=' + i['value'] + ';'
        return cookie

    def close(self):
        self.__browser.quit()

cooke="[{u'domain': u'.66ip.cn', u'name': u'Hm_lpvt_1761fabf3c988e7f04bec51acd4073f4', u'value': u'1480996482', u'path': u'/', u'httponly': False, u'secure': False}, {u'domain': u'.66ip.cn', u'name': u'Hm_lvt_1761fabf3c988e7f04bec51acd4073f4', u'expires': u'\u5468\u4e09, 06 12\u6708 2017 03:54:41 GMT', u'value': u'1480996482', u'expiry': 1512532481, u'path': u'/', u'httponly': False, u'secure': False}, {u'domain': u'www.66ip.cn', u'name': u'CNZZDATA1253901093', u'expires': u'\u5468\u4e8c, 06 6\u6708 2017 03:54:41 GMT', u'value': u'537710808-1480994599-http%253A%252F%252Fwww.66ip.cn%252F%7C1480994599', u'expiry': 1496721281, u'path': u'/', u'httponly': False, u'secure': False}, {u'domain': u'.66ip.cn', u'name': u'cf_clearance', u'expires': u'\u5468\u4e8c, 06 12\u6708 2016 04:59:40 GMT', u'value': u'2d0f205c5534efa2e24b9227e5f694a5a569768d-1480996480-300', u'expiry': 1481000380, u'path': u'/', u'httponly': True, u'secure': False}, {u'domain': u'.66ip.cn', u'name': u'__cfduid', u'expires': u'\u5468\u4e09, 06 12\u6708 2017 03:54:36 GMT', u'value': u'da637c5610bc9b03da6c2478faf3638781480996476', u'expiry': 1512532476, u'path': u'/', u'httponly': True, u'secure': False}]"
def getcookie():
    li=eval(cooke)
    cookie=''
    for  i in li:
        cookie=cookie+ i['name']+'='+i['value']+';'
    return cookie
    print cookie
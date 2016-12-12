#!/usr/bin/python
#coding:utf-8

import urllib2,httplib
import urllib
import time
import socket,Sqldatatask
import gevent
from gevent import pool, queue, spawn, joinall
ip_check_url = 'http://www.baidu.com/'
user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:12.0) Gecko/20100101 Firefox/12.0'
socket_timeout = 5

class Proxy_Gevent():
    def __init__(self):
        from gevent import monkey,sleep
        monkey.patch_all()
        self.pool = pool.Pool(100)
        self.sqltool=Sqldatatask.getObject()
        self.i=0
    def put(self,data):
        for item in data:
            self.pool.spawn(self.start, item[2], item[0], item[1])
        self.pool.join()
    def start(self,protocol,ip,port):
        result=check(protocol,ip,port)
        self.i+=1
        if len(result)>0:
            self.sqltool.add_work(result)
        print self.i



def check_http(protocol, pip):
    data=pip.split(':')
    ip=data[0]
    port=data[1]
    conn=None
    try:
        conn = httplib.HTTPConnection(host=ip,port=port, timeout=socket_timeout)
        conn.request(method='GET', url=ip_check_url)
        res = conn.getresponse()
        result= str(res.getheaders())
        if result.find('BWS')>0:
            print 'check_http',ip,port
            return True
        elif result.find('bfe')>0:
            print 'check_http', ip, port
            return True
        else:
            return False
    except Exception, e:
        print e
        return False
    finally:
        if conn is not None:
            conn.close()
# Check proxy
def check_http_proxy(protocol, pip):
    proxy_detected=False
    try:
        proxy_handler = urllib2.ProxyHandler({protocol:pip})
        opener = urllib2.build_opener(proxy_handler)

        urllib2.install_opener(opener)
        #
        req = urllib2.Request(ip_check_url)
        req.get_method = lambda: 'HEAD'
        time_start = time.time()
        conn = urllib2.urlopen(req)
        time_end = time.time()

        result= str(conn.info())
        if  result.find('bfe')>0:
            print 'check_http_proxy', pip


        # print detected_pip
            proxy_detected = True
            return True
        else:
            return False
    except urllib2.HTTPError, e:
        print "ERROR: Code ", e.code
        return False
    except Exception, detail:
        print "ERROR: ", detail
        return False

    return proxy_detected
def check(potocol,ip,port=None):
    httplist=[8123,3128,8000,8080]
    socklist=[1080, 9050]
    result=[]
    if port is None:
        if potocol=='http':
            for i in httplist:
                if proxy_check(potocol,ip,i):
                    result.append((ip,i))
                    break
        else:
            for i in socklist:
                if proxy_check(potocol, ip, i):
                    result.append((ip, i))
                    break
    else:
        if proxy_check(potocol, ip, port):
            result.append((ip, port))
    return result
def proxy_check(potocol,ip,port):

    socket.setdefaulttimeout(socket_timeout)
    start_time = time.time()
    if potocol=='http':
        protocol = "http"
        current_proxy = ip+':'+str(port)



        proxy_detected = check_http(protocol, current_proxy)

        # start_time = time.time()
        # proxy_detected = check_http(protocol, current_proxy)
        # print 'training check_http took %fs!' % (time.time() - start_time),ip

    else:
        proxy_detected=socket_check(potocol,ip,port)
    print 'training check_http_proxy took %fs!' % (time.time() - start_time), ip

    return proxy_detected
def socket_check(potocol,ip,port):
    import socks
    socket.setdefaulttimeout(socket_timeout)
    s=None
    s = socks.socksocket()
    if potocol=='socks4':
        s.set_proxy(socks.SOCKS4, ip, port)
    elif potocol=='socks5':
        s.set_proxy(socks.SOCKS5, ip, port)
    else:
        s.set_proxy(socks.HTTP, ip, port)

    try:
        s.connect(("www.baidu.com", 80))
        s.sendall("GET / HTTP/1.1\r\n\r\n ")
        result= str(s.recv(1024))
        if result.find('BWS') > 0:
            print 'check_socket_proxy', ip,port
            return True
        elif result.find('bfe') > 0:
            print 'check_socket_proxy', ip, port
            return True
        else:
            return  False
    except Exception,e:
        print e
        return False

def socket_check1(potocol,ip,port):
    import socks
    import socket
    socket.setdefaulttimeout(socket_timeout)
    type=None
    if potocol=='socks4':
        type=socks.SOCKS4

    elif potocol=='socks5':
        type=socks.SOCKS5

    else:
        type=socks.HTTP

    socks.setdefaultproxy(type, ip, port)

    socket.socket = socks.socksocket



    import urllib2

    req = urllib2.Request(ip_check_url)
    req.get_method = lambda: 'HEAD'
    time_start = time.time()
    try:
        conn = urllib2.urlopen(req)
        result = str(conn.info())
        print result,conn.read()
        if result.find('bfe') > 0:
            print 'check_socks_proxy', ip,port
            return True
        else:
            return False

    except urllib2.HTTPError, e:
        print "ERROR: Code ", e.code
        return False
    except Exception, detail:
        print "ERROR: ", detail
        return False
if __name__ == '__main__':
    start_time = time.time()
    ary=[]
    t = ('43.246.208.135', '1081', 'socks4',)

    ary.append(t)

    p=Proxy_Gevent()
    p.put(ary)


    # print 'training took %fs!' % (time.time() - start_time)
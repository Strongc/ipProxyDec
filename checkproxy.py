#!/usr/bin/python
#coding:utf-8

import urllib2
import urllib
import time
import socket

ip_check_url = 'http://www.baidu.com/'
user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:12.0) Gecko/20100101 Firefox/12.0'
socket_timeout = 30

# Check proxy
def check_http_proxy(protocol, pip):

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

        result= conn.read()
        print result
        # print detected_pip
        proxy_detected = True

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
        else:
            for i in socklist:
                if proxy_check(potocol, ip, i):
                    result.append((ip, i))
    else:
        if proxy_check(potocol, ip, port):
            result.append((ip, port))
    return result
def proxy_check(potocol,ip,port):

    socket.setdefaulttimeout(socket_timeout)
    if potocol=='http':
        protocol = "http"
        current_proxy = ip+':'+str(port)
        proxy_detected = check_http_proxy(protocol, current_proxy)
    else:
        proxy_detected=socket_check(potocol,ip,port)

    return proxy_detected


def socket_check(potocol,ip,port):
    import socks
    import socket
    socket.setdefaulttimeout(socket_timeout)
    if potocol=='socks4':
        socks.setdefaultproxy(socks.SOCKS4, ip, port)
    elif potocol=='socks5':
        socks.setdefaultproxy(socks.SOCKS5, ip, port)
    else:
        socks.setdefaultproxy(socks.HTTP, ip, port)
    # socks.setdefaultproxy(socks.PROXY_TYPE_HTTP, "5.2.74.92", 1080)
    socket.socket = socks.socksocket
    import urllib2

    req = urllib2.Request('http://www.baidu.com/')
    req.get_method = lambda: 'HEAD'
    time_start = time.time()
    try:
        conn = urllib2.urlopen(req)
        print conn.getcode()
        return True

    except urllib2.HTTPError, e:
        print "ERROR: Code ", e.code
        return False
    except Exception, detail:
        print "ERROR: ", detail
        return False
if __name__ == '__main__':
    start_time = time.time()
    socket_check()
    print 'training took %fs!' % (time.time() - start_time)
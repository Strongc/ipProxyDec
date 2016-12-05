#!/usr/bin/python
#coding:utf-8

import connecttool
import re
import config
import connectpool
def getfullcode(path='http://ip.zdaye.com/'):
    from selenium import webdriver
    driver = webdriver.PhantomJS()
    driver.get(path)
    result= driver.page_source
    driver.quit()
    return result
def getIPfromPage(page,rule=r'(?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?![\.\d])'):

    reip = re.compile(rule)

    iplist=set()
    for ip in reip.findall(page):
        iplist.add(ip)
    return iplist

def getStaticHtml(path):

    crawler=connecttool.ConnectTool()
    head,result=crawler.getHTML(path)
    return result






def ruletowebsite(rules):
    websites=[]
    if rules[1]=='':
        websites.append(rules[0])
    else:

        for i in range(int(rules[1]), int(rules[2]) + 1):
            result = rules[0] % (i)
            websites.append(result)
    return websites







#!/usr/bin/python
# coding:utf-8
from geoip2.database import Reader
from os.path import dirname, abspath, join
def getisp(ip):
    loc_info={}
    r = Reader(join(abspath(dirname(__file__)), 'GeoIP2-ISP.mmdb'))
    obj = r.isp(ip)
    print obj.raw
    loc_info['isp'] = {

        'organization': obj.raw.get('autonomous_system_organization', ''),
        'isp': obj.raw.get('isp', ''),
    }
    print loc_info
    r.close()


getisp(ip='58.218.215.155')
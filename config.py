#!/usr/bin/python
#coding:utf-8
class Config(object):
	#config file #
	host='localhost'
	username='root'
	passwd=''
	database='data'
	port=3306
	charset='utf8'
	cachemax=30
	cachemin=1
	iptable='proxy'
# proxysource格式
# 第一个 网址通用模板
# 第二个 起始页
# 第三个 终止页
# 第四个 ip匹配规则
# 第五个 端口匹配规则
# 第六个 协议类型
proxysource=[
# ('http://31f.cn/socks-proxy/','','','',r'<td>%s</td>\n<td>(\d+)</td>','socks5'),
# ('http://31f.cn/http-proxy/','','','',r'<td>%s</td>\n<td>(\d+)</td>','http'),
# ('http://31f.cn/https-proxy/','','','',r'<td>%s</td>\n<td>(\d+)</td>','https'),
# ('http://www.proxy360.cn/default.aspx','','','',r"""<span class="tbBottomLine" style="width:140px;">\s+%s\s+</span>\s+<span class="tbBottomLine" style="width:50px;">\s+(\d+)""",'https'),
# ('http://www.nianshao.me/?page=%s','1','1','',r"""%s</td>\n<td style="WIDTH:40PX">(\d+)""",'http'),存在问题
# ('http://ip.baizhongsou.com/', '', '','',r"""%s:(\d+)""",'http'),

# ('http://www.3464.com/data/Proxy/Socks5/', '', '','',r"""%s</td><td>(\d+)""" ,'socks5'),
#100
('http://www.mayidaili.com/free/%s','1','1'),#端口为图片
# ('http://www.proxy360.cn/Region/Brazil','','','',r"""%s\s+</span>\s+<span class="tbBottomLine" style="width:50px;">\s+(\d+)""",'http'),
# ('http://www.proxy360.cn/Region/China','','','',r"""%s\s+</span>\s+<span class="tbBottomLine" style="width:50px;">\s+(\d+)""",'http'),
# ('http://www.proxy360.cn/Region/America','','','',r"""%s\s+</span>\s+<span class="tbBottomLine" style="width:50px;">\s+(\d+)""",'http'),
# ('http://www.proxy360.cn/Region/Taiwan','','','',r"""%s\s+</span>\s+<span class="tbBottomLine" style="width:50px;">\s+(\d+)""",'http'),
# ('http://www.proxy360.cn/Region/Thailand','','','',r"""%s\s+</span>\s+<span class="tbBottomLine" style="width:50px;">\s+(\d+)""",'http'),
# ('http://www.proxy360.cn/Region/Japan','','','',r"""%s\s+</span>\s+<span class="tbBottomLine" style="width:50px;">\s+(\d+)""",'http'),
# ('http://www.proxy360.cn/Region/Thailand','','','',r"""%s\s+</span>\s+<span class="tbBottomLine" style="width:50px;">\s+(\d+)""",'http'),
# ('http://www.proxy360.cn/Region/Vietnam','','','',r"""%s\s+</span>\s+<span class="tbBottomLine" style="width:50px;">\s+(\d+)""",'http'),
# ('http://www.proxy360.cn/Region/bahrein','','','',r"""%s\s+</span>\s+<span class="tbBottomLine" style="width:50px;">\s+(\d+)""",'http'),
# ('http://www.kuaidaili.com/proxylist/%s/','1','10','',r"""%s</td>\s+<td data-title="PORT">(\d+)""",'http'),
# ('http://api.xicidaili.com/free2016.txt','','','',r"""%s:(\d+)""",'http'),
# ('http://www.xicidaili.com/nn/%s','1','6','',r"""%s</td>\s+<td>(\d+)""",'http'),
# ('http://www.xicidaili.com/nt/%s','1','6','',r"""%s</td>\s+<td>(\d+)""",'http'),
# ('http://www.xicidaili.com/wn/%s','1','6','',r"""%s</td>\s+<td>(\d+)""",'http'),
# ('http://www.xicidaili.com/wt/%s','1','6','',r"""%s</td>\s+<td>(\d+)""",'http'),
# ('http://www.66ip.cn/%s.html','2','6','',r"""%s</td><td>(\d+)""",'http'),
# ('http://www.66ip.cn/index.html','','','',r"""%s</td><td>(\d+)""",'http'),
# ('http://www.66ip.cn/areaindex_1/%s.html','1','6','',r"""%s</td><td>(\d+)""",'http'),
# ('http://www.66ip.cn/areaindex_2/%s.html','1','6','',r"""%s</td><td>(\d+)""",'http'),
# ('http://www.66ip.cn/areaindex_3/%s.html','1','6','',r"""%s</td><td>(\d+)""",'http'),
# ('http://www.66ip.cn/areaindex_4/%s.html','1','6','',r"""%s</td><td>(\d+)""",'http'),
# ('http://www.66ip.cn/areaindex_5/%s.html','1','6','',r"""%s</td><td>(\d+)""",'http'),
# ('http://www.66ip.cn/areaindex_6/%s.html','1','6','',r"""%s</td><td>(\d+)""",'http'),
# ('http://www.66ip.cn/areaindex_7/%s.html','1','6','',r"""%s</td><td>(\d+)""",'http'),
# ('http://www.66ip.cn/areaindex_8/%s.html','1','6','',r"""%s</td><td>(\d+)""",'http'),
# ('http://www.66ip.cn/areaindex_9/%s.html','1','6','',r"""%s</td><td>(\d+)""",'http'),
# ('http://www.66ip.cn/areaindex_10/%s.html','1','6','',r"""%s</td><td>(\d+)""",'http'),
# ('http://www.66ip.cn/areaindex_11/%s.html','1','6','',r"""%s</td><td>(\d+)""",'http'),
# ('http://www.66ip.cn/areaindex_12/%s.html','1','6','',r"""%s</td><td>(\d+)""",'http'),
# ('http://www.66ip.cn/areaindex_13/%s.html','1','6','',r"""%s</td><td>(\d+)""",'http'),
# ('http://www.66ip.cn/areaindex_14/%s.html','1','6','',r"""%s</td><td>(\d+)""",'http'),
# ('http://www.66ip.cn/areaindex_15/%s.html','1','6','',r"""%s</td><td>(\d+)""",'http'),
# ('http://www.66ip.cn/areaindex_16/%s.html','1','6','',r"""%s</td><td>(\d+)""",'http'),
# ('http://www.66ip.cn/areaindex_17/%s.html','1','6','',r"""%s</td><td>(\d+)""",'http'),
# ('http://www.66ip.cn/areaindex_18/%s.html','1','6','',r"""%s</td><td>(\d+)""",'http'),
# ('http://www.66ip.cn/areaindex_19/%s.html','1','6','',r"""%s</td><td>(\d+)""",'http'),
# ('http://www.66ip.cn/areaindex_20/%s.html','1','6','',r"""%s</td><td>(\d+)""",'http'),
# ('http://www.66ip.cn/areaindex_21/%s.html','1','6','',r"""%s</td><td>(\d+)""",'http'),
# ('http://www.66ip.cn/areaindex_22/%s.html','1','6','',r"""%s</td><td>(\d+)""",'http'),
# ('http://www.66ip.cn/areaindex_23/%s.html','1','6','',r"""%s</td><td>(\d+)""",'http'),
# ('http://www.66ip.cn/areaindex_24/%s.html','1','6','',r"""%s</td><td>(\d+)""",'http'),
# ('http://www.66ip.cn/areaindex_25/%s.html','1','6','',r"""%s</td><td>(\d+)""",'http'),
# ('http://www.66ip.cn/areaindex_26/%s.html','1','6','',r"""%s</td><td>(\d+)""",'http'),
# ('http://www.66ip.cn/areaindex_27/%s.html','1','6','',r"""%s</td><td>(\d+)""",'http'),
# ('http://www.66ip.cn/areaindex_28/%s.html','1','6','',r"""%s</td><td>(\d+)""",'http'),
# ('http://www.66ip.cn/areaindex_29/%s.html','1','6','',r"""%s</td><td>(\d+)""",'http'),
# ('http://www.66ip.cn/areaindex_30/%s.html','1','6','',r"""%s</td><td>(\d+)""",'http'),
# ('http://www.66ip.cn/areaindex_31/%s.html','1','6','',r"""%s</td><td>(\d+)""",'http'),
# ('http://www.66ip.cn/areaindex_32/%s.html','1','6','',r"""%s</td><td>(\d+)""",'http'),
# ('http://www.66ip.cn/areaindex_33/%s.html','1','6','',r"""%s</td><td>(\d+)""",'http'),
# ('http://www.66ip.cn/areaindex_34/%s.html','1','1','',r"""%s</td><td>(\d+)""",'http'),


#无法访问的网址
# ('http://freeproxylists.net/', '', ''),







]
	
		
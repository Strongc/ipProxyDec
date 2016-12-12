# IP代理检测的方法


## 一.目标IP
* 1.特定地区的IP
* 2.批量代理的IP
* 3.基于云服务的恶意IP


##二.代理类型:
* 1.VPN

* 2.Tor
  Tor节点
* 3.DCH
  服务提供商,以及数据中心会提供匿名服务
* 4.PUB
  公共代理,通过管理员通过代理软件在特殊端口进行监听,相对于vpn功能比较局限.
* 5.WEB
  简单的基于网页的代理
## 三.识别情况

|&nbsp;|REMOTE_ADDR|HTTP_X_FORWARDED_FOR|隐藏身份|识别难度|
|---|---|---|---|---|
|未使用代理|真实IP|无|无|&nbsp;|
|透明代理|代理IP|真实IP|无|易|
|匿名代理|代理IP|代理IP|是|易|
|欺诈代理|代理IP|随机IP|是|易|
|高匿名代理|代理IP|无|是|难|

##四 获得代理的途径
* 4.1 网上免费代理

* 4.2 NMAP扫描出可用代理

* 4.3 购买收费代理

* 4.4 使用云服务器搭建代理
如亚马逊,以及国内云服务商
* 4.5 使用Tor+VPN混合

##五.策略
总体策略:黑名单


###5.1在线检测(暂不细数)
* 接受报文分析
通过抓取数据包的方式, 如请求头(但是请求头可以被伪造),以及keep-alive 是否是长连接(因为部分廉价的代理是不会采用长连接).
* 基于用户行为分析
通过在同一个地点多个账号的同步相关操作行为,列为可疑行为



###5.2离线检测
* NMAP扫描
 通过检测ip的端口信息,如abyss,http-proxy,privoxy,
A.检测一个主机 (未知端口)耗时60s 甚至以上.
B.在已知端口的情况下http代理要20秒,socks耗时会少一些.
C.如果目标没有代理 ,会检测很快. 256 IP addresses (256 hosts up) scanned in 26.99 seconds
 
 nmap包含一个检测socket代理的脚本,其具体思路是访问1080以及9050端口,是否存在socket4或者socket5协议,通过该协议访问google主页,通过返回情况,来进行判断.准确度较高
 
* ZMAP配合脚本扫描
 通过端口找出开放的可能代理端口的状态,然后用脚本直接去检测(速度较快,准确度相对低)
 
 * Tor节点
 对于Tor节点,识别出口(exit)节点[https://collector.torproject.org/](https://collector.torproject.org/)


###5.3代理库
来自于网上的代理,maxmind的提供专门检测代理[GeoIP2 Anonymous IP Database](https://www.maxmind.com/en/geoip2-anonymous-ip-database)以及是否tor的数据库提供

###5.4免费代理库



##附录
###NMAP语法

测试端口 58.221.249.205  

端口:8000

检测脚本 socks-open-proxy 
	      http-open-proxy		
测试用例: <pre>nmap -v -sS -p 1080 --script socks-open-proxy 192.168.0.1/24</pre>
常见的判断ip的报文信息
                        'CLIENT_IP', 
                        'FORWARDED', 
                          'FORWARDED_FOR', 
                          'FORWARDED_FOR_IP', 
                          'HTTP_CLIENT_IP', 
                          'HTTP_FORWARDED', 
                          'HTTP_FORWARDED_FOR', 
                          'HTTP_FORWARDED_FOR_IP', 
                          'HTTP_PC_REMOTE_ADDR', 
                          'HTTP_PROXY_CONNECTION',
                          'HTTP_VIA', 
                          'HTTP_X_FORWARDED', 
                          'HTTP_X_FORWARDED_FOR', 
                          'HTTP_X_FORWARDED_FOR_IP', 
                          'HTTP_X_IMFORWARDS', 
                          'HTTP_XROXY_CONNECTION', 
                          'VIA', 
                          'X_FORWARDED', 
                          'X_FORWARDED_FOR'
                          
### nmap速度测试

<pre> nmap -p 9050 -T4 -n -Pn --script socks-open-proxy 132.123.23.2/20 </pre>
耗时:4096 IP addresses (4096 hosts up) scanned in 416.30 seconds






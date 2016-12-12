# IP代理检测方法


## 一.目标IP

* 批量代理的IP
* 基于云服务的恶意IP


##二.代理类型:

* HTTP/HTTPS

* SOCKS4/SOCKS5

* VPN

* Tor
  Tor节点


## 三.IP来源

* 网络

* 京东上报数据


## 四.HTTP/HTTPS代理检测手段

### 4.1 在线检测

* 接受报文分析
通过抓取数据包的方式, 如请求头(但是请求头可以被伪造),以及keep-alive 是否是长连接(因为部分廉价的代理是不会采用长连接).

|&nbsp;|REMOTE_ADDR|HTTP_X_FORWARDED_FOR|隐藏身份|识别难度|
|---|---|---|---|---|
|未使用代理|真实IP|无|无|&nbsp;|
|透明代理|代理IP|真实IP|无|易|
|匿名代理|代理IP|代理IP|是|易|
|欺诈代理|代理IP|随机IP|是|易|
|高匿名代理|代理IP|无|是|难|

* 基于用户行为分析
通过在同一个地点多个账号的同步相关操作行为,列为可疑行为

### 4.2 离线检测

* NMAP扫描
 检测IP的端口信息,如abyss,http-proxy,privoxy,
A.检测一个主机 (未知端口)耗时60s 甚至以上.
B.在已知端口的情况下http代理要20秒,socks耗时会少一些.
C.如果目标没有代理 ,会检测很快.

* ZMAP配合脚本扫描
 ZMAP找出端口,然后用脚本直接去检测(速度较快,准确度相对低)
 
* 代理库

	第三方maxmind的提供专门检测代理[GeoIP2 Anonymous IP Database](https://www.maxmind.com/en/geoip2-anonymous-ip-database)以及是否tor的数据库提供
 
## 五.SOCKS4/SOCKS5代理检测手段

* 已知端口
	使用对应的socks协议进行转发判断返回情况

* 未知端口
       A.使用NMAP确定是否存在端口运行代理的协议
       B.使用常见的socks端口进行检测(1080,5090)

 

## 六.Tor节点代理检测手段

对于Tor节点,识别出口(exit)节点[https://collector.torproject.org/](https://collector.torproject.org/),Tor节点常用标示为9050.
		

		

		
</br>
</br>
</br>
</br>

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
                          
### NMAP速度测试

<pre> nmap -p 9050 -T4 -n -Pn --script socks-open-proxy 132.123.23.2/20 </pre>
耗时:4096 IP addresses (4096 hosts up) scanned in 416.30 seconds






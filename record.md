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
## 识别情况

<table style="height: 324px; width: 557px;" border="1" cellspacing="0" cellpadding="0">
<tbody>
<tr>
<td style="text-align: center;">
<p><span style="font-size: 15px;">&nbsp;</span></p>
</td>
<td style="text-align: center;">
<p lang="en-US"><span style="font-size: 15px;">REMOTE_ADDR</span></p>
</td>
<td style="text-align: center;">
<p lang="en-US"><span style="font-size: 15px;">HTTP_X_FORWARDED_FOR</span></p>
</td>
<td style="text-align: center;">
<p><span style="font-size: 15px;">隐藏身份</span></p>
</td>
<td style="text-align: center;">
<p><span style="font-size: 15px;">识别难度</span></p>
</td>
</tr>
<tr>
<td style="text-align: center;">
<p><span style="font-size: 15px;">未使用代理</span></p>
</td>
<td style="text-align: center;">
<p><span style="font-size: 15px;" lang="zh-CN">真实<span lang="en-US">IP</span></span></p>
</td>
<td style="text-align: center;">
<p><span style="font-size: 15px;">无</span></p>
</td>
<td style="text-align: center;">
<p><span style="font-size: 15px;">无</span></p>
<iframe id="tmp_downloadhelper_iframe" style="display: none;"></iframe></td>
<td style="text-align: center;">
<p><span style="font-size: 15px;">&nbsp;</span></p>
</td>
</tr>
<tr>
<td style="text-align: center;">
<p><span style="font-size: 15px;">透明代理</span></p>
</td>
<td style="text-align: center;">
<p><span style="font-size: 15px;" lang="zh-CN">代理<span lang="en-US">IP</span></span></p>
</td>
<td style="text-align: center;">
<p><span style="font-size: 15px;" lang="zh-CN">真实<span lang="en-US">IP</span></span></p>
</td>
<td style="text-align: center;">
<p><span style="font-size: 15px;">无</span></p>
</td>
<td style="text-align: center;">
<p><span style="font-size: 15px;">易</span></p>
</td>
</tr>
<tr>
<td style="text-align: center;">
<p><span style="font-size: 15px;">匿名代理</span></p>
</td>
<td style="text-align: center;">
<p><span style="font-size: 15px;" lang="zh-CN">代理<span lang="en-US">IP</span></span></p>
</td>
<td style="text-align: center;">
<p><span style="font-size: 15px;" lang="zh-CN">代理<span lang="en-US">IP</span></span></p>
</td>
<td style="text-align: center;">
<p><span style="font-size: 15px;">是</span></p>
</td>
<td style="text-align: center;">
<p><span style="font-size: 15px;">易</span></p>
</td>
</tr>
<tr>
<td style="text-align: center;">
<p><span style="font-size: 15px;">欺诈代理</span></p>
</td>
<td style="text-align: center;">
<p><span style="font-size: 15px;" lang="zh-CN">代理<span lang="en-US">IP</span></span></p>
</td>
<td style="text-align: center;">
<p><span style="font-size: 15px;" lang="zh-CN">随机<span lang="en-US">IP</span></span></p>
</td>
<td style="text-align: center;">
<p><span style="font-size: 15px;">是</span></p>
</td>
<td style="text-align: center;">
<p><span style="font-size: 15px;">易</span></p>
</td>
</tr>
<tr>
<td style="text-align: center;">
<p><span style="font-size: 15px;">高匿名代理</span></p>
</td>
<td style="text-align: center;">
<p><span style="font-size: 15px;" lang="zh-CN">代理<span lang="en-US">IP</span></span></p>
</td>
<td style="text-align: center;">
<p><span style="font-size: 15px;">无</span></p>
</td>
<td style="text-align: center;">
<p><span style="font-size: 15px;">是</span></p>
</td>
<td style="text-align: center;">
<p><span style="font-size: 15px;">难</span></p>
</td>
</tr>
</tbody>
</table>
##三.策略
总体策略:黑名单()


###在线
* 接受报文分析
通过抓取数据包的方式, 如请求头(但是请求头可以被伪造),以及keep-alive 是否是长连接(因为部分廉价的代理是不会采用长连接).
* 基于用户行为分析
通过在同一个地点多个账号的同步相关操作行为,列为可疑行为



###离线
 通过检测ip的端口信息,如abyss,http-proxy,privoxy
 
 nmap包含一个检测socket代理的脚本,其具体思路是访问1080以及9050端口,是否存在socket4或者socket5协议,通过该协议访问google主页,通过返回情况,来进行判断.



###代理库
来自于网上的代理,maxmind的提供专门检测代理[GeoIP2 Anonymous IP Database](https://www.maxmind.com/en/geoip2-anonymous-ip-database)以及是否tor的数据库提供



##附录
###NMAP语法

测试端口 58.221.249.205  

端口:8000

检测脚本 socks-open-proxy 
	      http-open-proxy		
测试用例: <pre>nmap -v -sS -p 1080 --script socks-open-proxy 192.168.0.1/24</pre>







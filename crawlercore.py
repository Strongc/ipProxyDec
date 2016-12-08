#!/usr/bin/python
#coding:utf-8

import connecttool
import re
import config
import connectpool,ocrtool
def getfullcode(path='http://ip.zdaye.com/'):
    from selenium import webdriver
    driver = webdriver.PhantomJS()
    driver.get(path)
    result= driver.page_source
    driver.quit()
    return result

def getIPfromPage(page,rules=None):
    isgettoken=False
    token=None
    if rules[3]=='':
        rule=r'(?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?![\.\d])'
    else:
        rule=rules[3]
    portrule=rules[4]
    porttype=rules[6]
    reip = re.compile(rule)

    iplist=set()
    ips=reip.findall(page)
    for ip in ips:
        port='80'
        if portrule=='':
            pass
        else:

            prule=portrule % (ip)

            # template=re.compile(prule)
            # port =template.findall(page)
            port=re.search(prule, page).groups()[0]

            # report= re.compile(prule)
            # print prule
            # print report
            # print page
            #
            # port=report.findall(page)[0]
            if porttype == '1':
                picurl=port
                port_picrule=rules[7]
                if port_picrule!='' and isgettoken==False:
                    token = re.search(port_picrule, page).groups()[0]
                    isgettoken=True
                    print 'token',token

                data=getStaticHtml(picurl,token)
                picpath=ocrtool.downloadFile(data=data, name=None, type=None, url=picurl)
                port=ocrtool.getverifyimg(name=picpath)


        print ip,port
        iplist.add((ip,port))


    return iplist

def getStaticHtml(path,cookie=None):
    conpool=connectpool.getObject()
    print path
    if cookie is not None:
        conpool.setHeader('Cookie',cookie)
        head, result = conpool.getConnect(URL=path)
    else:
        head,result=conpool.getConnect(URL=path)
    return result






def ruletowebsite(rules):
    websites=[]
    if rules[1]=='':
        websites.append((rules[0],rules))
    else:

        for i in range(int(rules[1]), int(rules[2]) + 1):
            result = rules[0] % (i)
            websites.append((result,rules))
    return websites

texto="""
<!DOCTYPE html>
<html lang="zh-cn">
    <head>
        <meta charset="utf-8"/>
        <meta http-equiv="X-UA-Compatible" content="IE=edge"/>
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no"/>
            <meta name="keywords" content="免费代理,蚂蚁代理,代理服务器,高速http代理,IP提取器,爬虫代理,ip代理,国外代理服务器,免费代理服务器,免费代理ip,高匿代理ip,免费代理ip,代理服务器ip,代理地址,代理列表,最新免费代理ip"/>
    <meta name="description" content="免费代理|蚂蚁代理|代理服务器|高速http代理|IP提取器|爬虫代理|ip代理|国外代理服务器|免费代理服务器|免费代理ip|高匿代理ip|最新代理ip|免费代理ip|代理服务器ip|代理服务|代理地址|代理列表|最新免费代理ip" />
    <title>免费代理-蚂蚁代理-最新免费代理ip,高质量代理ip</title>
        <!-- Bootstrap -->
        <link href="http://static.mayidaili.com/css/bootstrap.min.css" rel="stylesheet"/>
        <link href="http://static.mayidaili.com/css/selectize.bootstrap3.css" rel="stylesheet"/>
        <link href="http://static.mayidaili.com/css/highlight.css" rel="stylesheet"/>
        <link href="http://www.mayidaili.com/css/style.css?v=1.0.5" rel="stylesheet"/>
        <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
        <!--[if lt IE 9]>
        <script src="http://static.mayidaili.com/js/html5shiv.min.js"></script>
        <script src="http://static.mayidaili.com/js/respond.min.js"></script>
        <script src="http://static.mayidaili.com/js/placeholders.min.js"></script>
        <script src="http://static.mayidaili.com/js/json2.js"></script>
        <![endif]-->
    </head>
    <body>
            <!-- black line from top -->
    <div class="header-line"></div>
     <div class="container">
     	<div class="row mt10">
     		<div class="col-md-7 text-right">
     		     		</div>
     		<div class="col-md-2 text-right">
     		     		</div>
     		<div class="col-md-3 text-right">
     			        QQ群：424699147 <a target="_blank" href="http://shang.qq.com/wpa/qunwpa?idkey=7a4828611af5747b8203fe79b27710fb723be2a7b23f423ba7ad91ae2ba67d1d">
            			<img border="0" src="http://pub.idqqimg.com/wpa/images/group.png" alt="点此加入蚂蚁代理官方QQ群" title="加群请写明原由" data-toggle="tooltip" data-placement="left"></a>
     		</div>
     	</div>
     </div>
    <nav class="navbar">
        <div class="container">
            <div class="row">
                <div class="col-md-4">
                	<div class="pull-left"><img src="http://static.mayidaili.com/img/logo.png" width="50" height="50" /></div>
                	<div class="pull-left logo-text">蚂蚁代理</div>
                </div>
                <div class="col-md-8">
                    <ul class="nav navbar-nav navbar-right">
                        <li class="">
                            <a href="http://www.mayidaili.com/">首页</a>
                        </li>
                        <li class="">
                            <a href="http://www.mayidaili.com/dynamic">高质量动态代理</a>
                        </li>
                        <li class="active">
                            <a href="http://www.mayidaili.com/free">免费代理</a>
                        </li>
                        <li class="">
                                                    </li>
                        <li class="">
                            <a href="http://www.mayidaili.com/share/">每日分享</a>
                        </li>
                        <li class="">
                            <a href="http://www.mayidaili.com/baike/">代理百科</a>
                        </li>
                        <li class="">
                            <a href="http://www.mayidaili.com/proxy/check-online/">在线检测</a>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    </nav>
        <div class="page-free-banner">
            <div class="container">
                <h1>免费代理</h1>
                <p>免费代理都是通过扫描网络上的公共代理得来，由于没有用户名和密码认证，用的人特别多，故称“万人骑”，因此在速度和稳定性上都没有保障</p>
				<p>本站免费代理均可免费查询使用，免费代理本身并不收费，但是如果您需要API批量获取接口，请购买API接口服务，<u>注意：通过API接口获取到的代理IP的质量与在线查询的一样</u></p>
                <p>实时扫描免费代理数量：<strong class="fz20">48823</strong></p>
            </div>
        </div>
        <div class="container">
			<ol class="breadcrumb text-right">
			  <li class="active">搜索免费代理</li>
			  <li><a href="http://www.mayidaili.com/free/api-link">生成API连接</a></li>
			  <li><a href="http://www.mayidaili.com/free/buy-api">购买API接口</a></li>
			</ol>
            <div class="row">
                <div class="col-md-3">
                    <div class="panel panel-default">
                    	<p class="nav-title-sm">按匿名度选择</p>
                    	<div class="p5">
							<a class="free-tags" href="http://www.mayidaili.com/free/anonymous/高匿">高匿</a>
							<a class="free-tags" href="http://www.mayidaili.com/free/anonymous/普匿">普匿</a>
							<a class="free-tags" href="http://www.mayidaili.com/free/anonymous/透明">透明</a>
						</div>
                    	<p class="nav-title-sm">按类型选择</p>
                    	<div class="p5">
							<a class="free-tags" href="http://www.mayidaili.com/free/education">高校代理</a>
						</div>
                    	<p class="nav-title-sm">按端口选择</p>
                    	<div class="p5">
	                    	<a class="free-tags" href="http://www.mayidaili.com/free/port/8081">8081</a>
	                    	<a class="free-tags" href="http://www.mayidaili.com/free/port/8808">8808</a>
	                    	<a class="free-tags" href="http://www.mayidaili.com/free/port/8909">8909</a>
	                    	<a class="free-tags" href="http://www.mayidaili.com/free/port/9100">9100</a>
	                    	<a class="free-tags" href="http://www.mayidaili.com/free/port/3127">3127</a>
	                    	<a class="free-tags" href="http://www.mayidaili.com/free/port/8008">8008</a>
	                    	<a class="free-tags" href="http://www.mayidaili.com/free/port/1234">1234</a>
	                    	<a class="free-tags" href="http://www.mayidaili.com/free/port/8082">8082</a>
	                    	<a class="free-tags" href="http://www.mayidaili.com/free/port/6789">6789</a>
	                    	<a class="free-tags" href="http://www.mayidaili.com/free/port/1080">1080</a>
							</br>
                    		<a class="free-tags" href="http://www.mayidaili.com/free/fiveport">随机五位端口</a>
                    	</div>
                    	<p class="nav-title-sm">按地区选择</p>
                    	<div class="free-bylocation">
							<select id="location_select_free" style="width:100%;" placeholder="输入关键字查找"></select>
	                        <script>var hotLocations=[{"alias":"asia,yazhou,yz,亚洲","fullstyle":"亚洲","id":"1-6255147"},{"alias":"africa,feizhou,fz,非洲","fullstyle":"非洲","id":"1-6255146"},{"alias":"north america,beimeizhou,bmz,北美洲","fullstyle":"北美洲","id":"1-6255149"},{"alias":"china,zhongguo,zg,中国","fullstyle":"亚洲,中国","id":"2-1814991"},{"alias":"united states,meiguo,mg,美国","fullstyle":"北美洲,美国","id":"2-6252001"},{"alias":"russia,eluosi,els,俄罗斯","fullstyle":"欧洲,俄罗斯","id":"2-2017370"},{"alias":"北京市,beijingshi,bjs,北京市","fullstyle":"中国,北京市","id":"3-2038349"},{"alias":"上海市,shanghaishi,shs,上海市","fullstyle":"中国,上海市","id":"3-1796231"},{"alias":"广州市,guangzhoushi,gzs,广州市","fullstyle":"广东省,广州市","id":"4-1809857"}];</script>
                    	</div>
						<div class="p5">
	                    	<a class="free-tags" href="http://www.mayidaili.com/free/location/浙江省-3-1784764">浙江省</a>
	                    	<a class="free-tags" href="http://www.mayidaili.com/free/location/北京市-3-2038349">北京市</a>
	                    	<a class="free-tags" href="http://www.mayidaili.com/free/location/山东省-3-1796328">山东省</a>
	                    	<a class="free-tags" href="http://www.mayidaili.com/free/location/河南省-3-1808520">河南省</a>
	                    	<a class="free-tags" href="http://www.mayidaili.com/free/location/福建省-3-1811017">福建省</a>
	                    	<a class="free-tags" href="http://www.mayidaili.com/free/location/江苏省-3-1806260">江苏省</a>
	                    	<a class="free-tags" href="http://www.mayidaili.com/free/location/上海市-3-1796231">上海市</a>
	                    	<a class="free-tags" href="http://www.mayidaili.com/free/location/江西省-3-1806222">江西省</a>
	                    	<a class="free-tags" href="http://www.mayidaili.com/free/location/广东省-3-1809935">广东省</a>
	                    	<a class="free-tags" href="http://www.mayidaili.com/free/location/湖南省-3-1806691">湖南省</a>
	                    	<a class="free-tags" href="http://www.mayidaili.com/free/location/辽宁省-3-2036115">辽宁省</a>
	                    	<a class="free-tags" href="http://www.mayidaili.com/free/location/四川省-3-1794299">四川省</a>
	                    	<a class="free-tags" href="http://www.mayidaili.com/free/location/贵州省-3-1809445">贵州省</a>
	                    	<a class="free-tags" href="http://www.mayidaili.com/free/location/云南省-3-1785694">云南省</a>
	                    	<a class="free-tags" href="http://www.mayidaili.com/free/location/黑龙江省-3-2036965">黑龙江省</a>
	                    	<a class="free-tags" href="http://www.mayidaili.com/free/location/广西壮族自治区-3-1809867">广西壮族自治区</a>
	                    	<a class="free-tags" href="http://www.mayidaili.com/free/location/陕西省-3-1796480">陕西省</a>
	                    	<a class="free-tags" href="http://www.mayidaili.com/free/location/重庆市-3-1814905">重庆市</a>
	                    	<a class="free-tags" href="http://www.mayidaili.com/free/location/河北省-3-1808773">河北省</a>
	                    	<a class="free-tags" href="http://www.mayidaili.com/free/location/湖北省-3-1806949">湖北省</a>
	                    	<a class="free-tags" href="http://www.mayidaili.com/free/location/内蒙古自治区-3-2035607">内蒙古自治区</a>
	                    	<a class="free-tags" href="http://www.mayidaili.com/free/location/吉林省-3-2036500">吉林省</a>
	                    	<a class="free-tags" href="http://www.mayidaili.com/free/location/安徽省-3-1818058">安徽省</a>
	                    	<a class="free-tags" href="http://www.mayidaili.com/free/location/山西省-3-1795912">山西省</a>
	                    	<a class="free-tags" href="http://www.mayidaili.com/free/location/新疆维吾尔自治区-3-1529047">新疆维吾尔自治区</a>
	                    	<a class="free-tags" href="http://www.mayidaili.com/free/location/甘肃省-3-1810676">甘肃省</a>
	                    	<a class="free-tags" href="http://www.mayidaili.com/free/location/天津市-3-1792943">天津市</a>
	                    	<a class="free-tags" href="http://www.mayidaili.com/free/location/海南省-3-1809054">海南省</a>
	                    	<a class="free-tags" href="http://www.mayidaili.com/free/location/青海省-3-1280239">青海省</a>
	                    	<a class="free-tags" href="http://www.mayidaili.com/free/location/宁夏回族自治区-3-1799355">宁夏回族自治区</a>
	                    	<a class="free-tags" href="http://www.mayidaili.com/free/location/西藏自治区-3-1279685">西藏自治区</a>
							<a class="free-tags" href="http://www.mayidaili.com/free/location/台湾省-2-1668284">台湾省</a>
						</div>
                    </div>
                </div>
                <div class="col-md-9">
                <table class="table table-hover table-bordered table-striped">
                    <thead>
                        <tr>
                            <th>IP地址</th>
                            <th>端口</th>
                            <th>匿名度</th>
                            <th>所在国家/地区</th>
                            <th>地理位置</th>
                            <th>连接时间</th>
                            <th>上次验证时间</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>111.62.251.17
							</td>
                            <td>
								<img width="80" height="20" class="js-proxy-img" data-uri="http://www.mayidaili.com/free/img/1/51402/TI3fYPdCR3wMQTSpF5Clqw" />
							</td>
                            <td>
                                    <a href="http://www.mayidaili.com/free/anonymous/透明">透明</a>
                            </td>
                            <td>
                                <img width="16" height="11" src="http://static.mayidaili.com/img/flags/CN.png" class="mr5" />
                                    <a href="http://www.mayidaili.com/free/location/中国-2-1814991">中国</a>
                            </td>
                            <td>
									<a href="http://www.mayidaili.com/free/location/中国,河北省-3-1808773">河北省</a>
									<a href="http://www.mayidaili.com/free/location/中国,河北省,保定市-4-1816969">保定市</a>

							</td>
                            <td>
                                <span class="label label-success">26</span>
                                ms
							</td>
                            <td>
                                <time class="timeago">刚刚</time>
                            </td>
                        </tr>
                        <tr>
                            <td>61.179.105.11
							</td>
                            <td>
								<img width="80" height="20" class="js-proxy-img" data-uri="http://www.mayidaili.com/free/img/1/39089/F2nfYnCI3OTYLdmslXOZOg" />
							</td>
                            <td>
                                    <a href="http://www.mayidaili.com/free/anonymous/透明">透明</a>
                            </td>
                            <td>
                                <img width="16" height="11" src="http://static.mayidaili.com/img/flags/CN.png" class="mr5" />
                                    <a href="http://www.mayidaili.com/free/location/中国-2-1814991">中国</a>
                            </td>
                            <td>
									<a href="http://www.mayidaili.com/free/location/中国,山东省-3-1796328">山东省</a>
									<a href="http://www.mayidaili.com/free/location/中国,山东省,烟台市-4-1787083">烟台市</a>

							</td>
                            <td>
                                <span class="label label-success">52</span>
                                ms
							</td>
                            <td>
                                <time class="timeago">刚刚</time>
                            </td>
                        </tr>
                        <tr>
                            <td>113.18.193.13
							</td>
                            <td>
								<img width="80" height="20" class="js-proxy-img" data-uri="http://www.mayidaili.com/free/img/1/38850/tsdNPwRU7VKmuc6ETSdicA" />
							</td>
                            <td>
                                    <a href="http://www.mayidaili.com/free/anonymous/普匿">普匿</a>
                            </td>
                            <td>
                                <img width="16" height="11" src="http://static.mayidaili.com/img/flags/CN.png" class="mr5" />
                                    <a href="http://www.mayidaili.com/free/location/中国-2-1814991">中国</a>
                            </td>
                            <td>
									<a href="http://www.mayidaili.com/free/location/中国,福建省-3-1811017">福建省</a>
									<a href="http://www.mayidaili.com/free/location/中国,福建省,福州市-4-1810815">福州市</a>

							</td>
                            <td>
                                <span class="label label-success">109</span>
                                ms
							</td>
                            <td>
                                <time class="timeago">刚刚</time>
                            </td>
                        </tr>
                        <tr>
                            <td>122.72.32.75
							</td>
                            <td>
								<img width="80" height="20" class="js-proxy-img" data-uri="http://www.mayidaili.com/free/img/1/53575/PuhGqx0y8_CT4z-noUyG1Q" />
							</td>
                            <td>
                                    <a href="http://www.mayidaili.com/free/anonymous/高匿">高匿</a>
                            </td>
                            <td>
                                <img width="16" height="11" src="http://static.mayidaili.com/img/flags/CN.png" class="mr5" />
                                    <a href="http://www.mayidaili.com/free/location/中国-2-1814991">中国</a>
                            </td>
                            <td>
									<a href="http://www.mayidaili.com/free/location/中国,重庆市-3-1814905">重庆市</a>


							</td>
                            <td>
                                <span class="label label-success">138</span>
                                ms
							</td>
                            <td>
                                <time class="timeago">刚刚</time>
                            </td>
                        </tr>
                        <tr>
                            <td>221.204.21.65
							</td>
                            <td>
								<img width="80" height="20" class="js-proxy-img" data-uri="http://www.mayidaili.com/free/img/1/28400/AI5_AXuxcEleXddK1xVI2g" />
							</td>
                            <td>
                                    <a href="http://www.mayidaili.com/free/anonymous/透明">透明</a>
                            </td>
                            <td>
                                <img width="16" height="11" src="http://static.mayidaili.com/img/flags/CN.png" class="mr5" />
                                    <a href="http://www.mayidaili.com/free/location/中国-2-1814991">中国</a>
                            </td>
                            <td>
									<a href="http://www.mayidaili.com/free/location/中国,山西省-3-1795912">山西省</a>
									<a href="http://www.mayidaili.com/free/location/中国,山西省,太原市-4-1793510">太原市</a>

							</td>
                            <td>
                                <span class="label label-success">34</span>
                                ms
							</td>
                            <td>
                                <time class="timeago">刚刚</time>
                            </td>
                        </tr>
                        <tr>
                            <td>218.29.187.4
							</td>
                            <td>
								<img width="80" height="20" class="js-proxy-img" data-uri="http://www.mayidaili.com/free/img/1/7341/7UOMuI0e0pC0aRoJ361xvA" />
							</td>
                            <td>
                                    <a href="http://www.mayidaili.com/free/anonymous/透明">透明</a>
                            </td>
                            <td>
                                <img width="16" height="11" src="http://static.mayidaili.com/img/flags/CN.png" class="mr5" />
                                    <a href="http://www.mayidaili.com/free/location/中国-2-1814991">中国</a>
                            </td>
                            <td>
									<a href="http://www.mayidaili.com/free/location/中国,河南省-3-1808520">河南省</a>
									<a href="http://www.mayidaili.com/free/location/中国,河南省,商丘市-4-1796132">商丘市</a>

							</td>
                            <td>
                                <span class="label label-success">35</span>
                                ms
							</td>
                            <td>
                                <time class="timeago">刚刚</time>
                            </td>
                        </tr>
                        <tr>
                            <td>175.6.10.15
							</td>
                            <td>
								<img width="80" height="20" class="js-proxy-img" data-uri="http://www.mayidaili.com/free/img/1/26279/k_EFMloGhNDIurqZUKAueA" />
							</td>
                            <td>
                                    <a href="http://www.mayidaili.com/free/anonymous/透明">透明</a>
                            </td>
                            <td>
                                <img width="16" height="11" src="http://static.mayidaili.com/img/flags/CN.png" class="mr5" />
                                    <a href="http://www.mayidaili.com/free/location/中国-2-1814991">中国</a>
                            </td>
                            <td>
									<a href="http://www.mayidaili.com/free/location/中国,湖南省-3-1806691">湖南省</a>
									<a href="http://www.mayidaili.com/free/location/中国,湖南省,长沙市-4-1815551">长沙市</a>

							</td>
                            <td>
                                <span class="label label-success">78</span>
                                ms
							</td>
                            <td>
                                <time class="timeago">刚刚</time>
                            </td>
                        </tr>
                        <tr>
                            <td>185.28.193.95
							</td>
                            <td>
								<img width="80" height="20" class="js-proxy-img" data-uri="http://www.mayidaili.com/free/img/1/54350/GdolUlrxz5dOgwAHh5dtbg" />
							</td>
                            <td>
                                    <a href="http://www.mayidaili.com/free/anonymous/普匿">普匿</a>
                            </td>
                            <td>
                                <img width="16" height="11" src="http://static.mayidaili.com/img/flags/CZ.png" class="mr5" />
                                    <a href="http://www.mayidaili.com/free/location/捷克共和国-2-3077311">捷克共和国</a>
                            </td>
                            <td>



							</td>
                            <td>
                                <span class="label label-success">661</span>
                                ms
							</td>
                            <td>
                                <time class="timeago">刚刚</time>
                            </td>
                        </tr>
                        <tr>
                            <td>54.215.198.81
							</td>
                            <td>
								<img width="80" height="20" class="js-proxy-img" data-uri="http://www.mayidaili.com/free/img/1/31986/lL6Ii3_HBIxfsChL5lhF3w" />
							</td>
                            <td>
                                    <a href="http://www.mayidaili.com/free/anonymous/高匿">高匿</a>
                            </td>
                            <td>
                                <img width="16" height="11" src="http://static.mayidaili.com/img/flags/US.png" class="mr5" />
                                    <a href="http://www.mayidaili.com/free/location/美国-2-6252001">美国</a>
                            </td>
                            <td>
									<a href="http://www.mayidaili.com/free/location/美国,加利福尼亚州-3-5332921">加利福尼亚州</a>
									<a href="http://www.mayidaili.com/free/location/美国,加利福尼亚州,San Jose-4-5392171">San Jose</a>

							</td>
                            <td>
                                <span class="label label-success">695</span>
                                ms
							</td>
                            <td>
                                <time class="timeago">刚刚</time>
                            </td>
                        </tr>
                        <tr>
                            <td>111.92.227.144
							</td>
                            <td>
								<img width="80" height="20" class="js-proxy-img" data-uri="http://www.mayidaili.com/free/img/1/21193/h-XTkN4vl1B47pTTsPbyKw" />
							</td>
                            <td>
                                    <a href="http://www.mayidaili.com/free/anonymous/透明">透明</a>
                            </td>
                            <td>
                                <img width="16" height="11" src="http://static.mayidaili.com/img/flags/HK.png" class="mr5" />
                                    <a href="http://www.mayidaili.com/free/location/香港-2-1819730">香港</a>
                            </td>
                            <td>



							</td>
                            <td>
                                <span class="label label-danger">1663</span>
                                ms
							</td>
                            <td>
                                <time class="timeago">刚刚</time>
                            </td>
                        </tr>
                        <tr>
                            <td>201.174.52.29
							</td>
                            <td>
								<img width="80" height="20" class="js-proxy-img" data-uri="http://www.mayidaili.com/free/img/1/32797/XLwnWVpcCsRwlzO85KmRBA" />
							</td>
                            <td>
                                    <a href="http://www.mayidaili.com/free/anonymous/透明">透明</a>
                            </td>
                            <td>
                                <img width="16" height="11" src="http://static.mayidaili.com/img/flags/MX.png" class="mr5" />
                                    <a href="http://www.mayidaili.com/free/location/墨西哥-2-3996063">墨西哥</a>
                            </td>
                            <td>
									<a href="http://www.mayidaili.com/free/location/墨西哥,奇瓦瓦州-3-4014336">奇瓦瓦州</a>
									<a href="http://www.mayidaili.com/free/location/墨西哥,奇瓦瓦州,Ciudad Juárez-4-4013708">Ciudad Juárez</a>

							</td>
                            <td>
                                <span class="label label-warning">1250</span>
                                ms
							</td>
                            <td>
                                <time class="timeago">刚刚</time>
                            </td>
                        </tr>
                        <tr>
                            <td>183.131.135.69
							</td>
                            <td>
								<img width="80" height="20" class="js-proxy-img" data-uri="http://www.mayidaili.com/free/img/1/48786/0DMYK9wFFAymf55icCgB-A" />
							</td>
                            <td>
                                    <a href="http://www.mayidaili.com/free/anonymous/透明">透明</a>
                            </td>
                            <td>
                                <img width="16" height="11" src="http://static.mayidaili.com/img/flags/CN.png" class="mr5" />
                                    <a href="http://www.mayidaili.com/free/location/中国-2-1814991">中国</a>
                            </td>
                            <td>
									<a href="http://www.mayidaili.com/free/location/中国,浙江省-3-1784764">浙江省</a>
									<a href="http://www.mayidaili.com/free/location/中国,浙江省,舟山市-4-1784107">舟山市</a>

							</td>
                            <td>
                                <span class="label label-success">71</span>
                                ms
							</td>
                            <td>
                                <time class="timeago">刚刚</time>
                            </td>
                        </tr>
                        <tr>
                            <td>203.172.209.246
							</td>
                            <td>
								<img width="80" height="20" class="js-proxy-img" data-uri="http://www.mayidaili.com/free/img/1/31222/fUr3IY1Xz58gh1_M_NRMyg" />
							</td>
                            <td>
                                    <a href="http://www.mayidaili.com/free/anonymous/普匿">普匿</a>
                            </td>
                            <td>
                                <img width="16" height="11" src="http://static.mayidaili.com/img/flags/TH.png" class="mr5" />
                                    <a href="http://www.mayidaili.com/free/location/泰国-2-1605651">泰国</a>
                            </td>
                            <td>



							</td>
                            <td>
                                <span class="label label-success">702</span>
                                ms
							</td>
                            <td>
                                <time class="timeago">刚刚</time>
                            </td>
                        </tr>
                        <tr>
                            <td>219.127.253.43
							</td>
                            <td>
								<img width="80" height="20" class="js-proxy-img" data-uri="http://www.mayidaili.com/free/img/1/25657/4pRKryPBn0OdU9hhP4mAuw" />
							</td>
                            <td>
                                    <a href="http://www.mayidaili.com/free/anonymous/高匿">高匿</a>
                            </td>
                            <td>
                                <img width="16" height="11" src="http://static.mayidaili.com/img/flags/JP.png" class="mr5" />
                                    <a href="http://www.mayidaili.com/free/location/日本-2-1861060">日本</a>
                            </td>
                            <td>



							</td>
                            <td>
                                <span class="label label-danger">2221</span>
                                ms
							</td>
                            <td>
                                <time class="timeago">刚刚</time>
                            </td>
                        </tr>
                        <tr>
                            <td>220.249.101.159
							</td>
                            <td>
								<img width="80" height="20" class="js-proxy-img" data-uri="http://www.mayidaili.com/free/img/1/18928/F50hS0P0MsdRVXgPcgGndA" />
							</td>
                            <td>
                                    <a href="http://www.mayidaili.com/free/anonymous/高匿">高匿</a>
                            </td>
                            <td>
                                <img width="16" height="11" src="http://static.mayidaili.com/img/flags/CN.png" class="mr5" />
                                    <a href="http://www.mayidaili.com/free/location/中国-2-1814991">中国</a>
                            </td>
                            <td>
									<a href="http://www.mayidaili.com/free/location/中国,湖北省-3-1806949">湖北省</a>
									<a href="http://www.mayidaili.com/free/location/中国,湖北省,武汉市-4-1791243">武汉市</a>
									<a href="http://www.mayidaili.com/free/location/中国,湖北省,武汉市,江夏区-5-6642320">江夏区</a>
									湖北经济学院
							</td>
                            <td>
                                <span class="label label-danger">1700</span>
                                ms
							</td>
                            <td>
                                <time class="timeago">刚刚</time>
                            </td>
                        </tr>
                    </tbody>
                </table>
				<div class="text-right">


<nav>
    <ul class="pagination">

<li class="active">
        <a href="http://www.mayidaili.com/free/1">1</a>
</li>
<li >
        <a href="http://www.mayidaili.com/free/2">2</a>
</li>


<li >
        <a href="http://www.mayidaili.com/free/3">3</a>
</li>
<li >
        <a href="http://www.mayidaili.com/free/4">4</a>
</li>
<li >
        <a href="http://www.mayidaili.com/free/5">5</a>
</li>
<li >
        <a href="http://www.mayidaili.com/free/6">6</a>
</li>
<li >
        <a href="http://www.mayidaili.com/free/7">7</a>
</li>
        <li class="dotitem">
            <a href="javascript:void(0)">...</a>
        </li>

    <li >
            <a href="http://www.mayidaili.com/free/3222">3222</a>
    </li>
    <li >
            <a href="http://www.mayidaili.com/free/3223">3223</a>
    </li>

        <li>
            <a href="http://www.mayidaili.com/free/2">»</a>
        </li>
</ul>
</nav>
				</div>
                </div>
            </div>
            <!-- end row -->
        </div>
        <div class="footer">
    	<div class="container">
    			<p>友情链接: <a href="http://www.ip181.com/" target="_blank">代理IP检测平台</a></p>
            	<p>警告：禁止利用本站资源从事任何违反本国（地区）法律法规的活动</p>
            	<p>©2015 蚂蚁代理 | 京ICP备13036930号-2</p>
        </div>
        <script src="http://static.mayidaili.com/js/jquery.min.js"></script>
        <script src="http://static.mayidaili.com/js/bootstrap.min.js"></script>
        <script src="http://static.mayidaili.com/js/selectize.min.js"></script>
        <script src="http://static.mayidaili.com/js/jquery.sticky.js"></script>
        <script src="http://static.mayidaili.com/js/highlight.pack.js"></script>
        <script src="http://www.mayidaili.com/js/main.js?v=1.0.5"></script>
        <script>var basePath="http://www.mayidaili.com";var staticPath="http://static.mayidaili.com";</script>
        <script>
var _hmt = _hmt || [];
(function() {
  var hm = document.createElement("script");
  hm.src = "//hm.baidu.com/hm.js?dad083bfc015b67e98395a37701615ca";
  var s = document.getElementsByTagName("script")[0];
  s.parentNode.insertBefore(hm, s);
})();
</script>
</div>
		<script language="javascript">
		$(function(){
			document.cookie="proxy_token=xpMPHFxm;path=/";
			$("img.js-proxy-img").each(function(index,item){
				$(this).attr("src",$(this).attr("data-uri")).removeAttr("data-uri");;
			});
		});
		</script>
    </body>
</html>
"""


def test(page):
    # ips = getIPfromPage(page, portrule=r"""%s</td>\n<td style="WIDTH:40PX">(\d+)""")
    # print ips
    # print len(ips)
    # rule=r"""%s\s?\t+</td>\s?    *<td>\s?\t+<img width="80" height="20" class="js-proxy-img" data-uri="(.*)" />""" % ('219.127.253.43')
    rule="""document.cookie="(.*);path"""

    template=re.compile(rule)
    port =template.findall(page)


    # port = re.search(rule,page).groups()
    print 'port is',port,':',len(port)

# test(texto)
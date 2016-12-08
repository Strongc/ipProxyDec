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

def getIPfromPage(page,rules=None):
    # import copy
    # htmlcode= copy.deepcopy(page)
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

            print prule
            print page



            port=re.search(prule, page).groups()[0]
            # report= re.compile(prule)
            # print prule
            # print report
            # print page
            #
            # port=report.findall(page)[0]
            if porttype == '1':
                picurl=port
                print port

                port_picrule=rules[7]
                if port_picrule!='':
                    pass

        print ip,port
        iplist.add((ip,port))


    return iplist

def getStaticHtml(path):
    conpool=connectpool.getObject()
    print path
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
                <p>实时扫描免费代理数量：<strong class="fz20">48761</strong></p>
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
	                    	<a class="free-tags" href="http://www.mayidaili.com/free/port/8099">8099</a>
	                    	<a class="free-tags" href="http://www.mayidaili.com/free/port/9100">9100</a>
	                    	<a class="free-tags" href="http://www.mayidaili.com/free/port/23">23</a>
	                    	<a class="free-tags" href="http://www.mayidaili.com/free/port/1453">1453</a>
	                    	<a class="free-tags" href="http://www.mayidaili.com/free/port/1518">1518</a>
	                    	<a class="free-tags" href="http://www.mayidaili.com/free/port/3127">3127</a>
	                    	<a class="free-tags" href="http://www.mayidaili.com/free/port/8008">8008</a>
	                    	<a class="free-tags" href="http://www.mayidaili.com/free/port/8085">8085</a>
	                    	<a class="free-tags" href="http://www.mayidaili.com/free/port/8808">8808</a>
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
                            <td>122.72.32.82
							</td>
                            <td>
								<img width="80" height="20" class="js-proxy-img" data-uri="http://www.mayidaili.com/free/img/1/49284/wsREIP3Xx0-c5J7Qx6egJA" />
							</td>
                            <td>
                                    <a href="http://www.mayidaili.com/free/anonymous/透明">透明</a>
                            </td>
                            <td>
                                <img width="16" height="11" src="http://static.mayidaili.com/img/flags/CN.png" class="mr5" />
                                    <a href="http://www.mayidaili.com/free/location/中国-2-1814991">中国</a>
                            </td>
                            <td>
									<a href="http://www.mayidaili.com/free/location/中国,重庆市-3-1814905">重庆市</a>


							</td>
                            <td>
                                <span class="label label-success">131</span>
                                ms
							</td>
                            <td>
                                <time class="timeago">刚刚</time>
                            </td>
                        </tr>
                        <tr>
                            <td>222.187.32.174
							</td>
                            <td>
								<img width="80" height="20" class="js-proxy-img" data-uri="http://www.mayidaili.com/free/img/1/21979/L9zUyjxPvfThHLWA5L_ULQ" />
							</td>
                            <td>
                                    <a href="http://www.mayidaili.com/free/anonymous/普匿">普匿</a>
                            </td>
                            <td>
                                <img width="16" height="11" src="http://static.mayidaili.com/img/flags/CN.png" class="mr5" />
                                    <a href="http://www.mayidaili.com/free/location/中国-2-1814991">中国</a>
                            </td>
                            <td>
									<a href="http://www.mayidaili.com/free/location/中国,江苏省-3-1806260">江苏省</a>
									<a href="http://www.mayidaili.com/free/location/中国,江苏省,徐州市-4-1787823">徐州市</a>

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
                            <td>61.157.126.45
							</td>
                            <td>
								<img width="80" height="20" class="js-proxy-img" data-uri="http://www.mayidaili.com/free/img/1/61664/AyLxLclBXtxgUTQ9jK-3-Q" />
							</td>
                            <td>
                                    <a href="http://www.mayidaili.com/free/anonymous/透明">透明</a>
                            </td>
                            <td>
                                <img width="16" height="11" src="http://static.mayidaili.com/img/flags/CN.png" class="mr5" />
                                    <a href="http://www.mayidaili.com/free/location/中国-2-1814991">中国</a>
                            </td>
                            <td>
									<a href="http://www.mayidaili.com/free/location/中国,四川省-3-1794299">四川省</a>
									<a href="http://www.mayidaili.com/free/location/中国,四川省,成都市-4-1815285">成都市</a>

							</td>
                            <td>
                                <span class="label label-success">114</span>
                                ms
							</td>
                            <td>
                                <time class="timeago">刚刚</time>
                            </td>
                        </tr>
                        <tr>
                            <td>121.201.31.9
							</td>
                            <td>
								<img width="80" height="20" class="js-proxy-img" data-uri="http://www.mayidaili.com/free/img/1/29858/FsoSw0CEFGbq6Tk9HfLF4g" />
							</td>
                            <td>
                                    <a href="http://www.mayidaili.com/free/anonymous/透明">透明</a>
                            </td>
                            <td>
                                <img width="16" height="11" src="http://static.mayidaili.com/img/flags/CN.png" class="mr5" />
                                    <a href="http://www.mayidaili.com/free/location/中国-2-1814991">中国</a>
                            </td>
                            <td>
									<a href="http://www.mayidaili.com/free/location/中国,广东省-3-1809935">广东省</a>
									<a href="http://www.mayidaili.com/free/location/中国,广东省,中山市-4-1784313">中山市</a>

							</td>
                            <td>
                                <span class="label label-success">91</span>
                                ms
							</td>
                            <td>
                                <time class="timeago">刚刚</time>
                            </td>
                        </tr>
                        <tr>
                            <td>112.25.33.26
							</td>
                            <td>
								<img width="80" height="20" class="js-proxy-img" data-uri="http://www.mayidaili.com/free/img/1/8113/SnOeWAtg45plImMrohAL7w" />
							</td>
                            <td>
                                    <a href="http://www.mayidaili.com/free/anonymous/透明">透明</a>
                            </td>
                            <td>
                                <img width="16" height="11" src="http://static.mayidaili.com/img/flags/CN.png" class="mr5" />
                                    <a href="http://www.mayidaili.com/free/location/中国-2-1814991">中国</a>
                            </td>
                            <td>
									<a href="http://www.mayidaili.com/free/location/中国,江苏省-3-1806260">江苏省</a>
									<a href="http://www.mayidaili.com/free/location/中国,江苏省,南京市-4-1799960">南京市</a>

							</td>
                            <td>
                                <span class="label label-success">62</span>
                                ms
							</td>
                            <td>
                                <time class="timeago">刚刚</time>
                            </td>
                        </tr>
                        <tr>
                            <td>36.80.34.225
							</td>
                            <td>
								<img width="80" height="20" class="js-proxy-img" data-uri="http://www.mayidaili.com/free/img/1/52901/in6kjNZBnyZFaLaLGqlmjQ" />
							</td>
                            <td>
                                    <a href="http://www.mayidaili.com/free/anonymous/透明">透明</a>
                            </td>
                            <td>
                                <img width="16" height="11" src="http://static.mayidaili.com/img/flags/ID.png" class="mr5" />
                                    <a href="http://www.mayidaili.com/free/location/印度尼西亚-2-1643084">印度尼西亚</a>
                            </td>
                            <td>



							</td>
                            <td>
                                <span class="label label-warning">1076</span>
                                ms
							</td>
                            <td>
                                <time class="timeago">刚刚</time>
                            </td>
                        </tr>
                        <tr>
                            <td>112.90.147.142
							</td>
                            <td>
								<img width="80" height="20" class="js-proxy-img" data-uri="http://www.mayidaili.com/free/img/1/56774/X4XQi_NSU-iPTeAClnHFvA" />
							</td>
                            <td>
                                    <a href="http://www.mayidaili.com/free/anonymous/透明">透明</a>
                            </td>
                            <td>
                                <img width="16" height="11" src="http://static.mayidaili.com/img/flags/CN.png" class="mr5" />
                                    <a href="http://www.mayidaili.com/free/location/中国-2-1814991">中国</a>
                            </td>
                            <td>
									<a href="http://www.mayidaili.com/free/location/中国,广东省-3-1809935">广东省</a>
									<a href="http://www.mayidaili.com/free/location/中国,广东省,珠海市-4-1783950">珠海市</a>

							</td>
                            <td>
                                <span class="label label-success">83</span>
                                ms
							</td>
                            <td>
                                <time class="timeago">刚刚</time>
                            </td>
                        </tr>
                        <tr>
                            <td>202.59.163.129
							</td>
                            <td>
								<img width="80" height="20" class="js-proxy-img" data-uri="http://www.mayidaili.com/free/img/1/6052/I__6hMTxSdTcfSWr9qtSeg" />
							</td>
                            <td>
                                    <a href="http://www.mayidaili.com/free/anonymous/透明">透明</a>
                            </td>
                            <td>
                                <img width="16" height="11" src="http://static.mayidaili.com/img/flags/ID.png" class="mr5" />
                                    <a href="http://www.mayidaili.com/free/location/印度尼西亚-2-1643084">印度尼西亚</a>
                            </td>
                            <td>
									<a href="http://www.mayidaili.com/free/location/印度尼西亚,万丹省-3-1923045">万丹省</a>
									<a href="http://www.mayidaili.com/free/location/印度尼西亚,万丹省,Nusa-4-1960732">Nusa</a>

							</td>
                            <td>
                                <span class="label label-danger">1826</span>
                                ms
							</td>
                            <td>
                                <time class="timeago">刚刚</time>
                            </td>
                        </tr>
                        <tr>
                            <td>14.207.12.132
							</td>
                            <td>
								<img width="80" height="20" class="js-proxy-img" data-uri="http://www.mayidaili.com/free/img/1/53016/avZCahquSV4d2G12hfiJ1A" />
							</td>
                            <td>
                                    <a href="http://www.mayidaili.com/free/anonymous/普匿">普匿</a>
                            </td>
                            <td>
                                <img width="16" height="11" src="http://static.mayidaili.com/img/flags/TH.png" class="mr5" />
                                    <a href="http://www.mayidaili.com/free/location/泰国-2-1605651">泰国</a>
                            </td>
                            <td>
									<a href="http://www.mayidaili.com/free/location/泰国,Bangkok-3-1609348">Bangkok</a>
									<a href="http://www.mayidaili.com/free/location/泰国,Bangkok,曼谷-4-1609350">曼谷</a>

							</td>
                            <td>
                                <span class="label label-danger">3518</span>
                                ms
							</td>
                            <td>
                                <time class="timeago">刚刚</time>
                            </td>
                        </tr>
                        <tr>
                            <td>113.18.193.19
							</td>
                            <td>
								<img width="80" height="20" class="js-proxy-img" data-uri="http://www.mayidaili.com/free/img/1/16592/g9Hj-Adz5EXnFJfcnRfk0A" />
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
                                <span class="label label-success">95</span>
                                ms
							</td>
                            <td>
                                <time class="timeago">刚刚</time>
                            </td>
                        </tr>
                        <tr>
                            <td>221.228.64.56
							</td>
                            <td>
								<img width="80" height="20" class="js-proxy-img" data-uri="http://www.mayidaili.com/free/img/1/51177/Ntdamh6csdryFUFM6kdqlw" />
							</td>
                            <td>
                                    <a href="http://www.mayidaili.com/free/anonymous/透明">透明</a>
                            </td>
                            <td>
                                <img width="16" height="11" src="http://static.mayidaili.com/img/flags/CN.png" class="mr5" />
                                    <a href="http://www.mayidaili.com/free/location/中国-2-1814991">中国</a>
                            </td>
                            <td>
									<a href="http://www.mayidaili.com/free/location/中国,江苏省-3-1806260">江苏省</a>
									<a href="http://www.mayidaili.com/free/location/中国,江苏省,无锡市-4-1790902">无锡市</a>

							</td>
                            <td>
                                <span class="label label-success">66</span>
                                ms
							</td>
                            <td>
                                <time class="timeago">刚刚</time>
                            </td>
                        </tr>
                        <tr>
                            <td>60.195.204.249
							</td>
                            <td>
								<img width="80" height="20" class="js-proxy-img" data-uri="http://www.mayidaili.com/free/img/1/58589/9Bav3RNkkORjOnWKL6pspA" />
							</td>
                            <td>
                                    <a href="http://www.mayidaili.com/free/anonymous/透明">透明</a>
                            </td>
                            <td>
                                <img width="16" height="11" src="http://static.mayidaili.com/img/flags/CN.png" class="mr5" />
                                    <a href="http://www.mayidaili.com/free/location/中国-2-1814991">中国</a>
                            </td>
                            <td>
									<a href="http://www.mayidaili.com/free/location/中国,北京市-3-2038349">北京市</a>


							</td>
                            <td>
                                <span class="label label-danger">2355</span>
                                ms
							</td>
                            <td>
                                <time class="timeago">刚刚</time>
                            </td>
                        </tr>
                        <tr>
                            <td>189.50.14.169
							</td>
                            <td>
								<img width="80" height="20" class="js-proxy-img" data-uri="http://www.mayidaili.com/free/img/1/30201/pPJlWsWgcp4Zk1yQRJ2u_w" />
							</td>
                            <td>
                                    <a href="http://www.mayidaili.com/free/anonymous/透明">透明</a>
                            </td>
                            <td>
                                <img width="16" height="11" src="http://static.mayidaili.com/img/flags/BR.png" class="mr5" />
                                    <a href="http://www.mayidaili.com/free/location/巴西-2-3469034">巴西</a>
                            </td>
                            <td>



							</td>
                            <td>
                                <span class="label label-success">715</span>
                                ms
							</td>
                            <td>
                                <time class="timeago">刚刚</time>
                            </td>
                        </tr>
                        <tr>
                            <td>60.195.117.245
							</td>
                            <td>
								<img width="80" height="20" class="js-proxy-img" data-uri="http://www.mayidaili.com/free/img/1/34331/R7fXSoUzUJ-3OVGAMM4tSw" />
							</td>
                            <td>
                                    <a href="http://www.mayidaili.com/free/anonymous/透明">透明</a>
                            </td>
                            <td>
                                <img width="16" height="11" src="http://static.mayidaili.com/img/flags/CN.png" class="mr5" />
                                    <a href="http://www.mayidaili.com/free/location/中国-2-1814991">中国</a>
                            </td>
                            <td>
									<a href="http://www.mayidaili.com/free/location/中国,北京市-3-2038349">北京市</a>

									<a href="http://www.mayidaili.com/free/location/中国,北京市,,海淀区-5-1809103">海淀区</a>
							</td>
                            <td>
                                <span class="label label-danger">2013</span>
                                ms
							</td>
                            <td>
                                <time class="timeago">刚刚</time>
                            </td>
                        </tr>
                        <tr>
                            <td>111.1.61.54
							</td>
                            <td>
								<img width="80" height="20" class="js-proxy-img" data-uri="http://www.mayidaili.com/free/img/1/8218/AbtUCh3HB1w8ViuHWfVQAw" />
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
									<a href="http://www.mayidaili.com/free/location/中国,浙江省,杭州市-4-1808925">杭州市</a>

							</td>
                            <td>
                                <span class="label label-success">67</span>
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
            <a href="http://www.mayidaili.com/free/3217">3217</a>
    </li>
    <li >
            <a href="http://www.mayidaili.com/free/3218">3218</a>
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
			document.cookie="proxy_token=FVoLBwIF;path=/";
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
    # rule=r"""%s</td>\n<td><img width="80" height="20" class="js-proxy-img" data-uri="(.*)" />""" % ('203.192.12.146')
    # rule=r"""%s\n(.)""" % ('122.72.32.82')
    rule="""222.187.32.174</td>\n<td>\n<img width="80" height="20" class="js-proxy-img" data-uri="http://www.mayidaili.com/free/img/1/21979/L9zUyjxPvfThHLWA5L_ULQ" /></td>"""

    port = re.search(rule,page).groups()
    print 'port is',port,':',len(port)

test(texto)
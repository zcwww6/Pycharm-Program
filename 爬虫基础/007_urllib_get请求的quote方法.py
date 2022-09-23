# _*_ coding : utf-8_*_
# @Time : 2022/9/17 10:44 
# @Author : Chengwei
# @File : 007_urllib_get请求的quote方法
# @Project : program


#需求：获取网页源码

import urllib.request
import urllib.parse
url = 'https://www.baidu.com/s?wd='

#模拟浏览器向服务器发送请求
header = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36 QIHU 360SE'}

#将’周杰伦‘三个字变成unicode编码的格式
name = urllib.parse.quote('周杰伦')
url = url +name

#
request = urllib.request.Request(url=url,headers=header)
response = urllib.request.urlopen(request)
#获取响应内容
content = response.read().decode('utf-8')
print(content)

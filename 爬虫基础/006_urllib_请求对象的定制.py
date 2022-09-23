# _*_ coding : utf-8_*_
# @Time : 2022/9/17 10:24 
# @Author : Chengwei
# @File : 006_urllib_请求对象的定制
# @Project : program


import urllib.request

url = 'https://www.baidu.com'

#url的组成
#http/https
#协议        主机       端口号    路径     参数       锚点
#http  80
#https   443
#mysql    3306
#oracle   1521
#redis

#user-agent 反爬机制
# response = urllib.request.urlopen(url)
# content = response.read().decode('utf-8')
# print(content)

#请求对象的定制，urlopen 方法中不能存储字典
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36 QIHU 360SE'}
request = urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
print(content)
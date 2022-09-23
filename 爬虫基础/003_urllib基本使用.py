# _*_ coding : utf-8_*_
# @Time : 2022/9/17 9:33 
# @Author : Chengwei
# @File : 003_urllib基本使用
# @Project : program

#使用urllib获取百度首页源码
import urllib.request
#定义一个url
url = 'http://www.baidu.com'

#模拟浏览器向服务器发送请求
reponse = urllib.request.urlopen(url)

#获取响应中的页面的源码  read()方法返回的是字节形式的二进制数据

#将二进制的数据转换为字符串  （解码）
content = reponse.read().decode('utf-8')

#打印数据
print(content)

# _*_ coding : utf-8_*_
# @Time : 2022/9/17 9:46 
# @Author : Chengwei
# @File : 004_urllib1个类型和6个方法
# @Project : program

import urllib.request

url = 'http://www.baidu.com'

#模拟浏览器向服务器发送请求
response = urllib.request.urlopen(url)

#一个类型和六个方法
#HTTPResponse 类型
print(type(response))

#按照字节的方式去读
# content = response.read()
# print(content)

#数字表示返回多少个字节
# content = response.read(5)
# print(content)

#读取一行
# content = response.readline()
# print(content)

#按行读取全部
# content = response.readlines()
# print(content)

#返回状态码
# print(response.getcode())

#返回状态码
print(response.geturl())

#返回状态信息
response.getheaders()


# _*_ coding : utf-8_*_
# @Time : 2022/9/17 11:06 
# @Author : Chengwei
# @File : 008_urllib_get请求的urlencode方法
# @Project : program

import urllib.parse
import urllib.request

#urlencode 应用于多个参数的转换




#获取网页源码
base_url = 'https://www.baidu.com/s?'
data = {
    'wd':'周杰伦',
    'sex':'男'
}
url = base_url + urllib.parse.urlencode(data)
headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0'}
request = urllib.request.Request(url=url,headers = headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
print(content)
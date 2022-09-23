# _*_ coding : utf-8_*_
# @Time : 2022/9/17 11:22 
# @Author : Chengwei
# @File : 009_urllib_post请求百度翻译
# @Project : program

import urllib.request
import urllib.parse
import json
url = 'https://fanyi.baidu.com/sug'

headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0'}

#请求对象定制的参数
data = {
    'kw':'spider'
}
#post 的请求必须进行编码
#post 请求的参数必须进行编码
data = urllib.parse.urlencode(data)
data = data.encode('utf-8')

request = urllib.request.Request(url=url,data=data,headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
#字符串转化json对象
obj = json.loads(content)
print(obj)
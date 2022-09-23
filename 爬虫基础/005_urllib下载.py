# _*_ coding : utf-8_*_
# @Time : 2022/9/17 9:54 
# @Author : Chengwei
# @File : 005_urllib下载
# @Project : program

import urllib.request

#下载网页
# url_page = 'http://www.baidu.com'

# urllib.request.urlretrieve(url_page,'baidu.html')
#下载图片
# url_picture = 'https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fwx2.sinaimg.cn%2Fmw690%2F005zcuwJly1h62uwk65oaj31e0230qv5.jpg&refer=http%3A%2F%2Fwx2.sinaimg.cn&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1665971983&t=c19195c9ddade2ceb48fcdadc20f1189'
# urllib.request.urlretrieve(url_picture,filename='lisa.jpg')
#下载视频
url_video = 'https://live-s3m.mediav.com/nativevideo/5bda5c6ab6e416abffe0da669d5632a7-bit_cloud1024.mp4'
urllib.request.urlretrieve(url_video,'video.mp4')
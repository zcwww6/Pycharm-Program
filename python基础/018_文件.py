# _*_ coding : utf-8_*_
# @Time : 2022/9/17 8:39 
# @Author : Chengwei
# @File : 018_文件
# @Project : program
'''
1.文件的打开/创建/关闭
    f = open('text.txt','w')
    f.write()  写入文件
    f。close()  关闭文件

2.文件的读写
    f.write()  写数据
        ’a‘  追加操作
    f.read()  读数据  默认情况下按字节来读
        f.readline()  按行读，但是只能读取一行
        f.readlines()  读取多行，返回列表

3. 文件的序列化和反序列化
    JSON 模块，本质是字符串
    import json
    json.dumps(name)  把对象转换成字符串，它本身不具备将数据写入到文件的功能
    json.dump(name，f)  转换并且写入

    反序列化：
        json.loads(content)  将json 对象转换为 python 对象
        json.load(f)  读取并且转化
'''
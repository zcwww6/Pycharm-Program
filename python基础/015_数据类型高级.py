# _*_ coding : utf-8_*_
# @Time : 2022/9/16 21:53 
# @Author : Chengwei
# @File : 015_数据类型高级
# @Project : program

'''
1.字符串高级
    获取长度：len
    查找内容：find ,找到事返回第一次出现位置的索引，找不到则返回-1
    判断开头结尾： startswith   endswith
    计算出现次数： count 返回str 在start 和 end 之间 在mystr 里面出现的次数
    替换内容 : replace 替换字符中指定的内容，如果指定次数count,则不会超过count 次
    切割字符串： split 通过参数的内容切割字符串
    修改大小写： upper  lower  将字符串的大小写转换
    空格处理  ： strip 去空格
    字符串拼接： join (没空一个加一个字符）
2.列表高级
    添加元素： append 在末尾添加元素
             insert在指定位置插入元素
             extend 合并两个列表
    修改元素： list[i] = x;  用x替换i 位置的元素
    查找元素： in
             not
    删除元素 ：
            del 根据下标进行删除
            pop 删除最后一个元素
            remove 根据元素的值进行删除

3.元组高级
    元组的元素不不能修改
    访问元组：  tuple[i]
    修改元祖： ！不支持！！！！
    定义只有一个元素的元组时需要在一个元素后面加逗号，当元组中只有一个元素的时候，它是整型数据

4.切片  是指对对象截取其中一部分的操作  支持字符串、列表、元组
        语法：[起始：结束：步长](不包括结束该索引)

5.字典高级
        查看元素： info['key']
                 info.get('key']
        修改元素：
                info['id'] = 12 如果该数据不存在那就是添加元素
        删除元素：
                del info['name']  删除Key为name 的值
                del info  删除整个字典
                clear 清空字典，但是保留字典对象
        遍历：
                for key in person.keys() :   遍历所有的key
                for value in person.values() :   遍历所有的value
                for key,value in person.items() :  遍历所有key 和 value
                for item in person.items():  遍历所有的项





'''
s = 'hello world'
print(s[:4])
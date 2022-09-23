# _*_ coding : utf-8_*_
# @Time : 2022/9/16 21:22 
# @Author : Chengwei
# @File : 012_逻辑运算符性能提升
# @Project : program

'''

'''
#当 and 前面的结果是false 的话后面的代码不再执行

a = 36
a > 10 and print('hello world')
a < 10 and print('wrong')

#前面为真时不执行后面的语句，前面为假执行后面的语句

a = 38
a > 37 or print("hello world")
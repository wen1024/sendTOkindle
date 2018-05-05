#!/usr/local/python3/bin/python3.6
#-*- coding:utf-8 _*-  
# #  FileName    : register
# #  Author      : XiaoHua Wen <wenhua.maker@gmail.com>
# #  Created     : 2018/1/26
# #  Copyright   : 2018-2020
# #  Description : 

import pymysql
import sys
def search_data(user_name):
    # 打开数据库连接
    db = pymysql.connect("localhost", "wenhua", "wenhua", "wechat", charset='utf8')
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # SQL 插入语句
    sql = "SELECT email FROM users WHERE user_name =%s"
    data = user_name
    cursor.execute(sql, data)
    results = cursor.fetchall()
    try:
        info = results[0][0]
        print(info)
    except IndexError:
        db.close()
        return u'尚未注册，请先使用注册功能'
    return info

def up_data(user_name, email):
    # 打开数据库连接
    db = pymysql.connect("localhost", "wenhua", "wenhua", "wechat", charset='utf8')
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # SQL 插入语句
    sql = "UPDATE users SET email=%s where user_name=%s"
    data = email,user_name
    try:
        # 执行sql语句
        print(sql,data)
        cursor.execute(sql,data)
        # 提交到数据库执行
        db.commit()
        return True
    except:
        print("不可处理异常:", sys.exc_info())
        # 如果发生错误则回滚
        db.rollback()
        return False
    # 关闭数据库连接
    db.close()

def save_data(user_name, email):
    # 打开数据库连接
    db = pymysql.connect("localhost", "wenhua", "wenhua", "wechat", charset='utf8')
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # SQL 插入语句
    sql = "REPLACE INTO users(user_name,email) VALUES (%s,%s)"
    data = user_name, email
    try:
        # 执行sql语句
        cursor.execute(sql,data)
        # 提交到数据库执行
        db.commit()
        return '注册成功'
    except:
        print("不可处理异常:", sys.exc_info())
        # 如果发生错误则回滚
        db.rollback()
        return sys.exc_info()[0]
    # 关闭数据库连接
    db.close()

def user_register(msg):
    user_name = msg['FromUserName']
    try:
        email = msg['Content'].split('#')[2]
    except IndexError:
        return '请输入正确的代码格式'

    if email.endswith(('kindle.com','kindle.cn','live.com')):
        return save_data(user_name, email)
    else:
        return '请使用正确的邮箱地址,如：kindle.cn,kindle.com'

def user_updata(msg):
    user_name = msg['FromUserName']
    try:
        email = msg['Content'].split('#')[2]
    except IndexError:
        return '请输入正确的代码格式'
    if up_data(user_name, email):
        return '更新成功'
    else:
        return '更新失败请联系管理员'
def user_info(msg):
    user_name = msg['FromUserName']
    return search_data(user_name)


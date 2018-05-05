#!#!/usr/local/python3/bin/python3.6
#-*- coding:utf-8 _*-  
# #  FileName    : wechat_robot
# #  Author      : XiaoHua Wen <wenhua.maker@gmail.com>
# #  Created     : 2018/1/26
# #  Copyright   : 2018-2020
# #  Description :

import register
import itchat, time
from itchat.content import *
from send_to_kindle import send_mail
import requests

loc = '河北保定'
userid = 184681
key ='be0f2c76d17c4b689b378210ab7776bb'
first_flag = 1

def get_info(info,userid = 184681,key ='be0f2c76d17c4b689b378210ab7776bb'):
    data = {
    "key": key,
    "info": info,
    "userid":userid
    }
    return data

@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def text_reply(msg):
    info = action(msg)
    msg.user.send(info)

@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def download_files(msg):
    path = "./file/"+msg.fileName
    result = msg.download(path)['BaseResponse']['RawMsg']
    if result == 'Successfully downloaded':
        msg.user.send('下载成功即将发送邮件')
        send_mail_result = send_mail(path,register.user_info(msg),msg.fileName)
    return send_mail_result

@itchat.msg_register(FRIENDS)
def add_friend(msg):
    msg.user.verify()
    msg.user.send('你好，新朋友')

@itchat.msg_register(TEXT, isGroupChat=True)
def text_reply(msg):
    if msg.isAt:
        msg['Content'] = '#'+'#'.join(msg.Text.split('#')[1:])
        print(msg)
        if msg['Content'].startswith('#注册'):
            info = register.user_register(msg)
            msg.user.send(info)
        elif msg['Content'].startswith('#更新'):
            info = register.user_updata(msg)
            msg.user.send(info)
        elif msg['Content'].startswith('#查询'):
            info = register.user_info(msg)
            msg.user.send(info)
        else:
            print(msg)
            info = get_info(info=msg.text)
            answer = requests.post('http://www.tuling123.com/openapi/api', data=info).json()
            msg.user.send(u'@%s\u2005 %s' % (msg.actualNickName, answer['text']))

def action(msg):
    if msg['Content'].startswith('#注册'):
        info = register.user_register(msg)
        return info
    elif msg['Content'].startswith('#更新'):
        info = register.user_updata(msg)
        return info
    elif msg['Content'].startswith('#查询'):
        info = register.user_info(msg)
        return info
    else:
        # if msg['Content'].startswith('#'):
        info = get_info(info=msg.text)
        answer = requests.post('http://www.tuling123.com/openapi/api', data=info).json()
        return answer['text']

itchat.auto_login(True)
itchat.run(True)


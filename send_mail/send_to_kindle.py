#!/usr/local/python3/bin/python3.6
#-*- coding:utf-8 _*-  
# #  FileName    : semo
# #  Author      : XiaoHua Wen <wenhua.maker@gmail.com>
# #  Created     : 2018/1/26
# #  Copyright   : 2018-2020
# #  Description : 

import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


def send_mail(path,recevice,file_name):
    username = 'send_to_kindle@hotmail.com'
    password = 'wh0205wh.'
    sender = username
    receivers = recevice

    # 如名字所示： Multipart就是多个部分
    msg = MIMEMultipart()
    msg['Subject'] = '推书'
    msg['From'] = sender
    msg['To'] = receivers

    # 下面是文字部分，也就是纯文本
    puretext = MIMEText('微信推书，如有问题联系微信：704505525')
    msg.attach(puretext)

    # 下面是附件部分 ，这里分为了好几个类型

    # 首先是xlsx类型的附件
    def attachment(path, filename):
        xlsxpart = MIMEApplication(open(path, 'rb').read())
        xlsxpart.add_header('Content-Disposition', 'attachment', filename=filename)
        msg.attach(xlsxpart)

    ##  下面开始真正的发送邮件了
    try:
        client = smtplib.SMTP()
        client.connect('smtp.live.com')
        client.starttls()
        client.login(username, password)
        attachment(path,file_name)
        client.sendmail(sender, receivers, msg.as_string())
        client.quit()
        return '邮件发送成功！(%s)'%recevice
    except smtplib.SMTPRecipientsRefused:
        return 'Recipient refused'
    except smtplib.SMTPAuthenticationError:
        return  'Auth error'
    except smtplib.SMTPSenderRefused:
        return 'Sender refused'
    except FileNotFoundError:
        return '文件不存在'
    except :
        return sys.exc_info()

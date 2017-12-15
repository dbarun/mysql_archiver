#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header

#邮件发送函数
def send_mail(message):
    # 第三方 SMTP 服务
    mail_host = "mail.xxx.com"  # 设置服务器
    mail_user = "xxx"  # 用户名
    mail_pass = "xxx"  # 口令

    sender = 'xxx@qq.com'
    receivers = ['xxx@qq.com']  # 接收邮件

    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print "邮件发送成功"
    except smtplib.SMTPException:
        print "Error: 无法发送邮件"

    return
# 简单邮件传输协议(SMTP)是一种协议，用于在邮件服务器之间发送电子邮件和路由电子邮件。
# Python提供smtplib模块，该模块定义了一个SMTP客户端会话对象，\
# 可用于使用SMTP或ESMTP侦听器守护程序向任何互联网机器发送邮件。

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL

from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class EmailUser():
    def __init__(self, sender_mail, pwd, host_server='smtp.qq.com'):
        try:
            self.sender_mail = sender_mail
            self.smtp = SMTP_SSL(host_server)
            self.smtp.ehlo(host_server)
            self.smtp.login(sender_mail, pwd)
        except Exception as e:
            raise e

    def sendHtmlEmail(self, receiver, mail_title, mail_content):
        # 发送html
        try:
            msg = MIMEText(mail_content, "html", 'utf-8')  # 发送的是html,不能带图片

            msg["Subject"] = Header(mail_title, 'utf-8')
            msg["From"] = self.sender_mail
            msg["To"] = receiver

            self.smtp.sendmail(self.sender_mail, receiver, msg.as_string())

        except Exception as e:
            raise e

    def sendAttachments(self, receiver, mail_title, mail_content, attpaths):
        # 发送带附件的邮件
        try:
            msg = MIMEMultipart()

            msg["Subject"] = Header(mail_title, 'utf-8')
            msg["From"] = self.sender_mail
            msg["To"] = receiver  ## 接收者的别名

            msg.attach(MIMEText(mail_content, 'html', 'utf-8'))

            for attpath in attpaths:
                filename = attpath.split('\\')[-1]
                att = MIMEText(open(attpath, 'rb').read(), 'base64', 'utf-8')
                att["Content-Type"] = 'application/octet-stream'
                # 这里的filename可以任意写，写什么名字，邮件中显示什么名字 为什么中文乱码........
                att["Content-Disposition"] = 'attachment; filename="%s"' % filename
                msg.attach(att)

            self.smtp.sendmail(self.sender_mail, receiver, msg.as_string())

        except Exception as e:
            raise e

    def sendHtmlAttPic(self, receiver, mail_title, mail_content, picnames):
        # 发送带图片的html邮件
        try:
            msg = MIMEMultipart('related')
            msg["Subject"] = Header(mail_title, 'utf-8')
            msg["From"] = self.sender_mail
            msg["To"] = receiver  ## 接收者的别名

            msgAlternative = MIMEMultipart('alternative')
            msg.attach(msgAlternative)
            msgText = (MIMEText(mail_content, 'html', 'utf-8'))
            msgAlternative.attach(msgText)

            for i in picnames:
                with open(i, 'rb') as fp:
                    msgImage = MIMEImage(fp.read())

                msgImage.add_header('Content-ID', '<%s>' % i.split('.')[0])
                msg.attach(msgImage)

            self.smtp.sendmail(self.sender_mail, receiver, msg.as_string())

        except Exception as e:
            raise e


if __name__ == '__main__':
    picnames = ['ceshi.png', 'ceshi2.png']
    picid = [item.split('.')[0] for item in picnames]

    mail_content = """
     <p>你好，Python 邮件发送测试...</p>
     <p>这是使用python登录邮箱发送HTML格式和图片的测试邮件：</p>
     <p><a href='http://www.百度.com'>百度</a></p>
     <p>图片演示：</p>
     <p><img src="cid:{0}"></p>
      <p><img src="cid:{1}"></p>
    """.format(*picid)

    emaluser = EmailUser(sender_mail='xxxxxxx@qq.com', pwd='**************', \
                         host_server='smtp.qq.com')

    emaluser.sendHtmlAttPic(receiver='yyyyyyy@aliyun.com', mail_title='(个_个)你好呀', \
                            mail_content=mail_content, picnames=picnames)

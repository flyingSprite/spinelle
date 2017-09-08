import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr

from conf.config import EMAIL_AUTHORIZATION_CODE, EMAIL_USERNAME, EMAIL_SMTP_SERVICE

"""
Order 23: Send Text Email by 126 mail
Refer to http://www.runoob.com/python/python-email.html
"""


class SendMail(object):

    def __init__(self):
        self.smtp_instance = smtplib.SMTP()
        self.smtp_instance.connect(host=EMAIL_SMTP_SERVICE)  # 25 为 SMTP 端口号
        self.smtp_instance.login(EMAIL_USERNAME, EMAIL_AUTHORIZATION_CODE)

    def send_text(self, to, subject, content):
        message = MIMEText(content, 'plain', 'utf-8')
        message['From'] = formataddr(["Runoob", EMAIL_USERNAME])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        message['To'] = formataddr(["FK", to])

        subject = subject
        message['Subject'] = Header(subject, 'utf-8')
        try:
            self.smtp_instance.sendmail(EMAIL_USERNAME, [to, ], message.as_string())
            print('Successful')
        except smtplib.SMTPException as e:
            raise e


sm = SendMail()
sm.send_text(
    'zrwuxian@126.com',
    '个人简介',
    '这个附件太大了，请修改一下'
)

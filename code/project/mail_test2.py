from smtplib import SMTP
from email.mime.text import MIMEText
from generateCaptcha import generate

from_addr = '10856033@ntub.edu.tw' # sender
to_addr = 'ntub112508@gmail.com' # recipient
# to_addr = ['10856014@ntub.edu.tw', '10856015@ntub.edu.tw', '10856033@ntub.edu.tw', '10856047@ntub.edu.tw'] # multiple recipient
content = '您的驗證碼為 "' + generate() + '"'
msg = MIMEText(content, 'html', 'utf-8')
msg['Subject'] = '您的信箱驗證碼'
msg['From'] = 'ezTrade <10856033@gmail.com>'
msg['To'] = 'ntub112508@gmail.com'


def sendMail(from_addr, to_addrs, msg):
    smtp = SMTP('smtp.gmail.com', 587)  # smtp server, port
    smtp.ehlo()
    smtp.starttls()  # use tls encryption
    smtp.login('10856033@ntub.edu.tw', 'gxyouohswmsmhwzk')  # smtp user authentication

    smtp.sendmail(from_addr, to_addrs, msg.as_string())  # send mail


sendMail(from_addr, to_addr, msg)

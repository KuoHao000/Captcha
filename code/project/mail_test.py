from smtplib import SMTP

from_addr = '10856033@ntub.edu.tw' # sender
to_addr = 'ntub112508@gmail.com' # recipient
# to_addr = ['10856014@ntub.edu.tw', '10856015@ntub.edu.tw', '10856033@ntub.edu.tw', '10856047@ntub.edu.tw'] # multiple recipient
msg = 'auto send mail test'


def sendMail(from_addr, to_addrs, msg):
    smtp = SMTP('smtp.gmail.com', 587) # smtp server, port
    smtp.ehlo()
    smtp.starttls() # use tls encryption
    smtp.login('10856033@ntub.edu.tw', 'gxyouohswmsmhwzk')  # user authentication

    smtp.sendmail(from_addr, to_addrs, msg) # send mail

sendMail(from_addr, to_addr, msg)
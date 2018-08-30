#python3
#
import requests #导入 requests
from bs4 import BeautifulSoup #导入BeautifulSoup

#---- 发邮件用的 先忽略
from email.mime.text import MIMEText
from email.header import Header
import smtplib
import socket

def sendEmail(title,content,receivers,sender='wevie_9@163.com',mail_host="smtp.163.com",mail_user="wevie_9@163.com",mail_pass="Aa123456"):

    msg = MIMEText(content, 'plain', 'utf-8')  # 内容, 格式, 编码
    msg['From'] = "{}".format(sender)
    msg['To'] = ",".join(receivers)
    msg['Subject'] = title  #邮件主题

    try:
        smtpObj = smtplib.SMTP_SSL(mail_host,465)  #启用SSL发信, 端口一般是465 qq邮件需要 ssl才能发出去
        #smtplib.SMTP(mail_host,22)
        smtpObj.login(mail_user, mail_pass)  # 登录验证
        smtpObj.sendmail(sender, receivers, msg.as_string())  #发送
        print("mail send success!.")
        #smtpObj.quit() 退出登录
    except smtplib.SMTPException as e: #这种错误类型比较常见
        print(e)
        print('邮件发送失败，请检查异常监控...')
#----

def get_detail(css,func=None,val=None): #获取内容
    for j in i.select(css):
        if func == 'get':
            var_name = j.get(val)
        else:
            var_name = j.text
        return var_name


#写入模式 打开文件（文件保存邮件正文） 填入一行内容，用于清除之前文件里的内容
with open('tmp.txt','w') as f:
    print('51 job 近期运维职位\n',file=f)

#page 1 51job 选定搜索条件后的网页 （无锡 4k-6k 运维）
url = 'https://search.51job.com/list/070400,000000,0000,00,9,99,%25E8%25BF%2590%25E7%25BB%25B4,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
#page 2
#url = 'https://search.51job.com/list/070400,000000,0000,00,9,99,%25E8%25BF%2590%25E7%25BB%25B4,2,2.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='

r = requests.get(url) #请求url
r.encoding = 'gbk' #以 gbk 编码（不然requests 默认unicode解码中文出现乱码）
html = r.text #响应内容读取到 html变量中

soup = BeautifulSoup(html,'lxml') #利用BeautifulSoup格式化

for i in soup.select('body .el'):
    if '江阴' in str(i.select('span.t3')): #如果工作地点在江阴则获取内容 否则丢弃

        detail_url = get_detail('p span a','get','href')
        job_name = get_detail('p span a','get','title')
        salary = get_detail('span.t4')
        date = get_detail('span.t5')
        work_space = get_detail('span.t3')
        company_name = get_detail('span.t2')

        #content = job_name + '\n',salary + '\n',date + '\n',work_space + '\n',company_name + '\n',detail_url + '\n'
        content = job_name, salary, date, work_space, company_name, detail_url , ''
        content = list(content)
        print(content)
        with open('tmp.txt','a') as f:
            for i in content:
                print(i,file=f)
with open('tmp.txt','r') as f:
    print(f.read())

#sendEmail

with open('tmp.txt','r') as f:
    content = f.read()
title = '51job Ops ...'
receivers=['wevie9@163.com']
sendEmail(title,content,receivers)


#sendEmail 注释

'''发送一封普通邮件,文本格式.

共有七个参数： 包括三个必填参数
title = 'mail title'        # 邮件标题  必填参数无默认值
content = 'mail content'    # 邮件内容  必填参数
receivers = ['Email addr']  # 收件人    必填     列表格式  可多个 列表内用逗号分开
sender = 'wevie_9@163.com'  # 发件人    最好写全 不然报错 (550, b'Invalid User', 'xiangyu.lin')
mail_host="smtp.163.com"    # 服务器    用163的
mail_user="wevie_9@163.com" # 用户名    默认用我的
mail_pass="Aa123456"        # 授权码    不是密码（网易邮箱可以登录邮箱开启授权码）
'''

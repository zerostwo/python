import requests
import re
from lxml import etree
import yagmail
import datetime as d

def log_scau(id, pwd):
    # 本代码共分为2部分
    session = requests.Session() # 创建会话连接，好处是会自动提交cookie，大大节省精力和代码量
    index = session.get('http://jiaowu.sicau.edu.cn/web/web/web/index.asp', timeout=2)
    # 第一部分，准备post提交的数据
    index.encoding = 'gb2312'
    seletor=etree.HTML(index.text)
    sign = seletor.xpath("//input[@name='sign']/@value")       # 利用xpath找到sign的值

    data = {                                          # 需要提交的数据
        'user': id,
        'pwd': pwd,
        'lb': 'S',
        'submit': '',
        'sign': sign
    }
    # 第二部分，尝试登陆
    try:
        post_url = 'http://jiaowu.sicau.edu.cn/jiaoshi/bangong/check.asp'  # 验证密码的网站
        session.post(post_url, data=data, timeout=2) # 先登陆验证密码网站
        data=session.get('http://jiaowu.sicau.edu.cn/xuesheng/bangong/main/index1.asp', timeout=2)  # 跳转到个人主页
        data.encoding = 'gb2312'
        notice = re.compile('<font color=#339999>(.*)</font></a>').findall(data.text)
        notice_url = re.compile('href="(.*)"><font color=#339999>').findall(data.text)
        new_date = re.compile('<td width="16%" align="left" valign="bottom" class="bluetext">(.*)<img height="11" src="../../../images/haitan/new.gif" width="28"></td>').findall(data.text)
        old_date = re.compile('<td width="16%" align="left" valign="bottom" class="bluetext">(.*)</td>').findall(data.text)
        date = new_date + old_date[len(new_date):]
        dic = {}
        contents = ['最新通知']
        f = open('/home/duansq/auto_notice.log', "a+")
        for i in range(0, len(notice)):
            dic[str(i)] = {}
            dic[str(i)][date[i]] = date[i] + "<a href = 'http://jiaowu.sicau.edu.cn/xuesheng/bangong/main/" + notice_url[i] + "'>" +notice[i] +"</a>"
        yag = yagmail.SMTP(user="zerostwo@126.com", password="981211Dd", host='smtp.126.com')
        now = d.datetime.now().strftime("(%m月%d日)")
        t = d.datetime.now().strftime("%Y-%m-%d %H:%M")
        for i in dic.keys():
            for j in dic[i].keys():
                if j == now:
                    contents.append(dic[i][j])
        if len(contents) == 1:
            print(t, "无最新通知", file=f)
            print(t, "无最新通知")
        else:
            yag.send('zzmath@126.com', subject='教务处动态', contents=contents)
            print(t, "发送成功", file=f)
            print(t, "发送成功")
    except:
        print(t, '出错', file=f)
        print(t, '出错')
    f.close()

id = '201702420'
pwd = '981211'
log_scau(id, pwd)


# 6133 201704811 qq123456 密码错误


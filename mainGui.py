# -*- coding:utf-8 -*-
__author__ = "cjluzzl"
__date__ = "2017/4/5 22:12 "

# -*- coding:utf-8 -*-
__author__ = "cjluzzl"
__date__ = "2017/4/5 10:16 "

from Tkinter import *
import tkMessageBox
import urllib2
import urllib
import re
import urlparse
import requests
import os


def download_image():
    url = "http://www.jiqie.com/a/re22.php"
    name = name_area.get().encode('utf8')
    if not name:
        tkMessageBox.showinfo('温馨提示', '请输入名字后再继续')
        return
    data = "id={0}&idi=jiqie&id1=30&id2=905&id3=%230000FF&id4=%230000DD&id5=%230000AA&id6=%23000077".format(name)
    header = {'HOST': 'www.jiqie.com',
              'Cookie':'__cfduid=db5909beddaf3db20c90e83d93cf9eccc1491320393; Hm_lvt_5fa01e7a9a7ea4ca19e7807aaa5a0def=1491320545,1491320571,1491363211,1491400691; Hm_lpvt_5fa01e7a9a7ea4ca19e7807aaa5a0def=1491402321',
              'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0'}

    req = urllib2.Request(url, headers=header, data=data)
    html = urllib2.urlopen(req).read()
    print html
    reg = r'<img src="..(.*?).gif'
    image_url = urlparse.urljoin(url, re.findall(reg, html)[0]+".gif")
    print image_url
    image_name = name.decode('utf8').encode('gbk')
    data = 'Cookie:__cfduid=db5909beddaf3db20c90e83d93cf9eccc1491320393; ' \
           'Hm_lvt_5fa01e7a9a7ea4ca19e7807aaa5a0def=1491320545,1491320571,1491363211,1491400691; ' \
           'Hm_lpvt_5fa01e7a9a7ea4ca19e7807aaa5a0def=1491402321'
    urllib.URLopener.version ='Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0'
    filename, headers = urllib.urlretrieve(image_url)
    print filename, '  ***  ', headers
    temp = open(filename,'rb').read()
    image = "%s.gif" % image_name
    with open(image, "wb") as fb:
        fb.write(temp)
        fb.close()

    #urllib.urlretrieve(image_url, filename="%s.gif" % image_name, data=data)

    print image_name.decode('gbk').encode('utf8')
    img = PhotoImage(file="{0}.gif".format(image_name.decode('gbk').encode('utf8')))
    photoLabel = Label(root, image=img)
    photoLabel.grid(row=3, column=1)
    root.update()
    root.mainloop()





#创建窗口 ，实例化窗口变量到root
root = Tk()
#修改窗口标题
root.title(u'计量赵子龙商务签名设计')


FONT_STYLE = ("微软雅黑",15)
#设置窗口大小 = 长 x 宽  加号连接的表示设置窗口在屏幕的位置
root.geometry('650x400+100+100')
# grid 和pack表示布局方式，一个项目中不能同时出现

name_label = Label(root, text=u"姓名：", font=FONT_STYLE, height='1')
name_label.grid(row=0, column=0)
#输入框、编辑框、文本框
name_area = Entry(root, font=FONT_STYLE)
#  entry单行输入框，text是多行文本框
name_area.grid(row=0, column=1)

button = Button(root, text=u" 一键设计", font=FONT_STYLE, width='15', height='1', command=download_image)
button.grid(row=2, column=1)
# img = PhotoImage(file="temp.gif")#(file="%s.gif" % "任志远".decode('gbk').encode('utf8'))
# photoLabel = Label(root, image=img)
# photoLabel.grid(row=3, column=1)
root.update_idletasks()
mainloop() #显示窗口

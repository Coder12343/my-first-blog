# -*- coding: utf-8 -*-
import urllib
import urllib2
import re
import cookielib
import sys,os
from datetime import datetime
import logging
import time

logger = logging.getLogger(__name__)

# 根据url获取网页
def get_page(url):
    req_header = {'User-Agent':'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E) ',
    'Accept':'text/html',
    # 'Accept-Charset':'utf-8',
    'Accept-Encoding':'utf-8',
    'Connection':'close',
    'Referer':None 
    }
    req_timeout = 5
    req = urllib2.Request(url,None,req_header)
    # print(url)
    resp = urllib2.urlopen(req,None,req_timeout)
    html = resp.read()
    return html

# 写入文件
def into_file(fileName,String):
    f = open(fileName,'w+')
    f.write(str(String))
    f.close()

# 写入二进制文件
def into_file2(fileName,String):
    f = open(fileName,'wb')
    f.write(str(String))
    f.close()

def download(url,pattern,path):
    html = get_page(url)
    into_file("C:\\Users\\huangtianqi\\Desktop\\catch.txt",html)

    urls = []
    # pattern = re.compile(r'\/bbc\/tae\/\d+\.html')
    urls = pattern.findall(html)
    count = 9
    print(urls)
    for u in urls[8:]:
        # time.sleep(1.5)
        nurl = "http://www.tingroom.com"+u
        html = get_page(nurl)
        into_file("C:\\Users\\huangtianqi\\Desktop\\test.txt",html)
        print(nurl)
        # time.sleep(1.5)

        # 获取‘下载听力’url
        # down_pattern = re.compile(r'/down.php\?id=\d*"')
        down_pattern = re.compile(r"/play\.php\?id=\d+")
        load_match = down_pattern.findall(html)
        load_url = load_match[0]
        print(load_url)
        html = get_page("http://www.tingroom.com"+load_url)
        into_file("C:\\Users\\huangtianqi\\Desktop\\test1.txt",html)
        # time.sleep(1.5)
        new_pattern = re.compile(r'http://\S*mp3')
        urls = new_pattern.findall(html)
        if len(urls) >= 1:
            html1 = urllib2.urlopen(urls[0]).read()
            
            into_file2(path+"\\"+str(count)+".mp3",html1)
            count = count + 1

# 'cyls','tae','re','qa_of_the_week','ask_about_britain','off_the_pitch','audio_programmes','on_the_town'
# strings = [ 'media_english','syw','intensive_listening','wnfs','ywzj','wdql','yyhlsg','xyw','together','ywgs','zgwd',
#             'xwch','zhdh','bbcyyjx','swyy']
# strings = ['together','ywgs','zgwd']
# for s in strings:
#     url = "http://www.tingroom.com/bbc/"+s+"/index.html"
#     pattern = re.compile(r"\/bbc\/"+s+"\/\d+\.html")
#     path = "C:\\Users\\huangtianqi\\Desktop\\tingroom\\"+s
#     os.system("mkdir "+ path)
#     download(url,pattern,path)

strings = ['yinyuekafeiting']
for s in strings:
    url = "http://www.tingroom.com/song/"+s
    pattern = re.compile(r"\/song\/"+s+"\/\d+\.html")
    path = "C:\\Users\\huangtianqi\\Desktop\\tingroom\\"+s
    os.system("mkdir "+ path)
    download(url,pattern,path)




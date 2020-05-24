# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import sys
import os
import requests_file
from requests_html import HTMLSession
from requests_file import FileAdapter
"""
convert pdf file into html file
"""

def crawler():
    session = HTMLSession( )

    # 如果是本地文件，需要以下代码
    # 挂载文件
    session.mount('file://', FileAdapter( ))
    # Windows系统路径目录分隔符为反斜杠，但get需要正斜杠所以先进行一下替换

    os.chdir("../data")
    file_path = os.getcwd( ).replace("\\", "/")
    print(file_path)
    url='word2vec.html'
    print('当前目录为：',os.getcwd())
    # 测试发现使用相对路径读不到文件，需要使用绝对路径
    r = session.get(f'file:///{file_path}/word2vec.html')
    soup=BeautifulSoup(r.text,'html.parser')
    soup_page_container = soup.find(id='page-container')
    #print('soup_page_container',soup_page_container.text)
    soup_pf1=soup.find(id='pf1')
    len_of_pages = 1
    text_len=len(soup_pf1.text)
    print('page',len_of_pages,'len',text_len,'conent:',soup_pf1.text)
    text =[]
    text.append(soup_pf1.text)

    next_ = soup_pf1.find_next_sibling()

    while next_:
        text_len = len(next_.text)
        text.append(next_.text)
        len_of_pages += 1
        print('page',len_of_pages,'len',text_len,'conent:',next_.text)
        next_ = next_.find_next_sibling( )

    with open(url + '.txt','w',encoding='utf-8') as f:
        for line in text:
            f.writelines(line+'\n')

# for next_line in soup_pf2.next_siblings:
    #     print (repr(next_line))

    # for next_ele in soup_pf2.next_elements:
    #     print (repr(next_ele))
    #os.chdir("..")
    #r = requests.get(url)
    #r = requests.get('http://'+url)
    #r = requests.get('file:///'+url)
    #r = requests.get(path+url)
    #print(r.status_code)
    #soup=BeautifulSoup(r)

if __name__ == "__main__":
    crawler()

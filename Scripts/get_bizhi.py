# -*- coding:utf-8 -*-

import os
import re
import urllib.request
from concurrent.futures import ThreadPoolExecutor

import requests
import tqdm as tqdm
from bs4 import BeautifulSoup

head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36"
}


def get_page(url):
    # 获取通过BeautifulSoup美化过的网页
    req = urllib.request.Request(url=url, headers=head)
    html = ''
    try:
        response = urllib.request.urlopen(req)
        html = response.read()
        page = BeautifulSoup(html, "html.parser")
    except Exception as result:
        print(result)
    return page


def get_file_type(name):
    # 获取图片的类型，即图片URL图片名的后缀.png .jpg等格式
    str1 = str(name).split('.', -1)
    str2 = str1[len(str1) - 1]
    return str2


def get_pic(url):
    pattern = r'<img alt="(.*?)" class="img-responsive big-thumb" height=".*?" loading="lazy" src="(.*?)" width=".*?"/>'
    # 在正则表达式匹配时里面各参数的顺序按照BeautifulSoup后的page来设置，在原始html中，img 后面并不是alt而是 img class
    # (.*?)即表示要获取的段，.*?代表任意字符不做匹配
    img_page = re.compile(pattern, re.S)
    page = get_page(url)
    pic_name = []
    # pic_name存储alt字段，对于一些图片的描述可做图片名，也直接用URL的图片名
    # 故pic_name可要可不要
    picurl = []
    for item in page.find_all('img'):
        # 遍历查找当前网页中所有的图片
        item = str(item)
        img_url = re.findall(img_page, item)
        if len(img_url) != 0:
            if img_url[0][0] != '':
                img_name = img_url[0][0] + '.' + get_file_type(img_url[0][1])
                pic_name.append(img_name)
                picurl.append((img_url[0][1]).replace('thumbbig-', ''))
                # 因为该主页中图片被压缩了，删除thumbbig-的URL才是图片原始地址
    return pic_name, picurl


def main(url):
    file_path = 'C:/Users/Public/Pictures/Capture/pi'
    # 给定文件存储路径
    # i = 0
    for item in (get_pic(url)[1]):
        req = urllib.request.Request(url=item, headers=head)
        data = urllib.request.urlopen(req).read()
        # 读取当前图片
        resp = requests.get(item, stream=True)
        file_size = int(resp.headers.get('content-length', 0))
        # 获取当前图片的总大小
        img_name = item.split('/')[-1]
        # 此处以URL中的后缀直接作为图片名（可能是毫无规律的数字，故有时中文网站alt中的中文描述更适合做名字）
        if not os.path.exists(file_path + img_name):
            pbar = tqdm.tqdm(total=int(file_size), unit='iB', unit_scale=True, desc=item.split('/')[-1])
            # 添加下载进度显示
            with open(file_path + img_name, 'wb') as file:
                for chunk in resp.iter_content(chunk_size=1024):
                    if chunk:
                        file.write(chunk)
                        pbar.update(1024)

        else:
            continue
        # i = i + 1


def run():
    print('开始下载...')
    input('''
    注意事项：
        所有壁纸都将要下载到 路径: C:/Users/Public/Pictures/Capture 请注意查收
    如果你已经看完了本事项，请按回车[Enter]
    ''')
    url1 = 'https://wall.alphacoders.com/search.php?search=landscape&quickload=300&page='
    for count in range(1, 3):
        url = url1 + str(count)
        # pool = ThreadPoolExecutor(max_workers=10)
        # pool.submit(main(url), count)
        main(url)
    exit(0)

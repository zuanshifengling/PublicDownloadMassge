# -*- coding:utf-8 -*-
# So good
# Yeah

__name__ = '__main__'

import time
import logging

# Logging日志设置
logging.basicConfig(level=logging.DEBUG, filename='./Logging/loger_main.log',format='%(asctime)s %(levelname)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

if __name__ == '__main__':

    logging.info('启动了程序')

    start_time = time.time()
    logging.info('开始时间 : ' + str(start_time))

    print('欢迎来到PDM下载器   Welcome to PDM Downloader')
    time.sleep(2)
    print('''
    /============================================================\\
    |                                                            |
    |============================================================|
    |                                                            |
    |   欢迎                                             Welcome  |
    |                                                            |
    |============================================================|
    |                                                            |
    |关于                   |concerning                           |
    |1.这只是一个实验项目     |1. This is just an experimental pro- |
    |                      |ct                                   |
    |2.有很多问题，欢迎反馈   |2. There are many questions, feedback|
    |                      |is welcome                           |
    |3.本程序可以当做下载器使 |3. This program can be used as a down|
    |用，可以下载小部分资源   |loader for , and a small part of res-|
    |                      |ources can be downloaded             |
    |4.可以下载壁纸啦-测试   |4. You can download wallpapers - test |
    |                                                            |
    |============================================================|
    |                                                            |
    |              by chunfeng.Andy                              |
    |              V 0.0.2                                       |
    |              S 0.0.2-Console-2022-12-27-Test               |
    |                                                            |
    |============================================================|
    |                                                            |
    \\============================================================/
    ''')
    time.sleep(5)
    # 读取支持文件
    logging.info('尝试读取文件')
    try:
        f = open('./lib/zc.txt', 'r', encoding='utf-8')
        text = f.read()
        f.close()
        logging.info('读取文件成功')
    except IOError as e:
        logging.debug('未找到文件')
        f = open('./lib/zc.txt', 'a', encoding='utf-8')
        f.close()
        f = open('./lib/zc.txt', 'r', encoding='utf-8')
        text = f.read()
        f.close()
    print('请选择下载模式')
    print(text)
    try:
        num = int(input('请输入模式 ( 输入数字 ) : '))
    except:
        logging.error('程序出错')
        print('程序出错!')
        time.sleep(4)
        end_time = time.time()
        run_time = end_time - start_time
        logging.info('本次运行时间 : ' + str(run_time))
        print('本次运行时间 : ' + str(run_time))
        exit(0)

    try:
        if num == 1:
            import Scripts.normal_link

            url = input(
                '请输入普通链接地址 , \n如 : https://issuecdn.baidupcs.com/issue/netdisk/yunguanjia/BaiduNetdisk_7.2.8.9.exe : ')
            name = input('请输入下载文件的名称 , \n如 : BaiduNetdisk_7.2.8.9.exe ( 记得加上.exe等后缀 ) : ')
            Scripts.normal_link.run(url=url, file_name=name)
            exit(0)
        elif num == 2:
            import Scripts.get_bizhi

            Scripts.get_bizhi.run()
            exit(0)

    except:
        logging.error('程序出错')
        print('程序出错!')
        time.sleep(4)
        end_time = time.time()
        run_time = end_time - start_time
        logging.info('本次运行时间 : ' + str(run_time))
        print('本次运行时间 : ' + str(run_time))
        exit(0)

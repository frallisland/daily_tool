# -*- coding:utf-8 -*-
'''
 @ author mengke
 @ email  lianchang16@qq.com
 @ create date 2023-02-13 22:18:43
 @ desc   query one's rank in leetcode contest when you konw her/his username
'''

import os
import requests
import random
from multiprocessing.pool import ThreadPool
from tqdm import tqdm


def check_page(num, url, username):
    header = {
        'origin': 'https://www.555yy1.com',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
    }

    proxies = ['HTTP://110.243.30.23:9999', 'HTTP://222.189.191.206:9999', 'HTTP://118.212.104.138:9999',
               'HTTP://182.149.83.97:9999', 'HTTP://106.42.163.100:9999', 'HTTP://120.83.107.69:9999',
               'HTTP://60.13.42.135:9999', 'HTTP://60.205.188.24:3128', 'HTTP://113.195.232.23:9999',
               'HTTP://59.62.36.74:9000', 'HTTP://218.2.226.42:80']
    proxy = {'HTTP': random.choice(proxies)}

    url = url+'/?pagination={:d}&&region=local'.format(num)

    r = requests.get(url, proxies=proxy, headers=header, timeout=5)

    rank = r.json()['total_rank']

    for _, obj in enumerate(rank):
        # print(obj['username'])
        if obj['username'] == username:
            return True
    return False


if __name__ == '__main__':
    contest_url = 'https://leetcode.cn/contest/api/ranking/weekly-contest-{:d}'.format(
        332)
    username = 'xxx'
    pages = 182

    ans = -1
    for page in tqdm(range(1, pages+1)):
        if check_page(page, contest_url, username):
            ans = page
            break
    print(ans)

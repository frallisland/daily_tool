# code ref to https://blog.csdn.net/qq_44700693/article/details/106189511

import os
import requests
import random
from multiprocessing.pool import ThreadPool
from tqdm import tqdm


def download(num, url, dir, flag=0):
    # url: this is a actual url--'https://****/20230108/17016_97bfaf0d/2000k/hls/6492ec773d2000001.ts',
    #     you just need to input 'https://****/20230108/17016_97bfaf0d/2000k/hls/6492ec773d200', the rest will be complete.
    # dir: video's name

    header = {
        'origin': 'https://www.555yy1.com',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
    }

    proxies = ['HTTP://110.243.30.23:9999', 'HTTP://222.189.191.206:9999', 'HTTP://118.212.104.138:9999',
               'HTTP://182.149.83.97:9999', 'HTTP://106.42.163.100:9999', 'HTTP://120.83.107.69:9999',
               'HTTP://60.13.42.135:9999', 'HTTP://60.205.188.24:3128', 'HTTP://113.195.232.23:9999',
               'HTTP://59.62.36.74:9000', 'HTTP://218.2.226.42:80']
    proxy = {'HTTP': random.choice(proxies)}

    url = url+'{:04d}'.format(num)+'.ts'
    dir = root_path+dir+'/'

    file_path = dir+str(url).split('/')[-1][-7:]

    with open(file_path, 'wb') as f:
        try:
            r = requests.get(url, proxies=proxy, headers=header, timeout=5)
            r.raise_for_status()
            r.encoding = 'utf-8'
            print('正在下载第 {} 个片段。'.format(num))
            f.write(r.content)
            if flag == 1:
                failure_list.remove(num)
        except:
            print('请求失败！')
            if num not in failure_list:
                failure_list.append(num)


def get_video(dir, mp4_file):
    dir = root_path+dir+'/'
    files = os.listdir(dir)
    mp4_file = root_path+mp4_file

    for file in tqdm(files, desc="正在转换视频格式："):
        if os.path.exists(dir + file):
            with open(dir + file, 'rb') as f1:
                with open(mp4_file, 'ab') as f2:
                    f2.write(f1.read())
        else:
            print("失败")


def check_ts():
    print("开始检查：")
    while failure_list:
        for num in failure_list:
            download(num, 1)
    print("ts 文件下载完成！")


if __name__ == '__main__':
    args = []
    root_path = './Spider/'
    failure_list = []  # 保存下载失败的片段

    dir = 'xxxx'  # change dirname
    mp4_file = 'yyyy.mp4'  # change target video name
    total = 9999  # change total segem

    if not os.path.exists(root_path+dir):
        os.makedirs(root_path+dir)

    # 开启线程池
    pool = ThreadPool(100)
    for i in range(1, total):
        args.append(
            (i, 'https://xxxx/20230108/6048_97bfaf0d/2000k/hls/f206c7edab100', dir))

    results = pool.starmap(download, args)
    pool.close()
    pool.join()

    check_ts()
    get_video(dir, mp4_file)

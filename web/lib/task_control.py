# coding=utf-8

import multiprocessing
from pocscan.library.utils import get_poc_files, url_seg
from main.tasks import run_task_in_gevent
from main.models import Tasks_status
from web.lib.crawler import MyCrawler
from pathlib import Path
import time

class Task_control(object):

    gevent_num = 100            # 协程数
    process_num = 5             # 进程数
    count = 0   # 每个进程，单独计数
    progress = 100              # 进度提醒的单位

    # 多进程函数，分配任务到各个进程
    def assign_task_in_multiprocessing(self, url_list, poc_file_dict):
        print('fuck2')
        run_task_in_gevent('123', 'fsdf')
        multiprocessing.Process(target=run_task_in_gevent.delay, args=('url_each_process', poc_file_dict )).start()
        # for url_each_process in url_list:
        #     multiprocessing.Process(target=run_task_in_gevent.delay, args=(url_each_process, poc_file_dict )).start()

    def launch(self, target, poc_name, task_name):
        # mypath = Path().absolute()
        # time.sleep(60)
        # print(mypath)
        self.set_task_status(target, task_name, status=True)
        url_list = url_seg(target, self.process_num)
        poc_file_dict = get_poc_files(poc_name)
        self.assign_task_in_multiprocessing(url_list, poc_file_dict)

    def set_task_status(self, target, task_name, status=True):
        try:
            t = Tasks_status(domains=target, task_name=task_name, status=status)
            t.save()
            return t
        except Exception as e :
            print (e)
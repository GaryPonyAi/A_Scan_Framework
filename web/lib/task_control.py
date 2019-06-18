# coding=utf-8

import multiprocessing
from pocscan.library.utils import get_poc_files, url_seg
from main.tasks import run_task_in_gevent
from main.models import Tasks_status,Project
from web.lib.crawler import MyCrawler
from pathlib import Path
import time
import os

class Task_control(object):

    gevent_num = 100            # 协程数
    process_num = 5             # 进程数
    count = 0   # 每个进程，单独计数
    progress = 100              # 进度提醒的单位

    # 多进程函数，分配任务到各个进程
    def assign_task_in_multiprocessing(self, targets, scan_tool):
        # print(targets)
        # run_task_in_gevent('123', 'fsdf')
        # print(targets[1])
        for target in targets:
            # run_task_in_gevent(target, scan_tool)
            multiprocessing.Process(target=run_task_in_gevent.delay, args=(target, scan_tool)).start()
        task_name = '/'.join(targets[0].split('/')[:-1])
        c = Project.objects.create(task_name=task_name)
        c.save()
        # for url_each_process in url_list:
        #     multiprocessing.Process(target=run_task_in_gevent.delay, args=(url_each_process, poc_file_dict )).start()

    def launch(self, targets, scan_tool, task_name):
        # mypath = Path().absolute()
        # time.sleep(60)
        # print(mypath)
        # file_targets = []
        # for target in targets:
        #     if os.path.isdir(target):
        #         onlyfiles = [f for f in listdir(target) if isfile(join(target, f))]
        #         file_targets.append(onlyfiles)
        #     else :
        #         file_targets.append(target)
        self.set_task_status(targets, task_name, status=True)

        # print(11111111111111)
        # url_list = url_seg(targets, self.process_num)
        # poc_file_dict = get_poc_files(poc_name)
        # self.assign_task_in_multiprocessing(url_list, poc_file_dict)
        self.assign_task_in_multiprocessing(targets, scan_tool)


    def set_task_status(self, targets, task_name, status=True):
        try:
            t = Tasks_status(domains=targets, task_name=task_name, status=status)
            t.save()
            return t
        except Exception as e :
            print (e)
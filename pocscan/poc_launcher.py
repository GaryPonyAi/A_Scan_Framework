# coding=utf-8

from pocscan.frame.beebeeto import Beebeeto
from pocscan.frame.pocsuite import PocSuite
from pocscan.frame.tangscan import Tangscan
from dj2.settings import SAVE_RESULT_API
import requests as req

from main.models import buglist,domain_ip,note,Result,Tasks_status
import time

import subprocess
import re


class Poc_Launcher(object):

    gevent_num = 100            # 协程数
    process_num = 5             # 进程数
    count = 0   # 每个进程，单独计数
    progress = 100              # 进度提醒的单位

    operator = {
        'beebeeto': Beebeeto,
        'pocsuite': PocSuite,
        'tangscan': Tangscan,
    }

    def __get_pocs_count(self, poc_files):
        return len(poc_files)

    def save_result(self, target, scan_tool, result):
        # result = str(result)
        # save_result_api_addr = SAVE_RESULT_API
        # post = {
        #      'target': target,
        #      'poc_file': poc_file,
        #      'result': result,

        # }
        # req.post(url=save_result_api_addr, data=post)
        # return result
        #Result(domain=target, poc_file=poc_file, result=result).save()
        # time.sleep(60)
        # newBug = Result.objects.create(domain=target, poc_file=poc_file, result=result)
        # newBug.save()
        # print("保存成功")
        # days_file = open('/home/jiarui/A_Scan_Framework/testtt.py','r')
        # with open('regression_edit_controller.cc', 'r') as f:
            # print(f.read())

        # filename = '/home/jiarui/A_Scan_Framework/test/test2.cpp'
        # time.sleep(60)
        print(scan_tool)
        if scan_tool == 0:
            out = subprocess.Popen(['flawfinder', filename], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            stdout,stderr = out.communicate()
            stdout = stdout.decode("utf-8")
            r = re.compile('[^:]+:(\\d+):\\s+\\[(\\d+)\\]\\s+([^:]+):\n((?:  .*\n)+)')
            result = r.findall(stdout)
            for i in range(len(result)):
                result[i] = list(result[i])
                result[i][3] = result[i][3].replace('\n  ', ' ').strip()
            description = '\n'.join([i[3] for i in result])
            task_name = '/'.join(filename.split('/')[:-1])
            # print(description)
            b = Result.objects.create(domain=filename, task_name=task_name, poc_file=scan_tool, result=','.join([i[0] for i in result]),
                        description=description)
            print(task_name)
            b.save()
        if scan_tool == 2:
            out = subprocess.Popen(['/home/jiarui/TscanCode/release/linux/TscanCodeV2.14.24.linux/TscanCodeV2.14.2395.linux/tscancode', filename], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            stdout,stderr = out.communicate()
            stdout = stdout.decode("utf-8")
            r = re.compile('\\[([^:\n]+):(\\d+)\\]:\\s*\\(([^)]+)\\)\\s*(.*)')
            result = r.findall(stdout)
            for i in range(len(result)):
                result[i] = list(result[i])
            description = '\n'.join([i[3] for i in result])
            task_name = '/'.join(filename.split('/')[:-1])
            b = Result.objects.create(domain=filename, task_name=task_name, poc_file=scan_tool, result=','.join([i[1] for i in result]),
                        description=description)
            b.save()


    def poc_verify(self, target, plugin_type, poc_file):
        result = self.operator.get(plugin_type)().run(target, poc_file)
        print(1234)
        if result.get('result', False):
            # self.save_result(target, poc_file, result.get('result'))
            self.save_result(target, poc_file, "12345")
        # return result
        self.save_result(target, poc_file, "12345")
        return "12345"
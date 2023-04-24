# coding=utf-8
"""
    @project: locust
    @Author：liuy2
    @file： testdemo.py
    @date：2023/4/24 23:32
"""



# coding=utf-8
import requests
from locust import HttpLocust,TaskSet,task


class MyBlogs(TaskSet):
    # 访问我的博客首页
    @task(1)
    def get_blog(self):
        # 定义请求头
        header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}

        req = self.client.get("/test",  headers=header, verify=False)
        if req.status_code == 200:
            print("success")
        else:
            print("fails")

class websitUser(HttpLocust):
    task_set = MyBlogs
    min_wait = 3000  # 单位为毫秒
    max_wait = 6000  # 单位为毫秒

if __name__ == "__main__":
    import os
    os.system("locust -f locusttest.py --host=https://www.cnblogs1.com/")
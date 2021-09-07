import datetime
import os
import requests
from unit import logger
import json

# 封装参数体
class BaseMethod:
    """
    封装api请求参数
    @:param method_type 请求类型
    @:param url 请求地址
    @:param header 请求头
    @:param timeout 超时时间 可选
    @:param datas 请求体参数
    @:param method_exit
    """
    def __init__(self, method_type, url, header, timeout=15, datas=None, method_exit=True):
        if not datas:
            datas = {}
        self.method_type = method_type
        self.url = url
        self.header = header
        self.datas = datas
        self.timeout = timeout
        self.method_exit = method_exit

# api自动请求工具
class Test_url(BaseMethod):
    """
    这个类是用来测试接口的类
    @:param BaseMethod 请求体，这是必传的参数
    """
    def __new__(cls, *args, **kwargs):
        cls.logger = logger
        logger.info("will begin use Test_url method")
        return object.__new__(*args, **kwargs)

    def __call__(self, *args, **kwargs):

        try:
            rv = requests.request(url=self.url,method=self.method_type, timeout=self.timeout, headers=self.header, data=json.dumps(self.datas))
        except Exception as e:
            logger.error(e.__str__())
            if self.method_exit:
                # exit程序终止函数
                exit()
        else:
            if rv.status_code != 200:
                logger.warning("Test : {0} , but reposes code is : {1}".format(self.url, rv.status_code))
                if self.method_exit:
                    exit()
            return json.loads(rv.text)

class bin_commods:

    def __new__(cls, *args, **kwargs):
        cls.logger = logger
        logger.info("will begin use system commods method")
        return object.__new__(*args, **kwargs)

    def __init__(self, cmd):
        self.cmd = cmd

    def __call__(self, *args, **kwargs):
        return logger.info(os.system(self.cmd))

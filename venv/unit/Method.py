import datetime
import os
import requests
from unit import logger
import json


class BaseMethod:
    def __init__(self, method_type, url, header, timeout=15, datas=None, method_exit=True):
        if not datas:
            datas = {}
        self.method_type = method_type
        self.url = url
        self.header = header
        self.datas = datas
        self.timeout = timeout
        self.method_exit = method_exit

class Test_url(BaseMethod):

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

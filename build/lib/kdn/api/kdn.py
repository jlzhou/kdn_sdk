#!/usr/bin/python3
# @Time    : 2020-03-25
# @Author  : Kevin Kong (kfx2007@163.com)

from .comm import Comm
from .query import Query
from .order import Order
import csv
import os


SANDBOXURL = "http://sandboxapi.kdniao.com:8080/kdniaosandbox/gateway/exterfaceInvoke.json"
URL = "http://api.kdniao.com"


class KDN(object):

    def __init__(self, client_id, api_key, sandbox=False):
        """
        params:
        client_id: 商户ID,
        api_key: API KEY,
        sandbox: 是否沙箱测试环境
        """
        self.client_id = client_id
        self.api_key = api_key
        self.sandbox = sandbox
        self.url = SANDBOXURL if self.sandbox else URL

    @classmethod
    def get_express_list(cls):
        """
        获取支持的公司列表
        返回包含代码和名称的字典
        """
        express = {}
        csv_path = os.path.dirname(os.path.dirname(__file__))
        with open(os.path.join(csv_path, "data/express.csv")) as f:
            for row in csv.reader(f):
                express[row[1].strip()] = row[0].strip()
        return express

    comm = Comm()
    query = Query()
    order = Order()

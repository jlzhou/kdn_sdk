#!/usr/bin/python3
# @Time    : 2020-03-26
# @Author  : Kevin Kong (kfx2007@163.com)

import unittest
from kdn.api.kdn import KDN


class TestOrder(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.client_id = "test1624824"
        cls.api_key = "f6bc7c23-7d7c-4dc8-9a73-506519393f6a"
        cls.kdn = KDN(cls.client_id, cls.api_key, sandbox=True)

    def test_order(self):
        res = self.kdn.order.order("1234561", "ZTO", 1, "张三", "0755-0907283",
                                   "13709076789", "广东省", "深圳市", "深南大道2009号", "李四", "0755-1111111",
                                   "13932080778", "广东省", "深圳市", "福田保税区", "书本", "9999999", "深圳市福田区福田保税区")
        print(res)

if __name__ == "__main__":
    unittest.main()

#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Time-stamp: <2017-01-06 17:03:39 Friday by wls81>

#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Time-stamp: <2013-09-06 00:43:23 Friday by zhangguhua>

# @version 1.0
# @author your name
import os

import tushare as ts
import cPickle as pickle
# 数据存储路径
data_path = os.path.dirname(os.path.abspath(__file__)) + '/data'

class TushareAPI:
    """
    tushare的功能封装，常用到一些函数
    """
    def __init__(self, init_file=None):
        """初始化函数

        :param init_file: 加载的初始化文件
        :returns: None
        :rtype: NoneType

        """
        # 存储所有股票信息列表
        self.market_info = None
        market_info_file = data_path + ("/.market_info")
        # 存储股票代码列表
        self.code_list = []
        code_list_file = data_path + ("/.code_list")
        # 存储股票名称列表
        self.name_list = []
        name_list_file = data_path + ("/.name_list")
        try:
            with open(market_info_file) as mif, open(code_list_file) as clf, open(name_list_file) as nlf :
                self.market_info = pickle.load(mif)
                self.code_list = pickle.load(clf)
                self.name_list = pickle.load(nlf)
        except :
            self.market_info = ts.get_today_all()
            self.code_list = self.market_info[['code', 'name']]['code'].tolist()
            self.name_list = self.market_info[['code', 'name']]['name'].tolist()
            with open(market_info_file, 'wb') as mif, open(code_list_file, 'wb') as clf, open(name_list_file, 'wb') as nlf:
                pickle.dump(self.market_info, mif)
                pickle.dump(self.code_list, clf)
                pickle.dump(self.name_list, nlf)
        
    def varifi_code(self, code):
        """判断股票代码是否存在
        
        :param code: 需要查询的股票代码
        :returns: 代码存在返回True否则返回False
        :rtype: bool

        """
        return code in self.code_list


    def varifi_name(self, name):
        """判断股票名称是否存在

        :param name: 需要查询的股票名称
        :returns: 名称存在返回True否则返回False
        :rtype: bool

        """
        return name in self.name_list

    def get_stock_info(self, query):
        """获取股票的实时信息

        :param query: 6位数字股票代码，或者指数代码（sh=上证指数 sz=深圳成指 hs300=沪深300指数 sz50=上证50 zxb=中小板 cyb=创业板）\
        可输入的类型：str、list、set或者pandas的Series对象
        :returns: 返回股票信息的dict
        :rtype: dict

        """
        info = ts.get_realtime_quotes(query)
        return info.to_dict()
    def get_stock_price(self, query):
        stock_info = self.get_stock_info(query)
        return stock_info['price']
if __name__ == "__main__":
    tsAPI = TushareAPI()
    print tsAPI.varifi_code("000333")
    print tsAPI.get_stock_info('000333')
    print tsAPI.get_stock_info(['000333','002038'])
    print tsAPI.get_stock_price('000333')
    print tsAPI.get_stock_price(['000333','002038'])

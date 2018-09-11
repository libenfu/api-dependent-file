#coding:utf-8
from api_mode import API_Mode
import json
#获取牌价

def ticker():
    symbol='bz_usdt'  #交易对
    data = API_Mode().ticker(symbol)
    print json.dumps(data.json(),indent=2)




#获取所有牌价数据
def tickerall():
    data = API_Mode().tickerall()
    print json.dumps(data.json(), indent=2)



#获取深度数据
def depth():
    symbol='bz_usdt'   #交易对
    data = API_Mode().depth(symbol)
    print json.dumps(data.json(), indent=2)



# 成交单
def order():
    symbol = 'bz_usdt'    #交易对
    data = API_Mode().order(symbol)
    print json.dumps(data.json(), indent=2)



#获取K线数据
def kline():
    symbol = 'bz_usdt'   #交易对
    resolution = '1min'  #时间   分钟：Xmin ,小时：Xhour , 天：Xday
    size = '300'
    toTime = '2018-07-27 20:53:00'  #获取toTime时间前的数据
    data = API_Mode().kline(symbol,resolution,size,toTime=toTime)
    print json.dumps(data.json(), indent=2)



#获取交易对信息
def symbolList():
    data = API_Mode().symbolList()
    print json.dumps(data.json(), indent=2)



#获取当前法币汇率信息
def currencyRate():
    data = API_Mode().currencyRate()
    print json.dumps(data.json(), indent=2)



#获取虚拟货币法币汇率信息
def currencyCoinRate():
    data = API_Mode().currencyCoinRate()
    print json.dumps(data.json(), indent=2)




#获取币种对应汇率信息
def coinRate():
    data = API_Mode().coinRate()
    print json.dumps(data.json(), indent=2)




#提交委托单
def addEntrustSheet():
    _type = '2'             #买：1  卖：2
    price = '1000'            #价格
    number = '10'            #数量
    symbol = 'bz_usdt'      #交易对
    data = API_Mode().addEntrustSheet(_type,price,number,symbol)
    print json.dumps(data.json(), indent=2)


#撤销委托单
def cancelEntrustSheet():
    entrustSheetId='837119868'   #委托单ID
    data = API_Mode().cancelEntrustSheet(entrustSheetId)
    print json.dumps(data.json(), indent=2)




#批量撤销委托单
def cancelAllEntrustSheet():
    trustAllId='837120409,837120552'   #委托单ID（多个中间逗号隔开）
    data = API_Mode().cancelAllEntrustSheet(trustAllId)
    print json.dumps(data.json(), indent=2)



#获取个人历史委托单列表
def getUserHistoryEntrustSheet():
    coinFrom = 'bz'                     #代币
    coinTo = 'usdt'                       #法币
    _type = '2'                          #买：1  卖：2  默认：返回全部
    page = '2'                           #要查看的页数
    pageSize = '4'                       #一页多少条数据
    # startTime = '2017-06-12 12:00:00'  # 开始时间
    # endTime = '2018-06-14 12:00:00'     #结束时间
    data = API_Mode().getUserHistoryEntrustSheet(coinFrom,coinTo,page,pageSize,_type=_type)
    print json.dumps(data.json(), indent=2)



#获取当前委托
def getUserNowEntrustSheet():
    coinFrom = 'bz'                     #代币
    coinTo = 'usdt'                       #法币
    # _type = '2'                          #买：1  卖：2   默认：返回全部
    page = '2'                           #要查看的页数
    pageSize = '2'                       #一页多少条数据
    # startTime = '2017-06-12 12:00:00'    #开始时间
    # endTime = '2018-06-08 12:00:00'      #结束时间
    data = API_Mode().getUserNowEntrustSheet(coinFrom,coinTo,page,pageSize)
    print json.dumps(data.json(), indent=2)



#获取委托单详情
def getEntrustSheetInfo():
    entrustSheetId = '815117319'           #委托单ID
    data = API_Mode().getEntrustSheetInfo(entrustSheetId)
    print json.dumps(data.json(), indent=2)



#获取用户所有资产
def getUserAssets():
    data  = API_Mode().getUserAssets()
    print json.dumps(data.json(), indent=2)


if __name__=="__main__":
    # ticker()
    # tickerall()
    # depth()
    # order()
    # kline()
    # symbolList()
    # currencyRate()
    # currencyCoinRate()
    # coinRate()
    # addEntrustSheet()
    # cancelEntrustSheet()
    # cancelAllEntrustSheet()
    # getUserHistoryEntrustSheet()
    # getUserNowEntrustSheet()
    # getEntrustSheetInfo()
    getUserAssets()





'''
Created by auto_sdk on 2020.11.26
'''
from top.api.base import RestApi
class TradeOrderskuUpdateRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.oid = None
		self.sku_id = None
		self.sku_props = None

	def getapiname(self):
		return 'taobao.trade.ordersku.update'

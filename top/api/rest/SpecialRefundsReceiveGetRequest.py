'''
Created by auto_sdk on 2020.06.09
'''
from top.api.base import RestApi
class SpecialRefundsReceiveGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.buyer_nick = None
		self.end_modified = None
		self.fields = None
		self.page_no = None
		self.page_size = None
		self.start_modified = None
		self.status = None
		self.type = None
		self.use_has_next = None

	def getapiname(self):
		return 'taobao.special.refunds.receive.get'

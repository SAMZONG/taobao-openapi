'''
Created by auto_sdk on 2020.10.27
'''
from top.api.base import RestApi
class MiniappTemplateOnlineappRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.app_id = None
		self.app_version = None
		self.clients = None
		self.template_id = None
		self.template_version = None

	def getapiname(self):
		return 'taobao.miniapp.template.onlineapp'

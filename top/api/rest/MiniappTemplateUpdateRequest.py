'''
Created by auto_sdk on 2020.05.15
'''
from top.api.base import RestApi
class MiniappTemplateUpdateRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.clients = None
		self.ext_json = None
		self.id = None
		self.template_id = None
		self.template_version = None

	def getapiname(self):
		return 'taobao.miniapp.template.update'

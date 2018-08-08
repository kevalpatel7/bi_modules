from odoo import fields,models,api, _
from odoo.osv import expression


class man(models.Model):
	
	_inherit = "res.partner"


	@api.model
	def name_search(self, name='', args=None, operator='ilike', limit=100):

		args = args or []


		res =  super(man, self).name_search(name='', args=None, operator='ilike', limit=100)
		print "res==========================-----------",res
		return res



	@api.multi
	@api.depends('name')
	def name_get(self):
		res=super(man,self).name_get()
		print "---------self-----------------",self


		return res

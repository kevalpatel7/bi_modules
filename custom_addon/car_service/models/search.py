from odoo import fields,models,api, _
from odoo.osv import expression
from openerp.api import Environment as Env


class search(models.Model):
	_inherit = "res.partner",'res.lang'



	@api.model
	def name_search(self, name='', args=None, operator='ilike', limit=100):
		args = args or []
		domain = []
		print ("============name==111================",name)
		if name:
			print ("============name===================",name)
			domain = ['|', ('phone', operator, name + '%'), '|',('name', operator, name+'%'),('mobile','=ilike',name + '%')]
			print ("============domain===================",domain)
		#if operator in expression.NEGATIVE_TERM_OPERATORS:
				#self.domain = ['&', '!'] + domain[1:]
		

		res =  super(search, self).search(domain + args, limit=limit ).name_get()

		print "===========aaaaaaaaaaaaaaaaaaaaa==============="
		return res



	@api.multi
	@api.depends('name', 'country_id','lang')
	def name_get(self):
		result = []
		#res=super(search,self).name_get()
		print "======================================self==========",self
		print "=========================res======================="
		# value = dict(self.fields['lang']._description_selection(self.evn)).get(self.type)
		for a in self:
			print "===========================self.name===========",a.country_id.id
			print "=======laaaaaaan================================",a.lang
			name = str(a.country_id.name) + ' ' + a.name + ' '+ a.lang
			print ("============name===================",name)
			result.append((a.id,name))
			print ("============result===================",result)
		#res = super(search, self).name_get()

		print "=================================="
		return result




	# @api.model
	# def default_get(self, default_fields):
	# 	print "============default=============",default_fields
	# 	res = super(search, self).default_get(default_fields)
	# 	print "============default after===========",default_fields
	# 	print "================res===========================",res
	# 	if res.get('lang'):
	# 		print res.lang,"---------++++++++++++++++++++________________________"
	# 	return res
		







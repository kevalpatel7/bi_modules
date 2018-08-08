from odoo import fields,models,api, _





class SaleOrder(models.Model):
	_inherit = "sale.order"


	date= fields.Date(String='date')
	location=fields.Many2one('stock.location',string='location')

	# @api.model
	# def create(self, vals):
	# 	print "=========SaleOrder=====create=============="
	# 	result = {}
	# 	return result

	
	#location= fields.Many2one(String='location')


class saleorderline(models.Model):
	_inherit = "sale.order.line"


	date= fields.Date(String='date')
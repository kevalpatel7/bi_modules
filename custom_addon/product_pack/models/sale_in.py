from odoo import fields,models,api, _

class sale_in(models.Model):

	_inherit = "sale.order"



	keval=fields.Char(string="keval")
	
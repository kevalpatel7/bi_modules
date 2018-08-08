from odoo import fields,models,api, _



class vehicle(models.Model):
	_inherit = "product.template"


	vehicle_type=fields.Selection([('car','car'),('bike','bike')],string='Vehicle type')
	rent=fields.Boolean(string='Can be rented')


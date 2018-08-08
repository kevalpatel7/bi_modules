from odoo import fields,models,api, _



class bike(models.Model):
	_name='bike.product'

	name=fields.Char(string='Enter bike name')
	rent=fields.Integer(string='Rent price')
	num_plate=fields.Char(string='Number plate')

